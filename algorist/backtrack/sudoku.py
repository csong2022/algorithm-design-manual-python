# A backtracking program to solve Sudoku
from algorist.backtrack.backtrack import BacktrackCallback, Backtrack

BASED = 3  # base dimension, 3*3 blocks
DIMENSION = BASED * BASED  # 9*9 board
NCELLS = DIMENSION * DIMENSION  # 81 cells in a 9*9 problem

DIGITS = "0123456789"


class Point:
    def __init__(self, x: int, y: int):
        self.x = x  # x and y coordinates of point
        self.y = y


class Board:
    def __init__(self):
        # matrix of board contents
        self.m = [[0] * (DIMENSION + 1) for i in range(DIMENSION + 1)]
        self.freecount = NCELLS  # how many open squares remain?
        self.move = [Point(-1, -1) for i in range(NCELLS + 1)]

    @staticmethod
    def copy_board(a, b):
        b.freecount = a.freecount
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                b.m[i][j] = a.m[i][j]

    @staticmethod
    def read(input):
        board = Board()
        for i in range(DIMENSION):
            line = input.readline()
            for j in range(DIMENSION):
                value = Board.to_digit(line[j])
                if value != 0:
                    board.fill_square(i, j, value)

        return board

    @staticmethod
    def to_digit(c: str) -> int:
        for i in range(len(DIGITS)):
            if c == DIGITS[i]:
                return i
        return -1

    def possible_values(self, x: int, y: int, possible: list) -> None:
        if x < 0 or y < 0 or self.m[x][y] != 0:
            init = False
        else:
            init = True

        for i in range(1, DIMENSION + 1):
            possible[i] = init

        for i in range(DIMENSION):
            if self.m[x][i] != 0:
                possible[self.m[x][i]] = False

        for i in range(DIMENSION):
            if self.m[i][y] != 0:
                possible[self.m[i][y]] = False

        xlow = BASED * (x // BASED)
        ylow = BASED * (y // BASED)

        for i in range(xlow, xlow + BASED):
            for j in range(ylow, ylow + BASED):
                if self.m[i][j] != 0:
                    possible[self.m[i][j]] = False

    @staticmethod
    def print_possible(possible: list):
        for i in range(DIMENSION + 1):
            if possible[i]:
                print(" %d" % i, end='')
        print()

    def possible_count(self, x: int, y: int) -> int:
        possible = [False] * (DIMENSION + 1)  # what is possible for the square
        self.possible_values(x, y, possible)
        cnt = 0
        for i in range(DIMENSION + 1):
            if possible[i]:
                cnt += 1
        return cnt

    def fill_square(self, x: int, y: int, v: int) -> None:
        if self.m[x][y] == 0:
            self.freecount -= 1
        else:
            print("Warning: filling already filled square (%d,%d)" % (x, y))
        self.m[x][y] = v

    def free_square(self, x: int, y: int) -> None:
        if self.m[x][y] != 0:
            self.freecount += 1
        else:
            print("Warning: freeing already empty square (%d,%d)" % (x, y))

        self.m[x][y] = 0

    def print(self) -> None:
        print("\nThere are %d free board positions." % self.freecount)

        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.m[i][j] == 0:
                    print(" ", end='')
                else:
                    print(DIGITS[self.m[i][j]], end='')

                if (j + 1) % BASED == 0:
                    print("|", end='')
            print()
            if (i + 1) % BASED == 0:
                for j in range(DIMENSION + BASED - 1):
                    print("-", end='')
                print()


class Sudoku(BacktrackCallback):
    def __init(self):
        self.fast = True
        self.smart = True

    def __init__(self, backtrack: Backtrack, fast: bool, smart: bool):
        self.backtrack = backtrack
        self.steps = 0
        self.fast = fast
        self.smart = smart

    def process_solution(self, a: list, k: int, board: Board) -> None:
        self.backtrack.finished = True
        print("process solution")
        board.print()

    def is_a_solution(self, a: list, k: int, board: Board) -> bool:
        self.steps += 1

        return board.freecount == 0

    def make_move(self, a: list, k: int, board: Board) -> None:
        board.fill_square(board.move[k].x, board.move[k].y, a[k])

    def unmake_move(self, a: list, k: int, board: Board) -> None:
        board.free_square(board.move[k].x, board.move[k].y)

    def construct_candidates(self, a: list, k: int, board: Board) -> tuple:
        possible = [False] * (DIMENSION + 1)
        c = [-1] * (DIMENSION + 1)
        x, y = self.next_square(board)  # which square should we fill next?

        board.move[k] = Point(x, y)  # store our choice of next position

        if x < 0 and y < 0:  # error condition, no moves possible
            return (), 0

        ncandidates = 0
        board.possible_values(x, y, possible)
        for i in range(1, DIMENSION + 1):
            if possible[i]:
                c[ncandidates] = i
                ncandidates += 1

        return c, ncandidates

    def next_square(self, board: Board) -> tuple:
        bestcnt = DIMENSION + 1  # the best square counts
        doomed = False  # some empty square without moves?

        x = -1
        y = -1
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                newcnt = board.possible_count(i, j)
                if newcnt == 0 and board.m[i][j] == 0:
                    doomed = True
                if self.fast:
                    if newcnt < bestcnt and newcnt >= 1:
                        bestcnt = newcnt
                        x = i
                        y = j
                else:
                    if newcnt >= 1 and board.m[i][j] == 0:
                        x = i
                        y = j

        if doomed and self.smart:
            x = -1  # initialize to non-position
            y = -1

        return x, y
