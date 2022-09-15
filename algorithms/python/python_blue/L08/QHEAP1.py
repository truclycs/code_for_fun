import queue
pq = queue.PriorityQueue()
dele = queue.PriorityQueue()

Q = int(input())
for i in range(Q):
    x = input().split()
    types = int(x[0])
    if types == 1:
        pq.put(int(x[1]))
    elif types == 2:
        dele.put(int(x[1]))
    else:
        while len(dele.queue) != 0 and dele.queue[0] == pq.queue[0]:
            dele.get()
            pq.get()
        print(pq.queue[0])

