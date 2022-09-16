def binarySearch():
    l = 0.0
    r = 1000.0
    while l + 1e-6 < r :
        mid = (l + r) / 2
        t = 0
        for i in range(n):
            if a[i] > mid:
                t += (a[i] - mid) * (1 - k / 100)
            else:
                t += a[i] - mid
        if t >= 0:
            l = mid
        else:
            r = mid
    return l

n, k = map(int, input().split())
a = list(map(int, input().split()))
print("{:.9f}".format(binarySearch()))