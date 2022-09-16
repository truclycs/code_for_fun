n = int(input())
a = list(map(int, input().split()))

l = S = D = 0
r = n - 1
while (l <= r):
    if (a[l] > a[r]):
        S += a[l]
        l += 1
    else:
        S += a[r]
        r -= 1
    if (l > r):
        break
    if (a[l] > a[r]):
        D += a[l]
        l += 1
    else:
        D += a[r]
        r -= 1

print(S, D)