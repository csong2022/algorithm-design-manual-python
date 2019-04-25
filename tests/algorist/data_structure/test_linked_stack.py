from unittest import TestCase

from algorist.data_structure.linked_stack import Stack


class TestStack(TestCase):
    def setUp(self) -> None:
        self.s = Stack()

    def testPopEmptyStack(self):
        self.assertTrue(self.s.is_empty())
        self.s.print()
        with self.assertRaises(IndexError):
            self.s.pop()

    def test(self):
        self.assertTrue(self.s.is_empty())

        for i in range(1, 17):
            self.s.push(i)

        self.s.print()

        self.assertFalse(self.s.is_empty())

        for i in range(16, 0, -1):
            self.assertEqual(self.s.pop(), i)

        self.assertTrue(self.s.is_empty())
