from sys import stdin
 
l = [int(x) for x in stdin.read().split()]

n = l[0]
pro = set() 
for x in l[1: n + 1]:
    pro.add(x)

res = 0
for x in l[n + 2:]:
    if x in pro:
        res += 1

print(res)

