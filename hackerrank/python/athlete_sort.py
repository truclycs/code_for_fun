n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

a.sort(key=lambda x: x[k])

for x in a:
    print(*x)
