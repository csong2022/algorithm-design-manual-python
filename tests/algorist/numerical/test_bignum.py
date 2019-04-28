from unittest import TestCase

from algorist.numerical.bignum import Bignum, int_to_bignum, add_bignum, compare_bignum, subtract_bignum, \
    multiply_bignum, divide_bignum
from tests.algorist.test.test_engine import execute


class TestBignum(TestCase):
    def process(self, input):
        while True:
            line = input.readline()
            if not line:
                break
            a, b = list(map(int, line.split()))
            print("a = %d    b = %d" % (a, b))

            n1 = Bignum()
            int_to_bignum(a, n1)

            n2 = Bignum()
            int_to_bignum(b, n2)

            n3 = add_bignum(n1, n2)
            print("addition -- ", end='')
            n3.print()

            print("compare_bignum a ? b = %d" % compare_bignum(n1, n2))

            n3 = subtract_bignum(n1, n2)
            print("subtraction -- ", end='')
            n3.print()

            n3 = multiply_bignum(n1, n2)
            print("multiplication -- ", end='')
            n3.print()

            zero = Bignum()
            int_to_bignum(0, zero)

            if compare_bignum(zero, n2) == 0:
                print("division -- NaN ")
            else:
                n3 = divide_bignum(n1, n2)
                print("division -- ", end='')
                n3.print()

            print("--------------------------")

    def test(self):
        execute(self, "bignum-in", "bignum-out")
