from unittest import TestCase

from algorist.geometry.convex_hull import convex_hull
from algorist.geometry.geometry import Point
from tests.algorist.test.test_engine import execute


class TestConvexHull(TestCase):
    def process(self, input):
        points = Point.read_points(input)

        polygon = convex_hull(points, len(points))
        polygon.print()

    def test_chin(self):
        execute(self, "chin", "chin-out")

    def test_chin1(self):
        execute(self, "chin1", "chin1-out")

    def test_i_2(self):
        execute(self, "i.2", "i.2-out")

    def test_i_4(self):
        execute(self, "i.4", "i.4-out")

    def test_i_9(self):
        execute(self, "i.9", "i.9-out")

    def test_i_10(self):
        execute(self, "i.10", "i.10-out")

    def test_i_19(self):
        execute(self, "i.19", "i.19-out")

    def test_convex_bad_10(self):
        execute(self, "convex-bad.10", "convex-bad.10-out")

    def test_VDError_uniq(self):
        execute(self, "VDError-uniq.dat", "VDError-uniq.dat-out")

    def test_VDError(self):
        execute(self, "VDError.dat", "VDError-uniq.dat-out")
