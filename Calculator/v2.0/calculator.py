import os

op = "0123456789+-*x/()"
ans = 0

def prompt(ans,calc):
    use = "You can use the previous result as \'ans\' in your expression.\n"
    other = "other"
    calculator = '\n\n\tCalculator\n'
    use_ = ''
    other_ = ''
    if ans:
        other_ = other
        use_ = use
        if not calc:
            calculator = ''
    print(f"{calculator}\nGive me an{other_} expression.\nI'll give you the result.\n{use_}")

os.system('cls')
while True:
    prompt(ans,0)
    expression = input().replace(' ','').replace("ans",str(ans)).replace('x','*')
    _ = os.system('cls')
    prompt(ans,1)
    print(expression)
    if any(c not in op for c in expression):
        print("Invalid Expression\n")
        continue
    ans = eval(expression)
    print("\nans =",ans)