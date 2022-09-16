n, x0, y0 = map(int, input().split())
shot = set()
tmp = 0
for _ in range(n):
    x, y = map(int, input().split())
    if y == y0:
        tmp = 1
        continue
    shot.add((x - x0) / (y - y0))
print(len(shot) + tmp)


