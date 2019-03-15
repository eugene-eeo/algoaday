from collections import namedtuple
from math import atan2, pi


Point = namedtuple('Point', 'x,y')


def sign(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    return 1


def det(p, q, r):
    return (q.x*r.y - q.y*r.x) - (p.x*r.y - p.y*r.x) + (p.x*q.y - p.y*q.x)


def side(p, q, r):
    return sign(det(p, q, r))


def is_convex(p, q, r):
    d_in  = Point(q.x - p.x, q.y - p.y)  # p -> q
    d_out = Point(r.x - q.x, r.y - q.y)  # q -> r
    # angle = pi + atan2(...) < pi
    #           => atan2(...) < 0
    return atan2(d_in.x*d_out.y - d_out.x*d_in.y, d_in.x*d_out.x + d_in.y*d_out.y) < 0


def triangulate(points):
    # points is given as a clockwise sequence of vertices
    points = points[:]
    T = []
    n = len(points)
    i = 0
    while n > 3:
        i %= n
        j = (i + 1) % n
        k = (i + 2) % n
        p = points[i]
        q = points[j]
        r = points[k]
        if is_convex(p, q, r):
            x = side(p, r, q)
            # check if this is a convex subsection, i.e. triangle
            # pqr does not intersect with any other points
            ok = all(side(p, r, p2) != x for idx, p2 in enumerate(points)
                     if idx not in (i, j, k))
            if ok:
                T.append([p, q, r])
                # remove q
                del points[j]
                n -= 1
                continue
        i += 1
    T.append(points)
    return T
