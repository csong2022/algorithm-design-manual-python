from unittest import TestCase

from algorist.data_structure.priority_queue import PriorityQueue


class TestPriorityQueue(TestCase):
    def test(self):
        a = [10 - i for i in range(10)]

        q1 = PriorityQueue.make_heap(a, len(a))
        q2 = PriorityQueue.make_heap1(a, len(a))

        self.assertFalse(q1.is_empty())
        q1.print()

        self.assertEqual(len(q1), len(q2))

        for i in range(len(q1)):
            self.assertEqual(q2.extract_min(), q1.extract_min())
