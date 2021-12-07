n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
for problem in b:
    if cnt < n and a[cnt] <= problem:
        cnt += 1

print(n - cnt)