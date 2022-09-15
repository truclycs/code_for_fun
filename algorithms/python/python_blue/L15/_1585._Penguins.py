n = int(input())
penguin = dict()
for _ in range(n):
    name = input()
    if name in penguin:
        penguin[name] += 1
    else:
        penguin[name] = 1

cnt = 0
for key in penguin.keys():
    if penguin[key] > cnt:
        res = key
        cnt = penguin[key]

print(res)

