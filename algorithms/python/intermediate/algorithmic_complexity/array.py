n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = -1
cnt_num = [0] * (10 ** 5 + 1)
cnt_distint_num = 0
for i in range(n):
    if cnt_num[a[i]] == 0:
        cnt_distint_num += 1
        if cnt_distint_num == k:
            r = i
            break
    cnt_num[a[i]] += 1

if cnt_distint_num != k:
    print(-1, -1)
else:    
    while cnt_num[a[l]] > 1:
        cnt_num[a[l]] -= 1
        l += 1    
    print(l + 1, r + 1)