def binarySearch(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False
t = int(input())
while t:
    t -= 1
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    a.sort()
    for i in range(n):
        if binarySearch(a, i + 1, n - 1, m - a[i]):
            res += 1
    print(res)

