while True:
    n = int(input())
    if n == 0:
        break
    a = [i for i in range(1, n + 1)]

    if n == 1:
        print('Discarded cards:')
    else:
        print('Discarded cards: ', end='')
        while len(a) > 2:
            print(a[0], end=', ')
            a = a[2:] + [a[1]]
        print(a[0])
        a = a[1:]
    print('Remaining card:', a[0])
