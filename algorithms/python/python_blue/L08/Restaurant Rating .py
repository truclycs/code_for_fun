import heapq
pq = [] # queue.PriorityQueue()
max_pq = [] # queue.PriorityQueue()

n = int(input())
for i in range(n):
    x = input().split()
    type = int(x[0])
    if type == 1:
        heapq.heappush(max_pq, -int(x[1]))# max_pq.put(-int(x[1]))
    else:
        size = (len(pq) + len(max_pq)) // 3
        if size == 0:
            print("No reviews yet")
        else:
            while len(pq) < size:
                heapq.heappush(pq, -heapq.heappop(max_pq))
            while pq[0] < -max_pq[0]:
                heapq.heappush(pq, -heapq.heappop(max_pq))
                heapq.heappush(max_pq, -heapq.heappop(pq))
            print(pq[0])
