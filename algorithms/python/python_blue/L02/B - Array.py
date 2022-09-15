n, k = map(int, input().split())
a = list(map(int, input().split()))
visited = 100001 * [0]

count = 0
l = 0
r = -1
for i in range(n):
    if (visited[a[i]] == 0):
        count += 1
    visited[a[i]] += 1
    if (count == k):
        r = i
        break

if (r == -1):
    print(-1, -1)
else:
    for i in a:
        if (visited[i] > 1):
            l += 1
            visited[i] -= 1
        else:
            break
    print(l + 1, r + 1)