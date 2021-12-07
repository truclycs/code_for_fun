n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = i - a[i]
    
cur = n - 1
alive = 1
for i in range(n - 1, -1, -1):
    if i < cur:
        alive += 1
    cur = min(cur, a[i])

print(alive)