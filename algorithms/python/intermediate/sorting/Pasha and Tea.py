n, w = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
total = min(a[0], a[n] / 2) * 3 * n
print(min(total, w))
