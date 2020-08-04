T = int(input())

while T:
    T -= 1
    expression = input()
    expression_transform = ""
    operators = []
    for c in expression:
        if c == '(':
            continue
        elif c.isalpha():
            expression_transform += c
        elif c == ')':
            expression_transform += operators[-1]
            operators = operators[0:-1]
        else:
            operators.append(c)
    
    print(expression_transform)
