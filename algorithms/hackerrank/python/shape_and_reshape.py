import numpy as np


a = list(map(int, input().split()))
a = np.array(a)
print(a.reshape(3, 3))