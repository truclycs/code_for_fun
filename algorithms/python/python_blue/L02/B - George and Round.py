n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
j = m - 1
for i in range(n - 1, -1, -1):
    if (j >= 0):
        if (b[j] >= a[i]):
            count += 1
            j -= 1
    else:
        break

print(n - count)