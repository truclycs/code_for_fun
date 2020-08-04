while True:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))

    number = 1
    side_street = []
    for c in a:
        if c != number:
            while side_street and number == side_street[-1]:
                side_street = side_street[:-1]
                number += 1
            side_street.append(c)
        else:
            number += 1

    while side_street and number == side_street[-1]:
        side_street = side_street[:-1]
        number += 1

    if number == n + 1:
        print("yes")
    else:
        print("no")
