INF = 10 ** 9

def FloydWarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

T = int(input())
while T:
    T -= 1
    s = input()
    n = len(s)
    dist = [[INF] * n for i in range(n)]
    matrix = []
    for i in range(n):
        if i == 0:
            matrix.append(s)
        else:
            matrix.append(input())
        for j in range(n):
            if matrix[i][j] == 'Y':
                dist[i][j] = 1
            elif i == j:
                dist[i][j] = 0
    
    FloydWarshall()
    friends =0
    id = 0

    for i in range(n):
        count = 0        
        for j in range(n):
            if dist[i][j] == 2:
                count += 1        
        if count > friends:
            friends = count
            id = i
    
    print(id, friends)