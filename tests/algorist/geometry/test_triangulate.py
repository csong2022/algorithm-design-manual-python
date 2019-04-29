from unittest import TestCase

from algorist.geometry.geometry import Polygon, Point
from algorist.geometry.triangulate import area_triangulation, area
from tests.algorist.test.test_engine import execute


class TestTriangulate(TestCase):
    def process(self, input):
        points = Point.read_points(input)

        p = Polygon(points, len(points))

        print(" area via triangulation = %f" % area_triangulation(p))
        print(" area slick = %f" % area(p))

    def test_tri1(self):
        execute(self, "tri1", "tri1-out")

    def test_tri2(self):
        execute(self, "tri2", "tri2-out")

    def test_tri3(self):
        execute(self, "tri3", "tri3-out")
