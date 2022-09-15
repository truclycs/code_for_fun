import queue

class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value

n = int(input())
a = list(map(int, input().split()))
pq = queue.PriorityQueue()

for i in range(len(a)):
    pq.put(PQEntry(a[i]))
    if (i < 2):
        print(-1)
    else:
        x = pq.queue[0].value
        pq.get()
        y = pq.queue[0].value
        pq.get()
        z = pq.queue[0].value
        pq.get()
        print(x * y * z)
        pq.put(PQEntry(x))
        pq.put(PQEntry(y))
        pq.put(PQEntry(z))
