n = int(input())
t = list(map(int, input().split()))
t = [0] + t

num_of_minutes = 0
for i in range(1, len(t)):
    if t[i] - t[i - 1] <= 15:
        num_of_minutes = t[i]
    else:
        break

print(min(num_of_minutes + 15, 90))
