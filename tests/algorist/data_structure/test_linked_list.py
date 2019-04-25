from unittest import TestCase

from algorist.data_structure.linked_list import List
from tests.algorist.test.test_engine import execute


class TestList(TestCase):

    def setUp(self) -> None:
        self.l = List()

    def test(self):
        self.assertTrue(self.l.is_empty())
        self.l.insert(1)
        self.l.insert(2)
        self.l.insert(3)
        self.l.print()
        self.assertTrue(1 in self.l)
        self.assertTrue(2 in self.l)
        self.l.delete(2)
        self.assertFalse(2 in self.l)


class ListDemoTest(TestCase):

    def process(self, input):
        l = List()

        for line in input:
            tokens = line[:-1].split(' ')

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
                if d in l :
                    print("item %d deleted" % d)
                else:
                    print("item to delete %d not found" % d)
                l.delete(d)

    def test(self):
        execute(self, "list-in", "list-out")