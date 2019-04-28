from unittest import TestCase

from algorist.backtrack.backtrack import Backtrack
from algorist.backtrack.sudoku import DIMENSION, Board, Sudoku
from tests.algorist.test.test_engine import execute


class TestSudoku(TestCase):
    def process(self, input):
        a = [0] * (DIMENSION * DIMENSION + 1)
        board = Board.read(input)  # Sudoku board structure
        board.print()

        temp = Board()
        Board.copy_board(board, temp)

        backtrack = Backtrack()

        speed = [True, False]
        intelligence = [True, False]

        for fast in speed:
            for smart in intelligence:
                sudoku = Sudoku(backtrack, fast, smart)

                print("----------------------------------");
                sudoku.steps = 0
                Board.copy_board(temp, board)
                backtrack.finished = False

                backtrack.backtrack(a, 0, board, sudoku)

                print("It took %d steps to find this solution " % sudoku.steps, end='')
                print("for fast=%d  smart=%d" % (1 if fast else 0, 1 if smart else 0))

    def test(self):
        execute(self, "puzzle", "puzzle-out")
