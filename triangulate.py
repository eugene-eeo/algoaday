from collections import namedtuple
from math import atan2, pi


Point = namedtuple('Point', 'x,y')


def is_convex(p, q, r):
    d_in  = Point(q.x - p.x, q.y - p.y)  # p -> q
    d_out = Point(r.x - q.x, r.y - q.y)  # q -> r
    angle = pi + atan2( d_in.x*d_out.y - d_out.x*d_in.y, d_in.x*d_out.x + d_in.y*d_out.y )
    return angle < pi


def triplet(points, i):
    n = len(points)
    x1 = points[i]
    x2 = points[(i + 1) % n]
    x3 = points[(i + 2) % n]
    return x1, x2, x3


def triangulate(points):
    # points is given as a clockwise sequence of vertices
    points = points[:]
    T = []
    n = len(points)
    i = 0
    while n > 3:
        i %= n
        p, q, r = triplet(points, i)
        if is_convex(p, q, r):
            T.append([p, q, r])
            # remove q
            del points[(i + 1) % n]
            n -= 1
            continue
        i += 1
    T.append(points)
    return T
