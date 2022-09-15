T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    s = set()
    for x in a[:N]:
        s.add(x)
    for x in a[N:M + N]:
        if x in s:
            print("YES")
        else:
            print("NO")
            s.add(x)


