import unittest
from unittest import TestCase

from algorist.dp.fib import MAXN, fib_c_driver, fib_dp, fib_dp2, fib_r
from tests.algorist.test.test_engine import execute


class TestFib(TestCase):
    def process(self):
        for i in range(MAXN):
            print("fib_c(%d) = %d" % (i, fib_c_driver(i)))

        for i in range(MAXN):
            print("fib_c(%d) = %d" % (i, fib_dp(i)))

        for i in range(MAXN):
            print("fib_c(%d) = %d" % (i, fib_dp2(i)))

        for i in range(MAXN):
            print("fib_c(%d) = %d" % (i, fib_r(i)))

    @unittest.skip("Takes too long")
    def test(self):
        execute(self, None, "fib-out")