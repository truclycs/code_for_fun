def process(a, n):
    wait = []
    num = 1
    for x in a:
        if x != num:
            while wait and wait[-1] == num:
                num += 1
                wait = wait[:-1]
            wait.append(x)
        else:
            num += 1
    while wait and wait[-1] == num:
        num += 1
        wait = wait[:-1]
    return "no" if wait else "yes"


while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    print(process(a, n))
