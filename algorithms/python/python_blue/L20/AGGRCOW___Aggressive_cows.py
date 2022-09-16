def isPossible(mid):
    i = 0
    j = 1
    cnt = 1
    while j < n:
        t = x[j] - x[i] 
        if t >= mid:
            i = j
            cnt += 1
        j += 1
    return cnt >= c

def binarySearch(l, r):
    while l <= r:
        mid = (l + r) // 2
        if isPossible(mid):
            l = mid + 1
        else:
            r = mid - 1

    if not isPossible(l):
        return l - 1
    return r


t = int(input())
while t:
    t -= 1
    n, c = map(int, input().split())
    x = []
    for i in range(n):
        q = int(input())
        x.append(q)

    x.sort()
    print(binarySearch(1, x[n - 1] - x[0]))
