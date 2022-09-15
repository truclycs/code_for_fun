k, n, w = map(int, input().split())

dollars = 0
for i in range(w + 1):
    dollars += i * k

if dollars <= n:
    print(0)
else:
    print(dollars - n)
