n, m = map(int, input().split())
l = [] 
first = []
second = []
for i in range(m):
    a, b = input().split()
    first.append(a)
    second.append(b)

s = input().split()

res = ""
for str in s:
    for i in range(m):
        if str == first[i]:
            if len(first[i]) > len(second[i]):
                res += second[i] + " "
            else:
                res += first[i] + " "
            break
print(res)



