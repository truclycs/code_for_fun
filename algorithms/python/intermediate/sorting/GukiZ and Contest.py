n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = (a[i], i)

a.sort(key=lambda x: x[0], reverse=True)

res = [0] * n
res[a[0][1]] = 1
rank = 1
cnt = 1
for i in range(1, n):
    if a[i][0] < a[i - 1][0]:
        rank += cnt
        cnt = 1
    else:
        cnt += 1

    res[a[i][1]] = rank

print(*res)
