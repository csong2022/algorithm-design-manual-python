from unittest import TestCase

from algorist.data_structure.tree import Tree, preorder, postorder
from tests.algorist.test.test_engine import execute


class TestTreeDemo(TestCase):
    def process(self, input):
        identity = lambda x: x
        l = Tree(key=identity)

        for line in input:
            tokens = line[:-1].split(' ')

            c = tokens[0].lower()
            if c == 'p':
                l.print()
                print()
            elif c == 'i':
                d = int(tokens[1])
                print("new item: %d" % d)
                l.insert(d)
            elif c == 's':
                d = int(tokens[1])
                if d in l:
                    print("item %d found" % d)
                else:
                    print("item %d not found" % d)
            elif c == 'd':
                d = int(tokens[1])
                print(" deleting item %d" % d)
                l.delete(d)
                l.print()
                print()

    def test_list(self):
        execute(self, "list-in", "treelist-out")

    def test_t1(self):
        execute(self, "t1.in", "t1.out")


class TestInOrderTraverse(TestCase):
    def setUp(self) -> None:
        self.l = Tree()
        self.l.insert(5)
        self.l.insert(3)
        self.l.insert(2)
        self.l.insert(4)

        self.l.insert(8)
        self.l.insert(6)
        self.l.insert(9)

    def test_inorder(self):
        _list = list(self.l)
        self.assertEqual([2, 3, 4, 5, 6, 8, 9], _list)

    def test_preorder(self):
        _list = list(preorder(self.l.root))
        self.assertEqual([5, 3, 2, 4, 8, 6, 9], _list)

    def test_postorder(self):
        _list = list(postorder(self.l.root))
        self.assertEqual([2, 4, 3, 6, 9, 8, 5], _list)
