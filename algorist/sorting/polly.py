#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rank the desirability of suitors -- sorting example.
"""
from algorist.utils.utils import cmp

__author__ = "csong2022"


class Suitor:
    def __init__(self, first: str, last: str, height: int, weight: int):
        self.first = first  # suitor's first name
        self.last = last  # suitor's last name
        self.height = height  # suitor's height
        self.weight = weight  # suitor's weight

    def __str__(self):
        return "%s,%s,%d,%d" % (self.last, self.first, self.height, self.weight)


BESTHEIGHT = 180  # best height in centimeters
BESTWEIGHT = 75  # best weight in kilograms


def read_suitors(_input) -> list:
    suitors = []

    while True:
        line = _input.readline()
        if not line:
            break
        values = line.split()
        first = values[0]
        last = values[1]

        height = int(values[2])
        height = abs(height - BESTHEIGHT)

        weight = int(values[3])
        if weight > BESTWEIGHT:
            weight -= BESTWEIGHT
        else:
            weight = -weight
        suitors.append(Suitor(first, last, height, weight))

    return suitors


def suitor_compare(a: Suitor, b: Suitor) -> int:
    result = cmp(a.height, b.height)
    if result != 0:
        return result

    result = cmp(a.weight, b.weight)
    if result != 0:
        return result

    result = cmp(a.last, b.last)
    if result != 0:
        return result

    return cmp(a.first, b.first)
