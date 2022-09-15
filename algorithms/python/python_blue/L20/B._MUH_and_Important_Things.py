n = int(input())
l = list(map(int, input().split()))
a = []
for i in range(n):
    a.append((l[i], i + 1))

a.sort()
cnt = 0
i = 0
maxi = 0;
while i < n:
    c = 0
    j = i
    while i < n: 
        if a[i][0] == a[j][0]:
            c += 1
        else:
            break
        i += 1
    if c > 1:
        cnt += 1
    maxi = max(c, maxi)

if cnt < 1 or (cnt == 1 and maxi < 3):
    print("NO")
else:
   
    print("YES")

    for i in range(n):
        print(a[i][1], end = " ")
    print()

    for i in range(1, n):
        if a[i][0] == a[i - 1][0]:
            a[i], a[i - 1] = a[i - 1], a[i]
            break

    for i in range(n):
        print(a[i][1], end = " ")

    print()

    for i in range(n - 1, 0, -1):
        if a[i][0] == a[i - 1][0]:
            a[i], a[i - 1] = a[i - 1], a[i]
            break

    for i in range(n):
        print(a[i][1], end = " ")
        