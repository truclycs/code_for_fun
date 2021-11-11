import math


AB = int(input())
BC = int(input())

print(str(round(180 * math.acos(BC / (AB ** 2 + BC ** 2) ** 0.5) / math.pi)) + '\N{DEGREE SIGN}')
