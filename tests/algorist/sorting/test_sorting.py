import random
from unittest import TestCase

from algorist.sorting.sorting import insertion_sort, selection_sort, quicksort, heapsort, mergesort, binary_search, \
    is_sorted
from tests.algorist.test.test_engine import execute

NELEM = 100


class TestSorting(TestCase):

    def process(self):
        s = list(range(NELEM))

        self.init_arr(s)
        insertion_sort(s, len(s))
        self.assertTrue(is_sorted(s))
        print("\n\nInsertion sort: ")
        self.print_arr(s)

        self.init_arr(s)
        selection_sort(s, len(s))
        self.assertTrue(is_sorted(s))
        print("\n\nSelection sort: ")
        self.print_arr(s)

        self.init_arr(s)
        quicksort(s, 0, len(s) - 1)
        self.assertTrue(is_sorted(s))
        print("\n\nQuicksort: ")
        self.print_arr(s)

        self.init_arr(s)
        heapsort(s, len(s))
        self.assertTrue(is_sorted(s))
        print("\n\nHeapsort sort: ")
        self.print_arr(s)

        self.init_arr(s)
        mergesort(s, 0, len(s) - 1)
        self.assertTrue(is_sorted(s))

        for i in range(len(s)):
            s[i] = 2 * (len(s) - i)
        random.shuffle(s)
        heapsort(s, len(s))
        self.assertTrue(is_sorted(s))

        for i in range(1, 2 * len(s) + 1):
            if i % 2 == 0:
                self.assertTrue(binary_search(s, i, 0, len(s)) >= 0, str(i))
            else:
                self.assertTrue(binary_search(s, i, 0, len(s)) == -1, str(i))

    def init_arr(self, s):
        for i in range(len(s)):
            s[i] = len(s) - i

        random.shuffle(s)

    def print_arr(self, s):
        for i in range(len(s)):
            print('%d ' % s[i]),
        print()

    def test(self):
        execute(self, None, "sorting-out")
