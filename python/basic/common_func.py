def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def binary(n):
    if n <= 1:
        return str(n)
    return binary(n // 2) + str(n % 2)


print(GCD(4, 8), GCD(9, 15), GCD(2, 9))
print(is_prime(2), is_prime(7), is_prime(9))
print(fibonacci(4))
print(count_digits(123456))
print(binary(10))
