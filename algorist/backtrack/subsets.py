# -*- coding: utf-8 -*-
"""
Construct all subsets via backtracking.

Translate from subsets.c.
"""
from algorist.backtrack.backtrack import BacktrackCallback


class Subsets(BacktrackCallback):
    """
    Construct all subsets via backtracking.
    """

    def is_a_solution(self, a: list, k: int, n: int) -> bool:
        return k == n

    def process_solution(self, a: list, k: int, n: int) -> None:
        print("{", end='')
        for i in range(1, k + 1):
            if a[i]:
                print(' %d' % i, end='')
        print(' }')

    def construct_candidates(self, a: list, k: int, n: int) -> tuple:
        c = [True, False]
        return c, len(c)
