from itertools import combinations


inp = input().split()
string = list(inp[0])
num = int(inp[1])

res = []
string.sort()
for i in range(1, num + 1):
    com = list(combinations(string, i))
    tmp = []
    for x in com:
        tmp.append("".join(x).upper())
    res += tmp

for x in res:
    print(x)
