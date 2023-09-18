import os

nums = "0123456789"
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

def bracket_process(op_stack):
    if '(' not in op_stack:
        return op_stack
    bracket_processed = []
    in_bracket = False
    b_count = 0
    for i in range(len(op_stack)):
        if op_stack[i] == '(':
            in_bracket = True
            b_count += 1
            if b_count == 1:
                last = i
        elif op_stack[i] == ')':
            b_count -= 1
        if b_count == 0:
            if in_bracket:
                bracket_processed.append(solve(op_stack[last+1:i]))
                in_bracket = False
            else:
                bracket_processed.append(op_stack[i])
    return bracket_processed

def muldiv(op_stack):
    muldiv_stack = []
    i = 0
    while i < len(op_stack):
        if op_stack[i] == '*' or op_stack[i] == 'x':
            muldiv_stack[-1] *= op_stack[i+1]
            i+=2
        elif op_stack[i] == '/':
            muldiv_stack[-1] /= op_stack[i+1]
            i+=2
        else:
            muldiv_stack.append(op_stack[i])
            i+=1
    return muldiv_stack

def addsub(op_stack):
    addsub_stack = []
    i = 0
    while i < len(op_stack):
        if op_stack[i] == '+':
            addsub_stack[-1] += op_stack[i+1]
            i+=2
        elif op_stack[i] == '-':
            addsub_stack[-1] -= op_stack[i+1]
            i+=2
        else:
            addsub_stack.append(op_stack[i])
            i+=1
    return addsub_stack

def solve(op_stack):
    op_stack = bracket_process(op_stack)
    op_stack = muldiv(op_stack)
    op_stack = addsub(op_stack)
    if len(op_stack) == 1:
        return op_stack[0]
    else:
        return "The expression is Incorrect"

os.system('cls')
while True:
    prompt(ans,0)
    expression = input().replace(' ','').replace("ans",str(ans))
    _ = os.system('cls')
    prompt(ans,1)
    print(expression)
    if any(c not in op for c in expression):
        print("Invalid Expression\n")
        continue
    op_stack = []
    last = 0
    for index in range(len(expression)):
        if expression[index] not in nums:
            if last != index:
                op_stack.append(int(expression[last:index]))
            op_stack.append(expression[index])
            last = index+1
    if last != len(expression):
        op_stack.append(int(expression[last:]))
    ans = solve(op_stack)
    print("\nans =",ans)