n = int(input())
min_left = 10 ** 9
max_right = 0
a = []
for _ in range(n):
    l, r = map(int, input().split())
    a.append((l, r))
    min_left = min(min_left, l)
    max_right = max(max_right, r)


res = -1
for i, x in enumerate(a):
    if x[0] == min_left and x[1] == max_right:
        res = i + 1

print(res)