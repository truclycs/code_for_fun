def transform(exp):
    res = ""
    op = []
    for e in exp:
        if e in ['+', '-', '*', '/', '^']:
            op.append(e)
        elif e == ')':
            res += op.pop()
        elif e != '(':
            res += e

    while op:
        res += op.pop()

    return res


n = int(input())
for _ in range(n):
    exp = input()
    print(transform(exp))    