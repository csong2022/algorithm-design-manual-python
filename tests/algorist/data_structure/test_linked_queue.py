from unittest import TestCase

from algorist.data_structure.linked_queue import Queue


class TestQueue(TestCase):
    def setUp(self) -> None:
        self.q = Queue()

    def testDequeueEmptyStack(self):
        self.assertTrue(self.q.is_empty())
        self.q.print()
        with self.assertRaises(IndexError):
            self.q.dequeue()

    def test(self):
        self.assertTrue(self.q.is_empty())

        for i in range(1, 17):
            self.q.enqueue(i)

        self.q.print()

        self.assertFalse(self.q.is_empty())

        i = 1
        for x in self.q:
            self.assertEqual(x, i)
            i += 1

        for i in range(1, 17):
            self.assertEqual(self.q.dequeue(), i)

        self.assertTrue(self.q.is_empty())
