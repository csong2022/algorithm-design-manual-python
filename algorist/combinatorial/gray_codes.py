#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate n-bit Gray Codes.

Given a number n, generate bit patterns from 0 to 2^n-1 such that successive patterns differ by one bit.

Examples:

Following is 2-bit sequence (n = 2)
00 01 11 10

Following is 3-bit sequence (n = 3)
000 001 011 010 110 111 101 100

And Following is 4-bit sequence (n = 4)
0000 0001 0011 0010 0110 0111 0101 0100 1100 1101 1111
1110 1010 1011 1001 1000
"""
from typing import List

__author__ = "csong2022"


def generate_gray_codes(n: int) -> List:
    """
    n-bit Gray Codes can be generated from list of (n-1)-bit Gray codes using following steps.
    1) Let the list of (n-1)-bit Gray codes be L1. Create another list L2 which is reverse of L1.
    2) Modify the list L1 by prefixing a ‘0’ in all codes of L1.
    3) Modify the list L2 by prefixing a ‘1’ in all codes of L2.
    4) Concatenate L1 and L2. The concatenated list is required list of n-bit Gray codes.

    :param n: number of bits.
    :return: n-bit gray codes.
    """
    if n <= 0:
        return []

    arr = ['0', '1']

    for i in range(2, n + 1):
        l2 = ['1' + x for x in reversed(arr)]
        l1 = ['0' + x for x in arr]
        arr = l1 + l2

    return arr
