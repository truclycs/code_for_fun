n = int(input())
s = input()
cnt = [0] * 26
is_pangram = True
for x in s:
    if 'A' <= x <= 'Z':
        cnt[ord(x) - 65] += 1
    else:
        cnt[ord(x) - 97] += 1

for i in range(26):
    if cnt[i] == 0:
        is_pangram = False
        break

if is_pangram:
    print("YES")
else:
    print("NO")
