k = int(input())
a = list(map(int, input().split()))

a.sort(key=lambda x: -x)

num_of_months = 0
height = 0

for h in a:
    if height >= k:
        break 
    height += h
    num_of_months += 1

if height < k:
    print(-1)
else:
    print(num_of_months)