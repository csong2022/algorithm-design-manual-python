#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Elevator stop optimization via dynamic programming.

Translate from elevator.c.
"""

__author__ = "csong2022"

MAX_RIDERS = 50  # what is the capacity of the elevator?
NFLOORS = 25  # the height of the building in floors
MAXINT = 100007


class Elevator:
    """
    Elevator stop optimization via dynamic programming.
    """

    def __init__(self, stops: list, nstops: int):
        self.nriders = len(stops) - 1
        self.nstops = nstops
        self.stops = stops
        self.m = [[0] * (nstops + 1) for i in range(NFLOORS + 1)]
        self.p = [[0] * (nstops + 1) for i in range(NFLOORS + 1)]

    def optimize_floors(self):
        for i in range(0, NFLOORS + 1):
            self.m[i][0] = self.floors_walked(0, MAXINT)
            self.p[i][0] = -1

        for j in range(1, self.nstops + 1):
            for i in range(0, NFLOORS + 1):
                self.m[i][j] = MAXINT
                for k in range(0, i + 1):
                    cost = self.m[k][j - 1] - self.floors_walked(k, MAXINT) + \
                           self.floors_walked(k, i) + self.floors_walked(i, MAXINT)
                    if cost < self.m[i][j]:
                        self.m[i][j] = cost
                        self.p[i][j] = k

        laststop = 0
        for i in range(1, NFLOORS + 1):
            if self.m[i][self.nstops] < self.m[laststop][self.nstops]:
                laststop = i

        return laststop

    def floors_walked(self, previous: int, current: int) -> int:
        nsteps = 0  # total distance traveled

        for i in range(1, self.nriders + 1):
            if previous < self.stops[i] <= current:
                nsteps += min(self.stops[i] - previous, current - self.stops[i])

        return nsteps

    def reconstruct_path(self, lastfloor: int, stops_to_go: int) -> None:
        if stops_to_go > 1:
            self.reconstruct_path(self.p[lastfloor][stops_to_go], stops_to_go - 1)

        print("%d" % lastfloor)

    def print_matrix(self, m: list) -> None:
        for j in range(self.nstops + 1):
            for i in range(NFLOORS + 1):
                print("%3d" % m[i][j], end='')
            print()
