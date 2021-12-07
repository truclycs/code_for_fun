case = 0
while True:
    p, c = map(int, input().split())
    if p == c == 0:
        break
    case += 1
    queue = [i for i in range(1, min(p, c) + 1)]
    print(f'Case {case}:')
    for _ in range(c):
        inp = input()
        if inp[0] == 'N':
            print(queue[0])
            queue = queue[1:] + [queue[0]]
        else:
            e = int(inp.split()[1])
            if e in queue:
                idx = queue.index(e)
                queue = [e] + queue[0:idx] + queue[idx + 1:]
            else:
                queue = [e] + queue