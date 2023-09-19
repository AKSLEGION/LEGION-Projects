import random
import os
import hashlib

interface = 'Home'
words = open('words.txt','r').read().split(', ')
wins = 0
losses = 0
username = "Guest"
guest = True

def home_prompt():
    hangman = "\n\tHANGMAN\n\n"
    print(f"{hangman}Do you want to login or play as a guest?\n1. Press L to login.\n2. Press R to register.\n3. Press G to play as guest.\n4. Press E to exit the game.\n")

def register_prompt():
    from users import users
    print("\n\tHANGMAN\n\n\nProvide Username and Password to register.\nType !Home to go back to home.")
    print('\nUsername:',end=' ')
    register_username = input()
    if register_username == "!Home":
        return (register_username,True,0,0)
    register_username_hash = hashlib.sha256(register_username.encode()).hexdigest()
    while register_username_hash in users:
        print("This username has already been taken.\nType !Login to go to login page.")
        print('\nUsername:',end=' ')
        register_username = input()
        if register_username == "!Home" or register_username == "!Login":
            return (register_username,True,0,0)
        register_username_hash = hashlib.sha256(register_username.encode()).hexdigest()
    print('\nPassword:',end=' ')
    register_password = input()
    if register_password == "!Home":
        return (register_password,True,0,0)
    register_password_hash = hashlib.sha256(register_password.encode()).hexdigest()
    users[register_username_hash]={'password':register_password_hash,'wins':0,'losses':0}
    (f:=open('users.py','w')).write(f"users = {users}")
    f.close()
    return (register_username,False,0,0)

def login_prompt():
    from users import users
    print("\n\tHANGMAN\n\n\nProvide Username and Password to login.\nType !Home to go back to home.")
    print('\nUsername:',end=' ')
    login_username = input()
    if login_username == "!Home":
        return (login_username,True,0,0)
    login_username_hash = hashlib.sha256(login_username.encode()).hexdigest()
    while login_username_hash not in users:
        print("This Username doesn't exist.\nType !Register to go to register page.")
        print("\nUsername:",end=' ')
        login_username = input()
        if login_username == "!Home" or login_username == "!Register":
            return (login_username,True,0,0)
        login_username_hash = hashlib.sha256(login_username.encode()).hexdigest()
    print('\nPassword:',end=' ')
    login_password = input()
    if login_password == "!Home":
        return (login_password,True,0,0)
    login_password_hash = hashlib.sha256(login_password.encode()).hexdigest()
    while login_password_hash != users[login_username_hash]['password']:
        print("Incorrect Password\nTry Again.\nType !Login to login with another username.")
        print("\nPassword:",end=' ')
        login_password = input()
        if login_password == "!Home" or login_password == '!Login':
            return (login_password,True,0,0)
        login_password_hash = hashlib.sha256(login_password.encode()).hexdigest()
    return (login_username,True,users[login_username_hash]['wins'],users[login_username_hash]['losses'])

def game_prompt(first):
    hangman = "\n\tHANGMAN\n\n"
    again = ""
    play = "1. Press Y to play.\n"
    stats = f"User: {username}\nWins: {wins}\nLosses: {losses}\n\n"
    if not first:
        hangman = ''
        again = ' again'
        play = '1. Press C to continue.\n'
    print(f"{hangman}{stats}Do you want to play{again}?\n{play}2. Press E to logout and exit to home.\n")

def Intro():
    print("\nWelcome to Hangman.\n\nI have chosen a word and omitted some letters from it.\nYou have to guess letters that might be in the word and fill it.\nIf you guess wrong you lose a life.\nLose 6 lives and you die.\n")

def death():
    print(f"Enough guesses buddy.\nYou have lost all your lives.\nGame Over.\nThe word was: {word}\n")

def win():
    print(f"Well Done.\nYou have guessed the complete word.\nThe word was: {word}\n")

def guess_prompt():
    print(f"Guess a letter.\nYou have {lives} lives left.\n\nFill the spaces.\n\n\t")
    for c in word:
        if c in omit:
            print('_',end=' ')
        else:
            print(c,end=' ')
    print("\n\nLetter Guessed:",end=' ')

def save_data():
    from users import users
    username_hash = hashlib.sha256(username.encode()).hexdigest()
    users[username_hash]['wins'] = wins
    users[username_hash]['losses'] = losses
    (f:=open('users.py','w')).write(f"users = {users}")

def handle_guess(guess,lives):
    if len(guess) > 1:
        print("\nPlease only guess 1 letter at a time.\n")
    elif guess.upper() not in word and guess.lower() not in word:
        lives -= 1
        print(f"\nWrong Guess. You have {lives} lives left.\n")
    elif guess not in omit:
        print("\nThis letter has already been displayed. Try another.\n")
    else:
        omit.remove(guess.upper())
        omit.remove(guess.lower())
        print(f"\nGood guess. {guess} is in this word.\n")
    return lives

while True:
    os.system('cls')
    if interface == 'Home':
        home_prompt()
        choice = input()
        while choice not in ('L','R','G','E'):
            print("\nInvalid Choice.\n")
            choice = input()
        if choice == 'L':
            interface = 'Login'
        elif choice == 'R':
            interface = 'Register'
        elif choice == 'G':
            username = "Guest"
            guest = True
            interface = "Game"
        elif choice == 'E':
            os.system('cls')
            break
    elif interface == 'Register':
        username,guest,wins,losses = register_prompt()
        if username in ("!Home",'!Login'):
            interface = username[1:]
            username = "Guest"
        else:
            interface = "Game"
    elif interface == "Login":
        username,guest,wins,losses = login_prompt()
        if username in ("!Home","!Register","!Login"):
            interface = username[1:]
            username = "Guest"
        else:
            interface = "Game"
    elif interface == 'Game':
        game_prompt(1)
        choice = input()
        while choice not in ('Y','E'):
            print("\nInvalid Choice.\n")
            choice = input()
        if choice == 'E':
            interface = "Home"
            if not guest:
                save_data()
        else:
            Intro()
            word = random.choice(words)
            omit = list(set([c.upper() for c in word if c != ' '] + [c.lower() for c in word if c != ' ']))
            chars = len(omit)//6
            for _ in range(chars):
                display = random.choice(omit)
                omit.remove(display.upper())
                omit.remove(display.lower())
            lives = 6
            guessed = set([])
            while True:
                if not lives:
                    death()
                    losses += 1
                    break
                guess_prompt()
                guess = input()
                lives = handle_guess(guess,lives)
                if not len(omit):
                    win()
                    wins += 1
                    break
            game_prompt(0)
            choice = input()
            while choice not in ('C','E'):
                print("\nInvalid Choice.\n")
                choice = input()
            if choice == 'E':
                interface = "Home"
                if not guest:
                    save_data()
            else:
                continue