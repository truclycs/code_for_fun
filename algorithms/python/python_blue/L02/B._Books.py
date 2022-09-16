
n, t = map(int, input().split())
a = list(map(int, input().split()))

l = time = res = 0
for r in range(n):
    time += a[r]
    while l <= r and time > t:
        time -= a[l]
        l += 1
    if r - l + 1 > res:
        res = r - l + 1
            
print(res)
