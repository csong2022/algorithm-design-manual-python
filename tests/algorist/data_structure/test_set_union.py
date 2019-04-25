from unittest import TestCase

from algorist.data_structure.set_union import SetUnion


class TestSetUnion(TestCase):
    def setUp(self) -> None:
        pairs = [
            (5, 4),
            (4, 9),
            (7, 6),
            (10, 5),
            (3, 2),
            (9, 10),
            (6, 1),
            (8, 3),
            (7, 2),
            (2, 1),
            (7, 8)
        ]

        self.uf = SetUnion(len(pairs))

        for pair in pairs:
            self.uf.union_sets(pair[0], pair[1])

    def test(self):
        self.uf.print()

        c1 = (1, 2, 3, 6, 7, 8)
        self.assertTrue(self.withinSameComponent(c1))

        c2 = (4, 5, 9, 10)
        self.assertTrue(self.withinSameComponent(c2))

    def withinSameComponent(self, c):
        x0 = c[0]
        for x in c[1:]:
            if not self.uf.same_component(x0, x):
                return False

        return True
