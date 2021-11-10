cube = lambda x: x ** 3


def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    f = [0] * n
    f[0] = 0
    f[1] = 1
    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]
    return f


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
