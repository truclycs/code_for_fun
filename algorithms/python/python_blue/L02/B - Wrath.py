n = int(input())
l = list(map(int, input().split()))

i = n - 1
j = n - 2
killed = 0
while (i > 0 and j >= 0):
    if (i != j):
        if (j >= i - l[i]):
            j -= 1
            killed += 1
        else:
            i -= 1
    else:
        j -= 1

print(n - killed)