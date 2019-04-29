from unittest import TestCase

from algorist.data_structure.tree import Tree
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
