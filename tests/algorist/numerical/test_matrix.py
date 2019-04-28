from unittest import TestCase

from algorist.numerical.matrix import read_matrix, multiply
from tests.algorist.test.test_engine import execute


class TestMatrix(TestCase):
    def process(self, input):
        a = read_matrix(input)
        a.print()

        b = read_matrix(input)
        b.print()

        c = multiply(a, b)
        c.print()

    def test_matrix_data1(self):
        execute(self, "matrix-data1", "matrix-data1-out")

    def test_matrix_data2(self):
        execute(self, "matrix-data2", "matrix-data2-out")
