from unittest import TestCase

from algorist.backtrack.backtrack import Backtrack, NMAX
from algorist.backtrack.nqueens import NQueens
from tests.algorist.test.test_engine import execute


class TestNQueens(TestCase):
    def process(self):
        backtrack = Backtrack()
        n_queens = NQueens()

        a = [0] * NMAX # solution vector

        for i in range(1, 11):
            n_queens.solution_count = 0
            backtrack.backtrack(a, 0, i, n_queens)
            print("n=%d  solution_count=%d" % (i, n_queens.solution_count))

    def test(self):
        execute(self, None, "8-queens-out")
