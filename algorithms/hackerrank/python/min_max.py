import numpy as np


n, m = map(int, input().split())

a = []
for _ in range(n):
    r = list(map(int, input().split()))
    a.append(r)

a = np.array(a)
print(np.max(np.min(a, axis=1)))