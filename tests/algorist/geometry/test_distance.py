from unittest import TestCase

from algorist.geometry.distance import distance
from tests.algorist.test.test_engine import execute


class TestDistance(TestCase):
    def process(self):
        a = (6, 2, 3)
        b = (6, 3, 4)
        print("distance = %f" % distance(a,b))

    def test(self):
        execute(self, None, "distance-out")
