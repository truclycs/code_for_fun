import numpy as np


n, m, p = map(int, input().split())
# a = []
# for _ in range(n + m):
#     r = list(map(int, input().split()))
#     a.append(r)

# a = np.array(a)
# print(a)

a = np.array([list(map(int, input().split())) for _ in range(n)])
b = np.array([list(map(int, input().split())) for _ in range(m)])
print(np.concatenate((a, b), axis=0))
