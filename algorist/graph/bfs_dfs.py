#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A generic implementation of graph traversal: breadth-first
and depth-first search

Translate from bfs-dfs.c.
"""

__author__ = "csong2022"

from collections import Iterable
from enum import Enum

from algorist.data_structure.linked_queue import Queue
from algorist.data_structure.linked_stack import Stack
from algorist.graph.graph import Graph, GraphSearchCallback


class GraphSearchUtils:
    @staticmethod
    def find_path(start: int, end: int, parents: list) -> Iterable:
        path = Stack()
        GraphSearchUtils._find_path(start, end, parents, path)
        return path

    @staticmethod
    def _find_path(start: int, end: int, parents: list, path: Stack) -> None:
        if start == end or end == -1:
            path.push(start)
        else:
            path.push(end)
            GraphSearchUtils._find_path(start, parents[end], parents, path)


class AbstractGraphSearch:
    def __init__(self, g: Graph):
        assert g is not None, "Graph not set."

        self.g = g
        self.processed = [False] * (g.nvertices + 1)
        self.discovered = [False] * (g.nvertices + 1)
        self.parent = [-1] * (g.nvertices + 1)
        self.initialize()

    def initialize(self):
        for i in range(0, self.g.nvertices + 1):
            self.processed[i] = self.discovered[i] = False
            self.parent[i] = -1

    def find_path(self, start: int, end: int) -> Iterable:
        assert 1 <= start <= self.g.nvertices, "Invalid vertex %d" % start
        assert 1 <= end <= self.g.nvertices, "Invalid vertex %d" % end

        return GraphSearchUtils.find_path(start, end, self.parent)


class BFS(AbstractGraphSearch):
    """
    A generic implementation of graph traversal: breadth-first and depth-first search
    """

    def __init__(self, g: Graph):
        super().__init__(g)

    def search(self, start: int, callback: GraphSearchCallback) -> None:
        assert 1 <= start <= self.g.nvertices, "Invalid vertex %d" % start

        q = Queue()
        q.enqueue(start)
        self.discovered[start] = True

        while not q.is_empty():
            v = q.dequeue()
            callback.process_vertex_early(v)
            self.processed[v] = True

            for p in self.g.edges[v]:
                if callback.valid_edge(p):
                    y = p.y
                    if (not self.processed[y]) or self.g.directed:
                        callback.process_edge(v, y)
                    if not self.discovered[y]:
                        q.enqueue(y)
                        self.discovered[y] = True
                        self.parent[y] = v

            callback.process_vertex_late(v)


class EdgeType(Enum):
    """
    DFS edge types
    """
    TREE = 0  # tree edge
    BACK = 1  # back edge
    CROSS = 2  # cross edge
    FORWARD = 3  # forward edge


class DFS(AbstractGraphSearch):
    """
    A generic implementation of graph traversal: depth-first search.
    """

    def __init__(self, g: Graph):
        super().__init__(g)
        self.entry_time = [0] * (g.nvertices + 1)  # time of vertex entry
        self.exit_time = [0] * (g.nvertices + 1)  # time of vertex exit
        self.time = 0  # current event time
        self.finished = False  # if true, cut off search immediately

    def initialize(self):
        super().initialize()
        self.time = 0

    def edge_classification(self, x: int, y: int) -> EdgeType:
        assert 1 <= x <= self.g.nvertices, "Invalid vertex %d" % x
        assert 1 <= y <= self.g.nvertices, "Invalid vertex %d" % y

        if self.parent[y] == x:
            return EdgeType.TREE
        if self.discovered[y] and (not self.processed[y]):
            return EdgeType.BACK
        if self.processed[y] and self.entry_time[y] > self.entry_time[x]:
            return EdgeType.FORWARD
        if self.processed[y] and self.entry_time[y] < self.entry_time[x]:
            return EdgeType.CROSS

        print("Warning: self loop (%d,%d)" % (x, y))
        return None

    def search(self, v: int, callback: GraphSearchCallback) -> None:
        assert 1 <= v <= self.g.nvertices, "Invalid vertex %d" % v

        if self.finished:  # allow for search termination
            return

        self.discovered[v] = True
        self.time += 1
        self.entry_time[v] = self.time

        callback.process_vertex_early(v)

        for p in self.g.edges[v]:
            y = p.y
            if not self.discovered[y]:
                self.parent[y] = v
                callback.process_edge(v, y)
                self.search(y, callback)
            elif (not self.processed[y]) or self.g.directed:
                callback.process_edge(v, y)

            if self.finished:
                return

        callback.process_vertex_late(v)
        self.time += 1
        self.exit_time[v] = self.time
        self.processed[v] = True
