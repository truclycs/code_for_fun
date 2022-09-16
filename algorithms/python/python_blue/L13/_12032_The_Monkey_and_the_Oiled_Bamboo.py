def check(a, n, k):
    for i in range(1, n):
        if a[i] - a[i - 1] > k:
            return False
        elif a[i] - a[i - 1] == k:
            k -= 1
    return True

def binarySearch(a, l, r, n):
    res = 0
    while (l <= r):
        mid = (l + r) // 2
        if check(a, n, mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

Case = 1
T = int(input())
while T:
    T -= 1
    n = int(input())
    a = list(map(int, input().split()))
    print("Case", Case, ":", binarySearch(a, 1, a[n - 1] + 1, n - 1))
    Case += 1