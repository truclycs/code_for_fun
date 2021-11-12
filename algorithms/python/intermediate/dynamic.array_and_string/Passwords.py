n, k = map(int, input().split())
failed_passwords = [input() for _ in range(n)]
password = input()

less_len = 0
equal_len = 0
for p in failed_passwords:
    if len(p) < len(password):
        less_len += 1
    elif len(p) == len(password):
        equal_len += 1

best = less_len + (less_len // k) * 5 + 1
worst = less_len + equal_len + ((less_len + equal_len - 1) // k) * 5

print(best, worst)