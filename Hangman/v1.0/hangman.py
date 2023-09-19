import random
import os

words = open('words.txt','r').read().split(', ')
wins = 0
losses = 0

def prompt(first):
    hangman = "\n\tHANGMAN\n\n"
    again = ""
    play = "1. Press Y to play.\n"
    stats = f"Wins: {wins}\nLosses: {losses}\n\n"
    if not first:
        hangman = ''
        again = ' again'
        play = '1. Press C to continue.\n'
    print(f"{hangman}{stats}Do you want to play{again}?\n{play}2. Press N to exit the game.\n")

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
    prompt(1)
    choice = input()
    while choice != 'N' and choice != 'Y':
        print("\nInvalid Choice.\n")
        choice = input()
    if choice == 'N':
        os.system('cls')
        break
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
        prompt(0)
        choice = input()
        while choice != 'N' and choice != 'C':
            print("\nInvalid Choice.\n")
            choice = input()
        if choice == 'N':
            os.system('cls')
            break
        else:
            continue