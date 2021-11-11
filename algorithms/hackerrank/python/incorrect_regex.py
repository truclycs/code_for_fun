import re


def is_valid_regex(regex):
    try:
        re.compile(regex)
    except:
        return False
    return True


T = int(input())
for _ in range(T):
    regex = input()
    print(is_valid_regex(regex=regex))
