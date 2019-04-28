# -*- coding: utf-8 -*-
"""
Construct all permutations via backtracking.

Translate from permutations.c.
"""
from algorist.backtrack.backtrack import BacktrackCallback


class Permutations(BacktrackCallback):
    """
    Construct all permutations via backtracking.
    """

    def is_a_solution(self, a: int, k: int, n: int) -> bool:
        return k == n

    def process_solution(self, a: int, k: int, n: int) -> None:
        for i in range(1, k + 1):
            print(' %d' % a[i], end='')
        print()

    def construct_candidates(self, a: int, k: int, n: int) -> tuple:
        in_perm = [False] * (n + 1)  # what is now in the permutation?
        c = [0] * (n + 1)
        for i in range(1, k):
            in_perm[a[i]] = True

        ncandidates = 0
        for i in range(1, n + 1):
            if not in_perm[i]:
                c[ncandidates] = i
                ncandidates += 1

        return c, ncandidates
