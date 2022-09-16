s = input()
t = input()

tmp = ""
for i in range(len(s) - 1, -1, -1):
    if s[i] == 'z':
        tmp += 'a'
    else:
        break

tmp += chr(ord(s[i]) + 1)
for j in range(i - 1, -1, -1):
    tmp += s[j]

res = ""
for i in range(len(tmp) - 1, -1, -1):
    res += tmp[i]

if res == t:
    print("No such string")
else:
    print(res)
