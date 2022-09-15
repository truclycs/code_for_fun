a = []
n = int(input())
for i in range(n):
    x = int(input())
    a.append(x)

a.sort()

if n % 2 == 0:
    print((a[n // 2] + a[n // 2 - 1]) / 2)
else:
    print(a[n // 2])