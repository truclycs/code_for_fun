point = [list(map(int, input().split())) for _ in range(8)]

point.sort()

respectable = True

if point[3][0] != point[4][0] or point[3][1] != point[0][1] or point[4][1] != point[2][1]:
    respectable = False

for i in range(2):
    if point[i][0] != point[i + 1][0] or point[i + 5][0] != point[i + 6][0]:
        respectable = False

for i in range(3):
    if point[i][1] != point[i + 5][1]:
        respectable = False

print('respectable') if respectable else print('ugly')
