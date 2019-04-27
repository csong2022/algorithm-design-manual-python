from math import sqrt

PI = 3.1415926  # ratio of circumference to diameter
EPSILON = 0.000001  # a quantity small enough to be zero
DIMENSION = 2  # dimension of points
MAXPOLY = 200  # maximum number of points in a polygon

"""
Basic geometric primitives and data types -- Lines, Circles, Segments
"""


class Point:
    def __init__(self, x, y):
        self.x = x  # x-coordinat
        self.y = y  # y-coordinate

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)

    def print(self):
        print("%7.3lf %7.3lf" % (self.x, self.y))

    @staticmethod
    def print_points(p, n):
        for i in range(n):
            print(str(p[i]))

    def __str__(self):
        return "(%lf,%lf)" % (self.x, self.y)


class Line:
    def __init__(self, a, b, c):
        self.a = a  # x-coefficient
        self.b = b  # y-coefficient
        self.c = c  # constant term

    def print(self):
        print(str(self))

    def __str__(self):
        return "(a=%7.3lf,b=%7.3lf,c=%7.3lf)" % (self.a, self.b, self.c)


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1  # endpoints of line segment
        self.p2 = p2

    def print(self):
        print("segment: ", end='')
        self.p1.print()
        self.p2.print()


class Polygon:
    def __init__(self, p, n):
        self.p = p  # array of points in polygon
        self.n = n  # number of points in polygon

    def print(self):
        Point.print_points(self.p, self.n)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a  # point a
        self.b = b  # point b
        self.c = c  # point c


class Triangulation:
    def __init__(self, t, n):
        self.t = t  # indicies of vertices in triangulation
        self.n = n  # number of triangles in triangulation


class Circle:
    def __init__(self, c, r):
        self.c = c  # center of circle
        self.r = r  # radius of circle


def points_to_line(p1, p2):
    if p1.x == p2.x:
        a = 1
        b = 0
        c = -p1.x
    else:
        b = 1
        a = -(p1.y - p2.y) / (p1.x - p2.x)
        c = -(a * p1.x) - (b * p1.y)

    return Line(a, b, c)


def point_and_slope_to_line(p, m):
    a = -m
    b = 1
    c = -(a * p.x + b * p.y)
    return Line(a, b, c)


def parallelQ(l1, l2):
    return abs(l1.a - l2.a) <= EPSILON and abs(l1.b - l2.b) <= EPSILON


def same_lineQ(l1, l2):
    return parallelQ(l1, l2) and abs(l1.c - l2.c) <= EPSILON


def intersection_point(l1, l2):
    if same_lineQ(l1, l2):
        print("Warning: Identical lines, all points intersect.")
        return Point(0.0, 0.0)

    if parallelQ(l1, l2):
        print("Error: Distinct parallel lines do not intersect.")
        return None

    x = (l2.b * l1.c - l1.b * l2.c) / (l2.a * l1.b - l1.a * l2.b);

    if abs(l1.b) > EPSILON:  # test for vertical line
        y = - (l1.a * x + l1.c) / l1.b
    else:
        y = - (l2.a * x + l2.c) / l2.b

    return Point(x, y)


def closest_point(p_in, l):
    if abs(l.b) <= EPSILON:  # vertical line
        x = -l.c
        y = p_in.y

        return Point(x, y)

    if abs(l.a) <= EPSILON:  # horizontal line
        x = p_in.x
        y = -l.c
        return Point(x, y)

    perp = point_and_slope_to_line(p_in, 1 / l.a)  # non-degenerate line
    return intersection_point(l, perp)


def distance(a, b):
    d = (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)

    return sqrt(d)


def copy_point(a, b):
    b.x = a.x
    b.y = a.y


def swap_point(a, b):
    c = Point(0, 0)
    copy_point(a, c)
    copy_point(b, a)
    copy_point(c, b)


def points_to_segment(a, b):
    return Segment(a, b)


def segment_to_points(s):
    return s.p1, s.p2


def point_in_box(p, b1, b2):
    return min(b1.x, b2.x) <= p.x <= max(b1.x, b2.x) and \
           min(b1.y, b2.y) <= p.y <= max(b1.y, b2.y)


def segments_intersect(s1, s2):
    l1 = points_to_line(s1.p1, s1.p2)
    l2 = points_to_line(s2.p1, s2.p2)

    if same_lineQ(l1, l2):  # overlapping or disjoint segments
        return point_in_box(s1.p1, s2.p1, s2.p2) or \
               point_in_box(s1.p2, s2.p1, s2.p2) or \
               point_in_box(s2.p1, s1.p1, s1.p2) or \
               point_in_box(s2.p2, s1.p1, s1.p2)

    if parallelQ(l1, l2):
        return False

    p = intersection_point(l1, l2)

    return point_in_box(p, s1.p1, s1.p2) and point_in_box(p, s2.p1, s2.p2)


def signed_triangle_area(a, b, c):
    return (a.x * b.y - a.y * b.x + a.y * c.x - a.x * c.y + b.x * c.y - c.x * b.y) / 2.0


def triangle_area(a, b, c):
    return abs(signed_triangle_area(a, b, c))


def ccw(a, b, c):
    return signed_triangle_area(a, b, c) > EPSILON


def cw(a, b, c):
    return signed_triangle_area(a, b, c) < -EPSILON


def collinear(a, b, c):
    return abs(signed_triangle_area(a, b, c)) <= EPSILON


def read_point(input):
    line = input.readline()
    if not line:
        return None
    else:
        x, y = list(map(float, line.split()))
        return Point(x, y)


def read_points(input):
    n = int(input.readline()[:-1])  # number of points

    p = []
    for i in range(n):
        p.append(read_point(input))

    return p
