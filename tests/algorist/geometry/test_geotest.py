from unittest import TestCase

from algorist.geometry.geometry import Point, Line
from tests.algorist.test.test_engine import execute


class GeoTest(TestCase):

    def process(self, input):
        while True:
            p1 = Point.read_point(input)
            if p1 is None:
                break
            p2 = Point.read_point(input)
            q1 = Point.read_point(input)
            q2 = Point.read_point(input)

            p1.print()
            p2.print()
            q1.print()
            q2.print()

            l1 = Line.points_to_line(p1, p2)
            l2 = Line.points_to_line(q1, q2)

            l1.print()
            l2.print()

            print("slope and line tests")
            l3 = Line.point_and_slope_to_line(p1, -l1.a)
            l3.print()

            l3 = Line.point_and_slope_to_line(p2, -l1.a)
            l3.print()

            l3 = Line.point_and_slope_to_line(q1, -l2.a)
            l3.print()

            l3 = Line.point_and_slope_to_line(q2, -l2.a)
            l3.print()

            print("parallel lines test")
            print("%d" % (1 if l1.parallel_q(l2) else 0))

            print("intersection point")

            tmp = l1.intersection_point(l2)
            if tmp is not None:
                i = tmp
            i.print()

            print("closest point")
            i = l1.closest_point(p1)
            i.print()
            i = l1.closest_point(p2)
            i.print()
            i = l1.closest_point(q1)
            i.print()
            i = l1.closest_point(q2)
            i.print()

            i = l2.closest_point(p1)
            i.print()
            i = l2.closest_point(p2)
            i.print()
            i = l2.closest_point(q1)
            i.print()
            i = l2.closest_point(q2)
            i.print()

            print("--------------------------------")

    def test(self):
        execute(self, "geotest-in", "geotest-out")
