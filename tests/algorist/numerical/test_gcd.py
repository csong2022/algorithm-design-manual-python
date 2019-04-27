from unittest import TestCase

from algorist.numerical.gcd import gcd1, gcd
from tests.algorist.test.test_engine import execute


class TestGcd(TestCase):
    def process(self, input):
        while True:
            line = input.readline()
            if not line:
                break
            p, q = list(map(int, line.split()))
            g1 = gcd1(p, q)
            print("gcd of p=%d and q=%d = %d" % (p, q, g1))
            g2, x, y = gcd(p, q)
            print(" %d*%d + %d*%d = %d" % (p, x, q, y, g2))

            if g1 != g2:
                print("ERROR: GCD")

            if (p * x + q * y) != g1:
                print("ERROR: DIOPHONINE SOLUTION WRONG!")

    def test(self):
        execute(self, "gcd-in", "gcd-out")
