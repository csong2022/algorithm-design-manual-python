# -*- coding: utf-8 -*-
"""
Compute minimum spanning trees of graphs via Dijkstra/Prim's algorithm.
"""
from algorist.graph.graph import Graph

MAXINT = 100007


def prim(g: Graph, start: int) -> list:
    """
    ompute minimum spanning trees of graphs via Dijkstra/Prim's algorithm.
    :param g: weighted graph
    :param start: starting vertex
    :return: discovery relation array
    """

    parent = [-1] * (g.nvertices + 1)  # discovery relation *
    intree = [False] * (g.nvertices + 1)  # is the vertex in the tree yet?
    distance = [MAXINT] * (g.nvertices + 1)  # cost of adding to tree

    distance[start] = 0

    v = start  # current vertex to process
    while not intree[v]:
        intree[v] = True

        for p in g.edges[v]:
            w, weight = p.y, p.weight
            if distance[w] > weight and (not intree[w]):
                distance[w] = weight
                parent[w] = v

        v, dist = 1, MAXINT
        for i in range(1, g.nvertices + 1):
            if (not intree[i]) and dist > distance[i]:
                v, dist = i, distance[i]

    return parent
