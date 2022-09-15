import queue 

while True:
    try:
        n = int(input())
    except EOFError:
        break
    pq = queue.PriorityQueue()
    s  = []
    q = queue.Queue()
    is_pq = is_queue = is_stack = True
    for i in range(n):
        type, value = map(int, input().split())
        if type == 1:
            pq.put(-value)
            s.append(value)
            q.put(value)
        else:
            if len(s) == 0:
                is_pq = is_queue = is_stack = False
                continue
            if pq.get() != -value:
                is_pq = False
            if q.get() != value:
                is_queue = False
            if s.pop() != value:
                is_stack = False

    if is_pq + is_queue + is_stack > 1:
        print("not sure")
    elif is_queue:
        print("queue")
    elif is_stack:
        print("stack")
    elif is_pq:
        print("priority queue")
    else:
        print("impossible")    