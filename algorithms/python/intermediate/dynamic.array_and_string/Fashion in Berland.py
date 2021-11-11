def is_right_way(n, a):
    if n == 1:
        return False if a[0] == 0 else True

    not_fastened = 0
    for x in a:
        if x == 0:
            not_fastened += 1

    return not_fastened == 1


n = int(input())
a = list(map(int, input().split()))
print('YES') if is_right_way(n, a) else print('NO')