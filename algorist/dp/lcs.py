#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Longest common subsequence of two strings.

Generify from lcs.c.
"""

__author__ = "csong2022"

from algorist.dp.editdistance import EditDistance, MAXLEN


class LCS(EditDistance):
    """
    Longest common subsequence of two strings.
    """

    def match(self, c: str, d: str) -> int:
        return 0 if c == d else MAXLEN

    def match_out(self, s: str, t: str, i: int, j: int) -> None:
        if s[i] == t[j]:
            print("%c" % s[i], end='')
