n = int(input())

# if array on 1 line
# a = list(map(int, input().split()))

# if each element of array on 1 line
a = []
for i in range(n):
    x = int(input())
    a.append(x)

result = 0
for i in range(n):
    if a[i] % 2 == 0 and a[i] % 5 == 0 and a[i] > result:
        result = a[i]

print(result)
