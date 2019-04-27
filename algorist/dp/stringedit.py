from algorist.dp.cell import Cell, INSERT, DELETE


class StringEdit:
    """
    Compute the optimal alignment matching two strings
    """

    def goal_cell(self, s: str, t: str, m: list = None) -> int:
        return len(s) - 1, len(t) - 1

    def match(self, c: int, d: int) -> int:
        return 0 if c == d else 1

    def indel(self, c: int) -> int:
        return 1

    def row_init(self, i: int, m: list) -> None:  # what is m[0][i]?
        if i > 0:
            m[0][i] = Cell(i, INSERT)
        else:
            m[0][i] = Cell(i, -1)

    def column_init(self, i: int, m: list) -> None:  # what is m[i][0]?
        if i > 0:
            m[i][0] = Cell(i, DELETE)
        else:
            m[i][0] = Cell(i, -1)

    def match_out(self, s: str, t: str, i: int, j: int) -> None:
        if s[i] == t[j]:
            print("M", end='')
        else:
            print("S", end='')

    def insert_out(self, t: str, j: int) -> None:
        print("I", end='')

    def delete_out(self, s: str, i: int) -> None:
        print("D", end='')
