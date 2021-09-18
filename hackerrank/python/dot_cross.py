import numpy as np


n = int(input())
A = []
for _ in range(n):
    inp = list(map(int, input().split()))
    A.append(inp)

B = []
for _ in range(n):
    inp = list(map(int, input().split()))
    B.append(inp)

A = np.array(A)
B = np.array(B)
print(np.dot(A, B))
