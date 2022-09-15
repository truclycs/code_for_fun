n = int(input())
t = list(map(int, input().split()))

l = 0
r = n - 1
sum_a = sum_b = 0
while l <= r:
    if sum_a <= sum_b:
        sum_a += t[l]
        l += 1
    else:
        sum_b += t[r]
        r -= 1

print(l, n - l)


