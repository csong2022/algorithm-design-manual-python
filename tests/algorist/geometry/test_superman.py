from unittest import TestCase

from algorist.geometry.geometry import Circle, Point
from algorist.geometry.superman import superman
from tests.algorist.test.test_engine import execute


class TestSuperman(TestCase):

    def process(self, input):
        s = Point.read_point(input)
        t = Point.read_point(input)

        ncircles = int(input.readline()[:-1])

        c = [None]

        for i in range(1, ncircles + 1):
            c.append(Circle.read_circle(input))

        s.print()
        t.print()

        print("%d" % ncircles)
        for i in range(1, ncircles + 1):
            c[i].print()

        superman(s, t, c, ncircles)

    def test_superin1(self):
        execute(self, "superin1", "superin1-out")

    def test_superin2(self):
        execute(self, "superin2", "superin2-out")

    def test_superin3(self):
        execute(self, "superin3", "superin3-out")

    def test_superin4(self):
        execute(self, "superin4", "superin4-out")
