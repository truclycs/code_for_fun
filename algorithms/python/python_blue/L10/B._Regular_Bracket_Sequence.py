s = input()
a = []
count = 0
for c in s:
    if c == '(':
        a.append(c)
    elif len(a) != 0:
        count += 2
        a.pop()
print(count)
