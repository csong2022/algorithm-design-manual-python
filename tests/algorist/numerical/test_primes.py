from unittest import TestCase

from algorist.numerical.primes import prime_factorization
from tests.algorist.test.test_engine import execute


class TestPrimes(TestCase):
    def process(self, input):
        while True:
            line = input.readline()
            if not line:
                break
            p = int(line[:-1])
            print("prime factorization of p=%ld " % p)
            prime_factorization(p)

    def test(self):
        execute(self, "primes-in", "primes-out")
