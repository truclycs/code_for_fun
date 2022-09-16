import sys
class Scanner:
    def __init__(self, istream):
        self.tokenizer = Scanner.__tokenizer__(istream)
    def __tokenizer__(istream):
        for line in istream:
                for token in line.strip().split():
                        yield token
    def next(self):
        return self.tokenizer.__next__()

def binarySearch(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False

sc = Scanner(sys.stdin)
n = int(sc.next())
k = int(sc.next())
a = []
for i in range(n):
    x = int(sc.next())
    a.append(x)

a.sort()
res = 0
for i in range(n):
    if binarySearch(a, i + 1, n - 1, a[i] + k):
        res += 1
print(res)