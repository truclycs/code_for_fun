import numpy as np

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = np.array(A)
B = np.array(B)
print(np.inner(A, B))
print(np.outer(A, B))