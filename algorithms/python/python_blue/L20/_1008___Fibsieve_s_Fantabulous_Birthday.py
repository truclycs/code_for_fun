Case = 0
T = int(input())
while T:
    T -= 1
    s = int(input())
    t = int(s ** 0.5)
    if t % 2 == 0:
        if t ** 2 < s:
            x = s - t ** 2
            y = t + 1
            if x > t + 1:
                x = t + 1
                y = (t + 1) ** 2 - s + 1
        else:
            x = 1
            y = t
    else:
        if t ** 2 < s:
            x = t + 1
            y = s - t ** 2
            if y > t + 1:
                x = (t + 1) ** 2 - s + 1
                y = t + 1
        else:
            x = t
            y = 1

    Case += 1
    print("Case " + str(Case) + ": " + str(y) + " " + str(x))
