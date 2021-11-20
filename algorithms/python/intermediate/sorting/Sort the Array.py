n = int(input())
a = list(map(int, input().split()))
b = a.copy()

a.sort()

left = 0
right = 0
for i in range(n):
    if a[i] != b[i]:
        left = i
        break

for i in range(n - 1, -1, -1):
    if a[i] != b[i]:
        right = i
        break

i = left
j = right
while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1

if a == b:
    print("yes")
    print(left + 1, right + 1)
else:
    print('no')
