s = input()
t = input()
n = len(s)
made = [False] * n
a = [0] * 130

for c in t:
    a[ord(c)] += 1

yay = whoops = 0

for i in range(n):
    if a[ord(s[i])] > 0:
        a[ord(s[i])] -= 1
        yay += 1
        made[i] = True

for i in range(n):
    if made[i] == False:
        c = s[i]
        if c.islower() and a[ord(c.upper())] > 0:
            a[ord(c.upper())] -= 1       
            whoops += 1
        elif c.isupper() and a[ord(c.lower())] > 0:
            a[ord(c.lower())] -= 1
            whoops += 1

print(yay, whoops)
