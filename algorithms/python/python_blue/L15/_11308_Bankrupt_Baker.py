t = int(input())
for _ in range(t):
    title = input()
    m, n, b = map(int, input().split())
    ingredients = dict()
    for i in range(m):
        line = input().split()
        ingredients[line[0]] = (int)(line[1])

    res = []
    for i in range(n):
        name = input()
        k = int(input())
        sum = 0
        for j in range(k):
            line = input().split()
            sum += ingredients[line[0]] * (int)(line[1])
        if sum <= b:
            res.append((sum, name))
    
    name = ""
    for c in title:
        name += c.upper()
    print(name)
    if len(res) == 0:
        print("Too expensive!")
    else:
        res.sort()
        for x in res:
            print(x[1])
        
    print()
