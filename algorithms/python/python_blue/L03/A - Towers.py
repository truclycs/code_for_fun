n = int(input())
a = list(map(int, input().split()))
a.sort()
highest = total = cnt = 1
for i in range(1, n):
    if (a[i] == a[i - 1]):
        cnt += 1
    else:
        total += 1
        highest = max(highest, cnt)
        cnt = 1

print(max(highest, cnt), total)