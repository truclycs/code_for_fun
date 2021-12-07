n = int(input())
a = list(map(int, input().split()))

a.sort()

max_height = 1
total_towers = 1
height = 1
for i in range(n - 1):
    if a[i] == a[i + 1]:
        height += 1
        max_height = max(max_height, height)
    else:
        total_towers += 1
        height = 1

print(max_height, total_towers)
