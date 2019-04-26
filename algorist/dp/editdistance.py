import sys

MAXLEN = 101  # longest possible string
MATCH = 0  # enumerated type symbol for match
INSERT = 1  # enumerated type symbol for insert
DELETE = 2  # enumerated type symbol for delete


class Cell:
    def __init__(self, cost, parent):
        self.cost = cost  # cost of reaching this cell *
        self.parent = parent  # parent cell


class EditDistance:
    """
     A generic implementation of string comparison via dynamic programming.
    """

    def __init__(self, string_edit):
        self.string_edit = string_edit
        # dynamic programming table
        self.m = [[Cell(0, -1) for j in range(MAXLEN + 1)] for i in range(MAXLEN + 1)]

    def string_compare(self, s, t):
        for j in range(len(t)):
            self.string_edit.row_init(j, self.m)

        for i in range(len(s)):
            self.string_edit.column_init(i, self.m)

        opt = [0] * 3  # cost of the three options
        for i in range(1, len(s)):
            for j in range(1, len(t)):
                opt[MATCH] = self.m[i - 1][j - 1].cost + self.string_edit.match(s[i], t[j])
                opt[INSERT] = self.m[i][j - 1].cost + self.string_edit.indel(t[j])
                opt[DELETE] = self.m[i - 1][j].cost + self.string_edit.indel(s[i])

                self.m[i][j] = Cell(opt[MATCH], MATCH)
                for k in [INSERT, DELETE]:
                    if opt[k] < self.m[i][j].cost:
                        self.m[i][j].cost = opt[k]
                        self.m[i][j].parent = k

        i, j = self.string_edit.goal_cell(s, t, self.m)
        return self.m[i][j].cost

    def reconstruct_path(self, s, t, i, j):
        # print("trace (%d,%d)" % (i, j), file=sys.stderr)
        if i < 0 or j < 0 or self.m[i][j].parent == -1:
            return

        if self.m[i][j].parent == MATCH:
            self.reconstruct_path(s, t, i - 1, j - 1)
            self.string_edit.match_out(s, t, i, j)

        elif self.m[i][j].parent == INSERT:
            self.reconstruct_path(s, t, i, j - 1)
            self.string_edit.insert_out(t, j)

        elif self.m[i][j].parent == DELETE:
            self.reconstruct_path(s, t, i - 1, j)
            self.string_edit.delete_out(s, i)

    def print_matrix(self, s, t, costQ):
        x = len(s)
        y = len(t)

        print("   ", end='')
        for i in range(y):
            print("  %c" % t[i], end='')
        print()

        for i in range(x):
            print("%c: " % s[i], end='')
            for j in range(y):
                if costQ:
                    print(" %2d" % self.m[i][j].cost, end='')
                else:
                    print(" %2d" % self.m[i][j].parent, end='')
            print()
