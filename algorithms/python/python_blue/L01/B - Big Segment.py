n = int(input())
l = []
r = []
for i in range(n):
    x, y = map(int, input().split())
    l.append(x)
    r.append(y)

left = l[0]
right = r[0]
for i in range(n):
    if (l[i] < left):
        left = l[i]
    if (r[i] > right):
        right = r[i]

res = -1
for i in range(n):
    if (left == l[i] and right == r[i]):
        res = i + 1

print(res)