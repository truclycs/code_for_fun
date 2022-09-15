T = int(input())
while T:
    T -= 1
    N, X = map(int, input().split())
    a = list(map(int, input().split()))
    s = set()
    for x in a:
        s.add(x)

    if (len(s) == X):
        print("Good")
    elif (len(s) < X):
        print("Bad")
    else:
        print("Average")

