from collections import deque


n = int(input())
deq = deque()
for i in range(n):
    inp = input().split()
    if inp[0] == 'append':
        deq.append(inp[1])
    elif inp[0] == 'pop':
        deq.pop()
    elif inp[0] == 'popleft':
        deq.popleft()
    else:
        deq.appendleft(inp[1])


for item in deq:
    print(item, end=" ")