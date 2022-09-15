s = input()
tmp = 97
res = 0
for c in s:
    if abs(ord(c) - tmp) <= 13:
        res += abs(ord(c) - tmp)
    else:
        res += 26 - abs(ord(c) - tmp)
    tmp = ord(c)

print(res)

