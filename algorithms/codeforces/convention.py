# https://onlinejudge.org/external/102/10245.pdf

import sys
sys.setrecursionlimit(10000)
INF = 1e9
 
 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
 
def distance(p1, p2):
    """Get the distance between 2 points"""
    x = p1.x - p2.x
    y = p1.y - p2.y
    return (x*x + y*y) ** 0.5
 
 
def bruteForce(point_set, left, right):
    """Calculate the shortest distance between 2 points from a set of points"""
    min_dist = INF
    for i in range(left, right):
        for j in range(i + 1, right):
            min_dist = min(min_dist, distance(point_set[i], point_set[j]))
    return min_dist
 
 
def stripClosest(point_set, left, right, mid, dist_min):
    """Get the smallest distance"""
    point_mid = point_set[mid]
    splitted_points = []
    for i in range(left, right):
        if abs(point_set[i].x - point_mid.x) <= dist_min:
            splitted_points.append(point_set[i])

    #Avoid comparing multiple points, 
    #arrange the points according to degrees Oy
    splitted_points.sort(key=lambda p: p.y)
 
    smallest = INF
    l = len(splitted_points)
    for i in range(0, l):
        for j in range(i + 1, l):
            if splitted_points[j].y - splitted_points[i].y >= dist_min:
                break
            d = distance(splitted_points[i], splitted_points[j])
            smallest = min(smallest, d)

    return smallest
 
 
def closestUtil(point_set, left, right):
    """Divide the array into 2 parts (left and right).
    Find the shortest distance on each side. 
    Compare and choose a shorter distance.
    """
    if right - left <= 3:
        return bruteForce(point_set, left, right)

    mid = (right + left) // 2
    dist_left = closestUtil(point_set, left, mid)
    dist_right = closestUtil(point_set, mid + 1, right)
    dist_min = min(dist_left, dist_right)
    
    return min(dist_min, stripClosest(point_set, left, right, mid, dist_min))
 
 
if __name__ == '__main__':
    while True:
        n = int(input())        

        if n == 0:
            break

        point_set = []
        for i in range(n):
            x, y = map(float, input().split())
            point_set.append(Point(x, y))
 
        #Arrange point coordinates in ascending order of Ox coordinates
        point_set.sort(key=lambda p: p.x)
 
        res = closestUtil(point_set, 0, n)

        #If dist_min > 10000 then print INFINITY, else print dist_min
        if res < 10000:
            print('%.4f' % res)
        else:
            print("INFINITY")