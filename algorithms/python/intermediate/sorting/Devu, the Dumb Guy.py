n, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
total_time = 0
for sub in a:
    total_time += sub * x
    x = max(x - 1, 1)

print(total_time)