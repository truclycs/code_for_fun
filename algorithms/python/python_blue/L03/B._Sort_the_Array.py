n = int(input())
t = list(map(int, input().split()))
a = []
a.append(0)
for x in t:
    a.append(x)
a.append(1000000001)
cnt = l = r = 0
yes = True
x = True
for i in range(1, len(a)):
    if cnt == 0:
        if a[i] < a[i - 1]:
            l = i - 1
            cnt += 1
    elif a[i] > a[i - 1]:
            if a[i] < a[l] or a[i-1] < a[l - 1]:
                yes = False
                break
            if x and i > 1:
                r = i - 1
                x = False
    elif not x:
        yes = False
        break
    
if yes:
    print("yes")
    if cnt == 0:
        print(1, 1)
    else:
        print(l, r)
else:
    print("no")