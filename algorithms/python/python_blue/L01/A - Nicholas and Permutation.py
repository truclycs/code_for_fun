n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if (a[i] == n):
        pos_max = i
    if (a[i] == 1):
        pos_min = i

if (pos_max < pos_min):
    if (pos_max > n - 1 - pos_min):
        pos_max = 0
    else:
        pos_min = n - 1
else:
    if (pos_min > n - 1 - pos_max):
        pos_min = 0
    else:
        pos_max = n - 1

print(abs(pos_max - pos_min))