import random
from unittest import TestCase


class TestRandom(TestCase):

    def test_random_shuffle(self):
        p = list(range(10))
        p_2 = p[1:]

        random.shuffle(p_2)
        p[1:] = p_2

        print(p)