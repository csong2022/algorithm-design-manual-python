from algorist.dp.editdistance import Cell
from algorist.dp.stringedit import StringEdit


class SubStringEdit(StringEdit):
    """
    Approximately match one string as a substring of another, where is s in t?
    """
    def goal_cell(self, s: str, t: str, m: list) -> tuple:
        i = len(s) - 1
        j = 0

        for k in range(len(t)):
            if m[i][k].cost < m[i][j].cost:
                j = k
        return i, j

    def row_init(self, i: int, m: list) -> None:
        m[0][i] = Cell(0, -1)
