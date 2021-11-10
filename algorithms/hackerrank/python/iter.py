from itertools import combinations
n = int(input())
a = input().split()
k = int(input())
combine = list(combinations(a, k))
contain_a = [x for x in combine if 'a' in x]
print(round(len(contain_a) / len(combine), 4))
