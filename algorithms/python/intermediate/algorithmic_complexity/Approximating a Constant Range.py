n = int(input())
a = list(map(int, input().split()))

cnt_num = [0] * (10 ** 5 + 1)
max_length = 0
distinct_num = 0
left = 0
for i in range(n):
    cnt_num[a[i]] += 1
    if cnt_num[a[i]] == 1:
        distinct_num += 1
    
    while left < i and distinct_num > 2:
        cnt_num[a[left]] -= 1
        if cnt_num[a[left]] == 0:
            distinct_num -= 1
        left += 1
        
    max_length = max(max_length, i - left + 1)
          
print(max_length)    
            
        