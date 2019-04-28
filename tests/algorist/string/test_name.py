from unittest import TestCase

from algorist.dp.editdistance import MAXLEN
from algorist.string.name import read_changes, process_mergers
from tests.algorist.test.test_engine import execute


class TestName(TestCase):

    def process(self, input):
        mergers = read_changes(input)

        nlines = int(input.readline()[:-1])

        s = [''] * MAXLEN
        for i in range(1, nlines + 1):
            line = input.readline()[:-1]
            s[:len(line)] = list(line)
            slen = process_mergers(s, len(line), mergers)

            for j in range(slen):
                print("%c" % s[j], end='')
            print()

    def test(self):
        execute(self, "name-in", "name-out")
