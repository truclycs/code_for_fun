class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        return (self.x < other.x) or (self.x == other.x and self.y <= other.y)
p = []
for i in range(8):
    a, b = map(int, input().split())
    p.append(Point(a, b))

p.sort()

ugly = False
for i in range(1, 3):
    if p[i].x != p[i - 1].x or p[i + 5].x != p[i + 4].x or p[i].y != p[i + 5].y or p[i].y == p[i - 1].y or p[i + 5].y == p[i + 4].y:
        ugly = True
if p[3].x != p[4].x or p[3].y == p[4].y or p[0].y != p[3].y or p[7].y != p[4].y:
		ugly = True

if ugly:
    print("ugly")
else:
    print("respectable")

