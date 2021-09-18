import numpy as np


P = list(map(float, input().split()))
x = float(input())
print(np.polyval(P, x))
