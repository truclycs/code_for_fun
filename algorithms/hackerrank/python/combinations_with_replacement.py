from itertools import combinations_with_replacement


inp = input().split()
string = list(inp[0])
num = int(inp[1])


string.sort()
res = combinations_with_replacement(string, num)

for x in res:
    print("".join(x).upper())
