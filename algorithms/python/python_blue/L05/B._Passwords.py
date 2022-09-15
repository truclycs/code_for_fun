n, k = map(int, input().split())
   
s = []
for i in range(n):
    x = input()
    s.append(x)

password = input()
cnt = 0
flag = False

s.sort(key = len)

best = worst = 0
for i in range(n):
    if len(s[i]) == len(password) and flag == False:
        best = i + 1
        flag = True
    elif len(s[i]) > len(password):
        worst = i 
        break
if worst == 0:
    worst = n
print(best + ((best - 1) // k) * 5, worst + ((worst - 1) // k) * 5)