s = input()

atom = {'C': 12,
        'O': 16,
        'H': 1}

a = []
for c in s:
    if c == '(':
        a.append(c)
    elif c.isdigit():
        a[-1] = a[-1] * int(c)
    elif c == ')':
        while a[-2] != '(':
            tmp = a.pop()
            a[-1] = a[-1] + tmp
        a[-2] = a[-1]
        a = a[:-1]
    else:
        a.append(atom[c])

print(sum(a))