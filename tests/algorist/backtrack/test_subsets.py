from unittest import TestCase

from algorist.backtrack.backtrack import NMAX, Backtrack
from algorist.backtrack.subsets import Subsets
from tests.algorist.test.test_engine import execute


class TestSubsets(TestCase):
    def process(self):
        a = [0] * NMAX

        subsets = Subsets()
        backtrack = Backtrack()
        backtrack.backtrack(a, 0, 3, subsets)

    def test(self):
        execute(self, None, "subsets-out")
