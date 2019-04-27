from unittest import TestCase

from algorist.geometry.geometry import Point, points_to_line, intersection_point, \
    Segment, segments_intersect
from tests.algorist.test.test_engine import execute


class CgTest(TestCase):

    def process(self, input):
        while True:
            line = input.readline()
            if not line:
                break
            p1 = self.read_point(line)
            p2 = self.read_point(input.readline())
            q1 = self.read_point(input.readline())
            q2 = self.read_point(input.readline())

            s1 = Segment(p1, p2)
            s2 = Segment(q1, q2)

            l1 = points_to_line(p1, p2)
            l2 = points_to_line(q1, q2)

            s1.print()
            s2.print()

            print("segments_intersect test")
            print("%d" % (1 if segments_intersect(s1, s2) else 0))

            print("intersection point")
            tmp = intersection_point(l1, l2)
            if tmp is not None:
                i = tmp
            i.print()

            print("--------------------------------")

    def read_point(self, line):
        x, y = list(map(float, line.split()))
        return Point(x, y)

    def test(self):
        execute(self, "cgtest-in", "cgtest-out")
