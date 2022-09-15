n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

j = 0
u = []
v = []
for i in range(n):
    while j < m and b[j] < a[i] - x:
        j += 1
    if j < m and b[j] <= a[i] + y:        
        u.append(i + 1)
        v.append(j + 1)
        j += 1

print(len(u))
for i in range(len(u)):
    print(u[i], v[i])

