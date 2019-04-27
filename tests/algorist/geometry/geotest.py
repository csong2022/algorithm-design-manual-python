from unittest import TestCase

from algorist.geometry.geometry import Point, points_to_line, point_and_slope_to_line, parallelQ, intersection_point, \
    closest_point, read_point
from tests.algorist.test.test_engine import execute


class GeoTest(TestCase):

    def process(self, input):
        while True:
            p1 = read_point(input)
            if p1 is None:
                break
            p2 = read_point(input)
            q1 = read_point(input)
            q2 = read_point(input)

            p1.print()
            p2.print()
            q1.print()
            q2.print()

            l1 = points_to_line(p1, p2)
            l2 = points_to_line(q1, q2)

            l1.print()
            l2.print()

            print("slope and line tests")
            l3 = point_and_slope_to_line(p1, -l1.a)
            l3.print()

            l3 = point_and_slope_to_line(p2, -l1.a)
            l3.print()

            l3 = point_and_slope_to_line(q1, -l2.a)
            l3.print()

            l3 = point_and_slope_to_line(q2, -l2.a)
            l3.print()

            print("parallel lines test")
            print("%d" % (1 if parallelQ(l1, l2) else 0))

            print("intersection point")

            tmp = intersection_point(l1, l2)
            if tmp is not None:
                i = tmp
            i.print()

            print("closest point")
            i = closest_point(p1, l1)
            i.print()
            i = closest_point(p2, l1)
            i.print()
            i = closest_point(q1, l1)
            i.print()
            i = closest_point(q2, l1)
            i.print()

            i = closest_point(p1, l2)
            i.print()
            i = closest_point(p2, l2)
            i.print()
            i = closest_point(q1, l2)
            i.print()
            i = closest_point(q2, l2)
            i.print()

            print("--------------------------------")

    def test(self):
        execute(self, "geotest-in", "geotest-out")
