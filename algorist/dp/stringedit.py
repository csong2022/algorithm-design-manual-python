from algorist.dp.editdistance import Cell, INSERT, DELETE


class StringEdit:
    """
    Compute the optimal alignment matching two strings
    """
    def goal_cell(self, s, t, m=None):
        return len(s) - 1, len(t) - 1

    def match(self, c, d):
        return 0 if c == d else 1

    def indel(self, c):
        return 1

    def row_init(self, i, m): # what is m[0][i]?
        if i > 0:
            m[0][i] = Cell(i, INSERT)
        else:
            m[0][i] = Cell(i, -1)

    def column_init(self, i, m): # what is m[i][0]?
        if i > 0:
            m[i][0] = Cell(i, DELETE)
        else:
            m[i][0] = Cell(i, -1)

    def match_out(self, s, t, i, j):
        if s[i] == t[j]:
            print("M", end='')
        else:
            print("S", end='')

    def insert_out(self, t, j):
        print("I", end='')

    def delete_out(self, s, i):
        print("D", end='')
