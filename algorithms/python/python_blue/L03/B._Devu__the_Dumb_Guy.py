n, x = map(int, input().split())
c = list(map(int, input().split()))

c.sort()
res = 0
for i in c:
    res += i * x
    if (x > 1):
        x -= 1

print(res)
