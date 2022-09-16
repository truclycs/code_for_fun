max = 100000001

def getSum(x):
    sum = 0
    for i in range(n):
        if h[i] >= x:
            sum += h[i] - x
    return sum

def binarySearch():
    res = 0
    l = 0
    r = max
    while l <= r:
        mid = (l + r) // 2
        if (m > getSum(mid)):
            r = mid - 1
        else:
            l = mid + 1 
            res = mid
    return res

n, m = map(int, input().split())
h = list(map(int, input().split()))
print(binarySearch())
