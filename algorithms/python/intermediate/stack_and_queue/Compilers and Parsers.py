T = int(input())
for _ in range(T):
    exp = input()
    max_len = 0
    open = 0
    for i, e in enumerate(exp):
        if e == '<':
            open += 1
        else:
            open -= 1
            if open == 0:
                max_len = i + 1
            elif open < 0:
                break
    print(max_len)
