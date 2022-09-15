n = int(input())
prices = list(map(int, input().split()))
s = set()
res = 10**16
for x in prices:
    s_tmp = set()
    while (len(s) > 0 and list(sorted(s))[0] - x < 0):
        tmp = list(sorted(s))[0]
        s_tmp.add(tmp)
        s.remove(tmp)
    if (len(s) > 0):
        res = min(res, list(sorted(s))[0] - x)
    while (len(s_tmp) > 0):
        s.add(list(s_tmp)[0])
        s_tmp.remove(list(s_tmp)[0])
    s.add(x)

print(res)


