#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Identify articulation vertices in a graph.

Translate from biconnect.c.
"""
from algorist.graph.bfs_dfs import DFS, EdgeType
from algorist.graph.graph import GraphSearchCallback, Graph

__author__ = "csong2022"


def articulation_vertices(g: Graph) -> None:
    dfs = DFS(g)
    callback = BiconnectedCallback(g, dfs)

    for i in range(1, g.nvertices + 1):
        if not dfs.discovered[i]:
            dfs.search(i, callback)


class BiconnectedCallback(GraphSearchCallback):

    def __init__(self, g: Graph, dfs: DFS):
        self.dfs = dfs
        self.reachable_ancestor = [0] * (g.nvertices + 1)  # earliest reachable ancestor of v
        self.tree_out_degree = [0] * (g.nvertices + 1)  # DFS tree outdegree of v

    def process_vertex_early(self, v: int) -> None:
        self.reachable_ancestor[v] = v

    def process_vertex_late(self, v: int) -> None:
        if self.parent(v) < 1:  # test if v is the root
            if self.tree_out_degree[v] > 1:
                print("root articulation vertex: %d " % v)
            return

        root = self.parent(self.parent(v)) < 1  # test if parent[v] is root
        if self.reachable_ancestor[v] == self.parent(v) and (not root):
            print("parent articulation vertex: %d " % self.parent(v))

        if self.reachable_ancestor[v] == v:
            print("bridge articulation vertex: %d " % self.parent(v))

            if self.tree_out_degree[v] > 0:  # test if v is not a leaf
                print("bridge articulation vertex: %d " % v)

        time_v = self.entry_time(self.reachable_ancestor[v])
        time_parent = self.entry_time(self.reachable_ancestor[self.parent(v)])

        if time_v < time_parent:
            self.reachable_ancestor[self.parent(v)] = self.reachable_ancestor[v]

    def process_edge(self, x: int, y: int) -> None:
        edge_type = self.dfs.edge_classification(x, y)

        if edge_type == EdgeType.TREE:
            self.tree_out_degree[x] += 1

        if edge_type == EdgeType.BACK and self.parent(x) != y:
            if self.entry_time(y) < self.entry_time(self.reachable_ancestor[x]):
                self.reachable_ancestor[x] = y

    def parent(self, v: int) -> int:
        return self.dfs.parent[v]

    def entry_time(self, v: int) -> int:
        return self.dfs.entry_time[v]
