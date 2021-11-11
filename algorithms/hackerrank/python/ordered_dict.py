from collections import OrderedDict


n = int(input())

items = OrderedDict()
for i in range(n):
    inp = input().split(' ')
    item = " ".join(inp[:-1])
    quan = int(inp[-1])
    items[item] = items.get(item, 0) + quan


for item in items:
    print(item, items[item])
