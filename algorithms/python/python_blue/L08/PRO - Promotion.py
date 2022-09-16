import heapq
pq = []
max_pq = []

got_max =  [0] * 1000001
got_min =  [0] * 1000001
res = 0
n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    for x in a[1:]:
        heapq.heappush(pq, x)
        heapq.heappush(max_pq, -x)

    while got_max[-max_pq[0]] != 0:
        got_max[-max_pq[0]] -= 1
        heapq.heappop(max_pq)
    while got_min[pq[0]] != 0:
        got_min[pq[0]] -= 1
        heapq.heappop(pq)

    res += max_pq[0] + pq[0]
    got_max[-max_pq[0]] += 1
    got_max[pq[0]] += 1
    got_min[-max_pq[0]] += 1
    got_min[pq[0]] += 1  

print(-res)
    
