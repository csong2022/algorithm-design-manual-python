# -*- coding: utf-8 -*-
"""
Compute string edit distance *without* dynamic programming!

Translate from editbrute.c.
"""
from algorist.dp.editdistance_cell import MATCH, INSERT, DELETE, Cell
from algorist.dp.editdistance import EditDistance
from algorist.dp.stringedit import StringEdit


class EditBrute(EditDistance):
    """
    Compute string edit distance *without* dynamic programming!
    """

    def __init__(self, string_edit: StringEdit):
        super().__init__(string_edit)

    def string_compare2(self, s: str, t: str, i: int, j: int) -> int:
        opt = [0] * 3  # cost of the three options

        if i == 0: return j * self.string_edit.indel(' ')
        if j == 0: return i * self.string_edit.indel(' ')

        opt[MATCH] = self.string_compare2(s, t, i - 1, j - 1) + self.string_edit.match(s[i], t[j])
        opt[INSERT] = self.string_compare2(s, t, i, j - 1) + self.string_edit.indel(t[j])
        opt[DELETE] = self.string_compare2(s, t, i - 1, j) + self.string_edit.indel(s[i])

        lowest_cost = opt[MATCH]
        for k in [INSERT, DELETE]:
            if opt[k] < lowest_cost:
                lowest_cost = opt[k]

        self.m[i][j] = Cell(lowest_cost, -1)

        return lowest_cost
