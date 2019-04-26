from unittest import TestCase

from algorist.backtrack.backtrack import NMAX, Backtrack
from algorist.backtrack.permutations import Permutations
from tests.algorist.test.test_engine import execute


class TestPermutations(TestCase):
    def process(self):
        a = [0] * NMAX  # solution vector

        permutations = Permutations()
        backtrack = Backtrack()
        backtrack.backtrack(a, 0, 0, permutations)
        backtrack.backtrack(a, 0, 1, permutations)
        backtrack.backtrack(a, 0, 2, permutations)
        backtrack.backtrack(a, 0, 3, permutations)

    def test(self):
        execute(self, None, "permutations-out")
