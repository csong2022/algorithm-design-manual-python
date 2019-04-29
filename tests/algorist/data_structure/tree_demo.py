from unittest import TestCase

from algorist.data_structure.tree import Tree
from tests.algorist.test.test_engine import execute


class TestTreeDemo(TestCase):
    def process(self, input):
        l = Tree()

        for line in input:
            tokens = line.split(' ')

            c = tokens[0].lower()
            if c == 'p':
                l.print()
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

    def test(self):
        execute(self, "list-in", "treelist-out")