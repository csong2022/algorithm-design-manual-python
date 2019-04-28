from unittest import TestCase

from algorist.geometry.order import row_major, column_major, snake_order, diagonal_order
from tests.algorist.test.test_engine import execute


class TestOrder(TestCase):
    def process(self):
        print("row_major")
        row_major(5, 5)

        print("\ncolumn_major")
        column_major(3, 3)

        print("\nsnake_order")
        snake_order(5, 5)

        print("\ndiagonal_order")
        diagonal_order(3, 4)

        print("\ndiagonal_order")
        diagonal_order(4, 3)

    def test(self):
        execute(self, None, "order-out")
