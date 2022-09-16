n, w = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
res = 0
g = a[0] * n + a[0] * 2 * n
b = a[n] * n + (a[n] / 2) * n
if g > res and g <= w and a[0] * 2 <= a[n]:
    res = g
elif b > res and b <= w and a[n] // 2 <= a[0]:
    res = b
else:
    res = w

print('{:.8f}'.format(res))