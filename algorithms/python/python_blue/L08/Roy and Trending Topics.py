import queue
pq = queue.PriorityQueue()
class Topic:
    def __init__(self, ID, new_score, change):
        self.ID = ID
        self.new_score = new_score
        self.change = change
    def __lt__(self, other):
        return self.change > other.change or (self.change == other.change and self.ID > other.ID)
        
n = int(input())
for i in range(n):
    ID, Z, P, L, C, S = map(int, input().split())
    new_score =  P * 50 + L * 5 + C *10 + S * 20 
    change = new_score - Z
    pq.put(Topic(ID, new_score, change))
    
for i in range(5):
    print(pq.queue[0].ID, pq.queue[0].new_score)
    pq.get()

    