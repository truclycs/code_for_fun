n, m  = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()
res = 0
for i in range(m):
    if a[i] < 0:
        res += a[i]
    else:
        break

print(abs(res))