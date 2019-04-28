# -*- coding: utf-8 -*-
"""
Topologically sort a directed acyclic graph by DFS numbering (DAG)

Translate from topsort1.c.
"""
from algorist.data_structure.linked_stack import Stack
from algorist.graph.bfs_dfs import EdgeType, DFS
from algorist.graph.graph import GraphSearchCallback, Graph


class TopSort1Callback(GraphSearchCallback):
    def __init__(self, dfs: DFS):
        self.dfs = dfs
        self.sorted = Stack()

    def process_vertex_late(self, v: int) -> None:
        self.sorted.push(v)

    def process_edge(self, x: int, y: int) -> None:
        classification = self.dfs.edge_classification(x, y)

        if classification == EdgeType.BACK:
            print("Warning: directed cycle found, not a DAG")


def topsort(g: Graph):
    dfs = DFS(g)
    callback = TopSort1Callback(dfs)

    for i in range(1, g.nvertices + 1):
        if not dfs.discovered[i]:
            dfs.search(i, callback)

    callback.sorted.print()
