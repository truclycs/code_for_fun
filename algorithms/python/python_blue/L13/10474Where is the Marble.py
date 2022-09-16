def bsFirst(a, left, right, x): 
    while left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

Case = 0
while True:
    N, Q = map(int, input().split(' '))
    if N == Q == 0:
        break
    
    a = []
    for i in range(N):
        x = int(input())
        a.append(x)
    a.sort()

    Case += 1
    print("CASE# " + str(Case) + ":")

    for i in range(Q):
        q = int(input())
        if bsFirst(a, 0, N - 1, q) != -1:
            print(q, "found at", bsFirst(a, 0, N - 1, q) + 1)
        else:
            print(q, "not found")

