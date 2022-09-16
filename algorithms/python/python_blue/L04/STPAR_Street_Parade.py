while (True):
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    x = 1
    j = -1
    stack = []
    for i in s:
        if i != x:
            if (j == -1):
                stack.append(i)
            else:
                j += 1
                stack[j] = i
        else:
            x += 1
            while len(stack) + j >= 0:
                if stack[j] == x:
                    x += 1
                    j -= 1 
                else:
                    break
    if (x == n + 1):
        print("yes")
    else:
        print("no")
           