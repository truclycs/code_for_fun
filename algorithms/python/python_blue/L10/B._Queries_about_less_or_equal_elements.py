class array:
    def __init__(self, value, id):
        self.value = value
        self.id = id

n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(array(x[i], i))
b = []
for i in range(m):
    b.append(array(y[i], i))

a.sort(key = lambda arr : arr.value)
b.sort(key = lambda arr : arr.value)

i = 0
res = [0] * m
for x in b:
    while i < n:
        if a[i].value <= x.value:
            i += 1
        else:
            break
    res[x.id] = i

for x in res:
    print(x, end = " ")


