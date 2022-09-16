n = int(input())
a = [None] * n
b = [None] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

for i in range(n):
    if i < n // 2 or a[i] < b[n - i - 1]:
        print(1, end = "")
    else:
        print(0, end = "")

print()

for i in range(n):
    if i < n // 2 or b[i] < a[n - i - 1]:
        print(1, end = "")
    else:
        print(0, end = "")