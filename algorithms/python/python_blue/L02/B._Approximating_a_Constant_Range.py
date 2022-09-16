n = int(input())
a = list(map(int, input().split()))

cnt = [0] * 100001

l = res = count = 0
for r in range(n):
    if (cnt[a[r]] == 0):
        count += 1
    cnt[a[r]] += 1
    while count > 2:
        cnt[a[l]] -= 1
        if cnt[a[l]] == 0:
            count -= 1
        l += 1
    res = max(res, r - l + 1)

print(res)
