n = int(input())
height = list(map(int, input().split()))

height.sort()

largest_height = 1
total_towers = 1
h = 1

for i in range(1, n):
    if height[i] == height[i - 1]:
        h += 1
    else:
        total_towers += 1
        largest_height = max(largest_height, h)
        h = 1

print(max(largest_height, h), total_towers)