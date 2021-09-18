import numpy as np


N = int(input())
A = []
for _ in range(N):
    row = list(map(float, input().split()))
    A.append(row)

A = np.array(A)
print(round(np.linalg.det(A), 2))
