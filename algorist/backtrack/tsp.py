# -*- coding: utf-8 -*-
"""
Heuristics for solving TSP.

Translate from tsp.h, tsp.c.
"""
import random
from math import sqrt

NMAX = 1000  # maximum number of points


class Point:
    def __init__(self, x: int, y: int):
        self.x = x  # x and y coordinates of point
        self.y = y

    @staticmethod
    def distance(p1, p2):
        return sqrt(sq(p1.x - p2.x) + sq(p1.y - p2.y))

    def __str__(self):
        return "%d, %d" % (self.x, self.y)


class TspInstance:
    def __init__(self, p: list, n: int):
        self.p = p  # array of points
        self.n = n  # how many points in problem?

    @staticmethod
    def read(input):
        n = int(input.readline()[:-1])
        p = [Point(-1, -1)]

        for i in range(n):
            _, x, y = list(map(int, input.readline().split()))
            p.append(Point(x, y))

        return TspInstance(p, n)

    def print(self) -> None:
        for i in range(1, self.n + 1):
            print("%d %d %d" % (i, self.p[i].x, self.p[i].y), end='')


class TspSolution:
    def __init__(self, p, n):
        self.p = p  # array if indices
        self.n = n  # how many elements in permutation?

    @staticmethod
    def initialize(n: int):
        p = list(range(n + 1))
        return TspSolution(p, n)

    def __copy__(self):
        return TspSolution(self.p[:], self.n)

    @staticmethod
    def read(input):
        n = int(input.readline()[:-1])
        p = [-1]

        for i in range(n):
            p.append(int(input.readline()[:-1]))

        return TspSolution(p, n)

    def random_solution(self):
        p = self.p[1:]
        random.shuffle(p)
        self.p[1:] = p

    def print(self):
        for i in range(1, self.n + 1):
            print(" %d" % self.p[i], end='')
        print("\n------------------------------------------------------")


def sq(x: int) -> int:
    return x * x


def distance(s: TspSolution, x: int, y: int, t: TspInstance) -> float:
    i = x
    j = y

    if i == t.n + 1:
        i = 1

    if j == t.n + 1:
        j = 1

    if i == 0:
        i = t.n

    if j == 0:
        j = t.n

    return Point.distance(t.p[(s.p[i])], t.p[(s.p[j])])


def solution_cost(s: TspSolution, t: TspInstance) -> float:
    cost = distance(s, t.n, 1, t)  # cost of solution

    for i in range(1, t.n):
        cost += distance(s, i, i + 1, t)

    return cost


def transition(s: TspSolution, t: TspInstance, i: int, j: int) -> float:
    neighbors = False  # i,j neighboring tour positions?

    if i == j:
        return 0.0

    if i > j:
        return transition(s, t, j, i)

    if i == j - 1:
        neighbors = True

    if i == 1 and j == s.n:
        i, j = j, i
        neighbors = True

    if neighbors:
        was = distance(s, i - 1, i, t) + distance(s, j, j + 1, t)
    else:
        was = distance(s, i - 1, i, t) + distance(s, i, i + 1, t) + \
              distance(s, j - 1, j, t) + distance(s, j, j + 1, t)

    s.p[j], s.p[i] = s.p[i], s.p[j]

    if neighbors:
        willbe = distance(s, i - 1, i, t) + distance(s, j, j + 1, t)
    else:
        willbe = distance(s, i - 1, i, t) + distance(s, i, i + 1, t) + \
                 distance(s, j - 1, j, t) + distance(s, j, j + 1, t)

    return willbe - was
