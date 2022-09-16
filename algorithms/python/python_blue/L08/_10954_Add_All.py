import queue

while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    pq = queue.PriorityQueue()
    for x in a:
        pq.put(x)
    res = 0
    while True:
        a = pq.queue[0]
        pq.get()
        b = pq.queue[0]
        pq.get()
        pq.put(a + b)
        if len(pq.queue) == 1:
            res += pq.queue[0]
            break
        res += a + b
    print(res)

