#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Identify a cycle in a graph, if one exists.

Translate from findcycle.c.
"""

__author__ = "csong2022"

from algorist.graph.bfs_dfs import EdgeType, DFS
from algorist.graph.graph import GraphSearchCallback


class FindCycleCallback(GraphSearchCallback):
    def __init__(self, dfs: DFS):
        self.dfs = dfs

    def process_edge(self, x: int, y: int) -> None:
        classification = self.dfs.edge_classification(x, y)
        if classification == EdgeType.BACK:
            print("Cycle from %d to %d:" % (y, x))
            path = self.dfs.find_path(y, x)
            path.print()
            print()
            self.dfs.finished = True
