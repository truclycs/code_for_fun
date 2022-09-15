n, s = map(int, input().split())
location = dict()
res = -1
for _ in range(n):
    x, y, k = map(int, input().split())
    r = x ** 2 + y ** 2
    if r in location:
        location[r] += k
    else:
        location[r] = k
    
radius = []
for r in location:
    radius.append(r)
radius.sort()
for r in radius:
    s += location[r]
    if s >= 10 ** 6:
        res = r ** 0.5
        break

print(res)

