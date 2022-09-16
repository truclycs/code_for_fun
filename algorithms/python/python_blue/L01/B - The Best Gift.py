n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * (m + 1)
for x in a:
    cnt[x] += 1   

res = 0
for i in range(1, m):
    for j in range(i + 1, m + 1):
        res += cnt[i] * cnt[j]

print(res)