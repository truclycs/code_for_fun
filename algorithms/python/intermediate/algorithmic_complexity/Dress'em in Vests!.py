n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0
pairs = []
while i < n and j < m:
    if a[i] - x <= b[j] <= a[i] + y:
        pairs.append((i + 1, j + 1))
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
        
print(len(pairs))
for x, y in pairs:
    print(x, y)
        