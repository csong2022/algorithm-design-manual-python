#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Edit distance dynamic programming table cell.
"""

__author__ = "csong2022"


MATCH = 0  # enumerated type symbol for match
INSERT = 1  # enumerated type symbol for insert
DELETE = 2  # enumerated type symbol for delete


class Cell:
    def __init__(self, cost: int, parent: int):
        self.cost = cost  # cost of reaching this cell *
        self.parent = parent  # parent cell
