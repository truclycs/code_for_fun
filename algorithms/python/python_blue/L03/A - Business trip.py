k = int(input())
a = list(map(int, input().split()))

a.sort()
res = cm = 0
for i in range(11, -1, -1):
    if (cm >= k):
        break
    cm += a[i]
    res += 1

if (cm < k):
    print(-1)
else:
    print(res)