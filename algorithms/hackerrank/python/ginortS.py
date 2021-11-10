s = input()

up = []
low = []
even = []
odd = []

for c in s:
    if c.isnumeric():
        if int(c) % 2 == 0:
            even.append(c)
        else:
            odd.append(c)
    elif c.isupper():
        up.append(c)
    else:
        low.append(c)

low.sort()
up.sort()
odd.sort()
even.sort()
res = "".join(low + up + odd + even)

print(res)