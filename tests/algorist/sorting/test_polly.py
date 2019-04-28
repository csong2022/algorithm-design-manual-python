from functools import cmp_to_key
from unittest import TestCase

from algorist.sorting.polly import read_suitors, suitor_compare
from tests.algorist.test.test_engine import execute


class TestPolly(TestCase):
    def process(self, input):
        suitors = read_suitors(input)
        suitors.sort(key=cmp_to_key(suitor_compare))

        for suitor in suitors:
            print("%s, %s" % (suitor.last, suitor.first))

    def test(self):
        execute(self, "polly-in", "polly-out")
