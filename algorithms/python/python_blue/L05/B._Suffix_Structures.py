s = input()
t = input()

cnt = [0] * 123

for c in t:
    cnt[ord(c)] += 1    

for c in s:
    if cnt[ord(c)] > 0:
        cnt[ord(c)] -= 1

flag = True
for c in t:
    if cnt[ord(c)] > 0:
        flag = False

if flag and len(s) == len(t):
    print("array")
elif flag:
    i = 0
    count = 0
    for x in t:
        while i < len(s):
            if (s[i] == x):
                count += 1
                i += 1
                break
            i += 1
    if count == len(t):
        print("automaton")
    else:
        print("both")
else:
    print("need tree")
