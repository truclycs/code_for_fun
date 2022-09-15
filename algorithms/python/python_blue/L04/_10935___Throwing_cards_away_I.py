import queue
q = queue.Queue()
while True:
    n = int(input())
    for i in range(n):
        q.put(i + 1)
    if n == 0:
        break
    if n > 1:
        print("Discarded cards: ", end = "")
        while q.qsize() > 2:
            print(q.queue[0], end = ", ")
            q.get()
            x = q.queue[0]
            q.get()
            q.put(x)
        print(q.queue[0])
        q.get()
        print("Remaining card:", q.queue[0])
        q.get()
    else:
        print("Discarded cards:")
        print("Remaining card:", q.queue[0])
        q.get()
   
