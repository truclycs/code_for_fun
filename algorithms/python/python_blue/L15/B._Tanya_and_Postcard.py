s = input()
t = input()
n = len(s)
made = [False] * n
d = dict()

for c in t:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

yays = whoops = 0

for i in range(n):
    if s[i] in d and d[s[i]] > 0: 
        d[s[i]] -= 1
        yays += 1
        made[i] = True

for i in range(n):
    if made[i] == False:
        c = s[i]
        if c.upper() in d and d[c.upper()] > 0:
            d[c.upper()] -= 1       
            whoops += 1
        elif c.lower() in d and d[c.lower()] > 0:
            d[c.lower()] -= 1
            whoops += 1

print(yays, whoops)