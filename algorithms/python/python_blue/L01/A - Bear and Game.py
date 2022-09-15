n = int(input())
a = list(map(int, input().split()))

res = 15
for i in a:
    if (i <= res):
        res = i + 15
    else:
        break
if (res > 90):
    res =  90
print(res)