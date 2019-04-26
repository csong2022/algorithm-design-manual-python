from unittest import TestCase

from algorist.dp.editdistance import EditDistance
from algorist.dp.stringedit import StringEdit
from algorist.dp.substringedit import SubStringEdit
from tests.algorist.test.test_engine import execute


class TestSubStringEdit(TestCase):
    def process(self, input):
        s = ' ' + input.readline()[:-1]
        t = ' ' + input.readline()[:-1]

        string_edit = SubStringEdit()
        edit_distance = EditDistance(string_edit)

        print("matching cost = %d " % edit_distance.string_compare(s, t))

        edit_distance.print_matrix(s, t, True)
        print()
        edit_distance.print_matrix(s, t, False)

        i, j = string_edit.goal_cell(s, t, edit_distance.m)
        print("%d %d" % (i, j))

        edit_distance.reconstruct_path(s, t, i, j)
        print()

    def test(self):
        execute(self, "substringedit-in", "substringedit-out")