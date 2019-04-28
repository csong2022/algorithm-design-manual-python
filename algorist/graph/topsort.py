# -*- coding: utf-8 -*-
"""
Topologically sort a directed acyclic graph (DAG)

Translate from topsort.c.
"""
from algorist.data_structure.linked_queue import Queue
from algorist.graph.graph import Graph


def compute_indegrees(g: Graph):  # indegree of each vertex
    indegree = [0] * (g.nvertices + 1)

    for i in range(1, g.nvertices + 1):
        for p in g.edges[i]:
            indegree[p.y] += 1

    return indegree


def topsort(g: Graph):
    _sorted = [None] * (g.nvertices + 1)
    indegree = compute_indegrees(g)

    zeroin = Queue()  # vertices of indegree 0
    for i in range(1, g.nvertices + 1):
        if indegree[i] == 0:
            zeroin.enqueue(i)

    j = 0  # counters
    while not zeroin.is_empty():
        j += 1
        x = zeroin.dequeue()
        _sorted[j] = x
        for p in g.edges[x]:
            y = p.y
            indegree[y] -= 1
            if indegree[y] == 0:
                zeroin.enqueue(y)

    if j != g.nvertices:
        print("Not a DAG -- only %d vertices found" % j)

    return _sorted
