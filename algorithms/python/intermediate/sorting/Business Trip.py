n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
num_months = 0
cen = 0
for x in a:
    if cen < n:
        cen += x
        num_months += 1
    else:
        break
print(-1) if cen < n else print(num_months)