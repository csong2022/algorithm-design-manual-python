# -*- coding: utf-8 -*-
"""
Compute all-pairs shortest paths in weighted graphs.
"""
from algorist.graph.graph import Graph

MAXINT = 100007


class AdjacencyMatrix:
    def __init__(self, nvertices: int):
        self.nvertices = nvertices  # number of vertices in the graph
        # adjacency/weight info
        self.weight = [[MAXINT] * (nvertices + 1) for i in range(nvertices + 1)]

    @staticmethod
    def read_adjacency_matrix(_input, directed: bool):
        nvertices, m = list(map(int, _input.readline().split()))

        g = AdjacencyMatrix(nvertices)

        for i in range(m):
            x, y, w = list(map(int, _input.readline().split()))
            g.weight[x][y] = w
            if not directed:
                g.weight[y][x] = w

        return g

    def print_graph(self) -> None:
        for i in range(1, self.nvertices + 1):
            print("%d: " % i, end='')
            for j in range(1, self.nvertices + 1):
                if self.weight[i][j] < MAXINT:
                    print(" %d" % j, end='')
            print()

    def print(self) -> None:
        for i in range(1, self.nvertices + 1):
            print("%3d: " % i, end='')
            for j in range(1, self.nvertices + 1):
                print(" %3d" % self.weight[i][j], end='')
            print()


def floyd(g: AdjacencyMatrix):
    """
    Compute all-pairs shortest paths in weighted graphs.

    :param g: weighted graph in adjacency matrix format.
    :return: None
    """
    for k in range(1, g.nvertices + 1):
        for i in range(1, g.nvertices + 1):
            for j in range(1, g.nvertices + 1):
                through_k = g.weight[i][k] + g.weight[k][j]
                if through_k < g.weight[i][j]:
                    g.weight[i][j] = through_k
