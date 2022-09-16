n, h = map(int, input().split())
a = list(map(int, input().split()))

res = 0 
for i in a:
    if (i <= h):
        res += 1
    else:
        res += 2

print(res)