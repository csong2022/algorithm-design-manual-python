# -*- coding: utf-8 -*-
"""
Longest common subsequence of two strings.

Generify from lcs.c.
"""
from algorist.dp.editdistance import EditDistance, MAXLEN


class LCS(EditDistance):
    """
    Longest common subsequence of two strings.
    """

    def match(self, c: int, d: int) -> int:
        return 0 if c == d else MAXLEN

    def match_out(self, s: str, t: str, i: int, j: int) -> None:
        if s[i] == t[j]:
            print("%c" % s.charAt(i), end='')
