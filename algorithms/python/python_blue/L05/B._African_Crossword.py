n, m = map(int, input().split())

s = []
for i in range(n):
    tmp = input()
    s.append(tmp)

res = ""
for i in range(n):
    for j in range(m):
        c = s[i][j]
        flag = True
        for x in range(n):
            if s[x][j] == c and x != i:
                flag = False
                break
        if not flag:
            continue
        for y in range(m):
            if s[i][y] == c and y != j:
                flag = False
                break
        if flag:
            res += c
        
print(res)