n = int(input())
a = list(map(int, input().split()))

Alice = 0
Bob = 0
l = 0
r = n - 1
while l <= r:
    if Alice <= Bob:
        Alice += a[l]
        l += 1
    elif Alice > Bob:
        Bob += a[r]
        r -= 1
        
print(l, n - l)