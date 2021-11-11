import numpy as np


n, m = map(int, input().split())

a = []
for _ in range(n):
    r = list(map(int, input().split()))
    a.append(r)

a = np.array(a)
print(np.mean(a, axis=1))
print(np.var(a, axis=0))
print(round(np.std(a, axis=None), 11))