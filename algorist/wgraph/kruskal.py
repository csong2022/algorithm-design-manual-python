# -*- coding: utf-8 -*-
"""
Compute minimum spanning trees of graphs via Kruskal's algorithm.
"""
from algorist.data_structure.set_union import SetUnion
from algorist.graph.graph import Graph


class EdgePair:
    def __init__(self, x: int, y: int, weight: int):
        self.x = x  # adjacency info
        self.y = y
        self.weight = weight  # edge weight, if any


def to_edge_array(g: Graph) -> list:
    e = [EdgePair(0, 0, 0)] * (g.nedges + 1)

    m = 0
    for i in range(1, g.nvertices + 1):
        for p in g.edges[i]:
            if p.y > i:
                e[m] = EdgePair(i, p.y, p.weight)
                m += 1

    return e


def kruskal(g: Graph) -> None:
    """
    Compute minimum spanning trees of graphs via Kruskal's algorithm.
    :param g: weighted graph.
    :return: None
    """
    s = SetUnion(g.nvertices)
    print("initialized set union")

    e = to_edge_array(g)
    e.sort(key=lambda x: x.weight)

    for i in range(g.nedges):
        s.print()

        if not s.same_component(e[i].x, e[i].y):
            print("edge (%d,%d) of weight %d in MST" % (e[i].x, e[i].y, e[i].weight))
            s.union_sets(e[i].x, e[i].y)
