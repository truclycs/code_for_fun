def smaller(a, l, r, x):
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] < x:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res

def bigger(a, l, r, x):
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] > x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

n = int(input())
a = list(map(int, input().split()))
q = int(input())
h = list(map(int, input().split()))
for i in range(q):
    x = smaller(a, 0, n - 1, h[i])
    y = bigger(a, 0, n - 1, h[i])
    if x == -1:
        print('X', end = " ")
    else: 
        print(a[x], end = " ")
    if y == -1:
        print('X')
    else: 
        print(a[y])