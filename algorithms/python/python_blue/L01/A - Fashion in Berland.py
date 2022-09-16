n = int(input())
a = []
a = list(map(int, input().split()))

cnt = 0
for i in a:
    if (i == 0):
        cnt += 1

if ((n == 1 and cnt == 0) or (n > 1 and cnt == 1)):
    print("YES")
else:
    print("NO")