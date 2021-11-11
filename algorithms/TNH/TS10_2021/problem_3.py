s = input()


def is_palin(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


n = len(s)
result = ''
for i in range(n):
    for j in range(n - i):
        sub_s = s[j: j + i + 1]
        if is_palin(sub_s):
            result = sub_s

print(result)
