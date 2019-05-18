#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A generic adjacency list graph data type.

Translate from graph.h, graph.c, include functionalities in wgraph.h, wgraph.c.
Generify the edge node type, using List data structure as adjacent list.

Implementation supports unweighted, weighted, and flow graph.
"""

__author__ = "csong2022"

from algorist.data_structure.linked_list import List


class UnweightedEdgeNode:
    """Edge node for unweighted graph/digraph."""

    def __init__(self, y: int):
        self.y = y  # adjancency info

    def copy(self, v: int):
        return UnweightedEdgeNode(v)


class WeightedEdgeNode:
    """Edge node for Weighted graph/digraph."""

    def __init__(self, y: int, weight):
        self.y = y  # adjancency info
        self.weight = weight  # edge weight

    def copy(self, v: int):
        return WeightedEdgeNode(v, self.weight)


class GraphSearchCallback:
    """
    Graph traversal callback. Generify the customization point for graph traversal.
    """

    def process_vertex_early(self, v: int) -> None:
        """Triggered when first encounter the vertex."""
        pass

    def process_vertex_late(self, v: int) -> None:
        """Trigger when done all processing for the vertex."""
        pass

    def process_edge(self, x: int, y: int) -> None:
        """Process edge."""
        pass

    def valid_edge(self, e) -> bool:
        """Validate edge."""
        return True


class Graph:
    """
    Adjacency list representation of graph data structure.
    Supports unweighted, weighted, and flow graph.
    """

    def __init__(self, nvertices: int, directed: bool):
        self.edges = [List() for i in range(nvertices + 1)]  # adjacency info
        self.degree = [0] * (nvertices + 1)  # outdegree of each vertex

        self.nvertices = nvertices  # number of vertices in the graph
        self.nedges = 0  # number of edges in the graph
        self.directed = directed  # is the graph directed?

    def find_edge(self, x: int, y: int):
        self.validate_vertex(x)
        self.validate_vertex(y)
        return next((p for p in self.edges[x] if p.y == y), None)

    def validate_vertex(self, v: int) -> None:
        if v < 1 or v > self.nvertices:
            raise IndexError('Invalid vertex %d' % v)

    def insert_edge(self, x: int, n, directed: bool) -> None:
        """
        Insert new edge.
        :param x: starting vertex.
        :param n: Edge node of end vertex.
        :param directed: is directed?
        :return: None.
        """
        self.validate_vertex(x)
        self.validate_vertex(n.y)

        self.edges[x].insert(n)
        self.degree[x] += 1

        if not directed:
            self.insert_edge(n.y, n.copy(x), True)
        else:
            self.nedges += 1

    def delete_edge(self, x: int, y: int, directed: bool) -> None:
        """
        Delete edge.

        :param x: starting vertex.
        :param y: end vertex.
        :param directed: is directed?
        :return: None
        """
        self.validate_vertex(x)
        self.validate_vertex(y)

        n = self.find_edge(x, y)

        if n is not None:
            self.edges[x].delete(n)
            self.degree[x] -= 1
            if not directed:
                self.delete_edge(y, x, True)
            else:
                self.nedges -= 1
        else:
            print("Warning: deletion(%d,%d) not found in g" % (x, y))

    def print(self) -> None:
        for i in range(1, self.nvertices + 1):
            print("%d: " % i, end='')

            for p in self.edges[i]:
                print(" %d" % p.y, end='')
            print()


class UnweightedEdgeReader:

    def read_edge(self, _input) -> tuple:
        """
        Read unweighted graph edge from file input.

        :param _input: file input.
        :return: tuple of (starting vertex, end edge node)
        """
        x, y = list(map(int, _input.readline().split()))
        n = UnweightedEdgeNode(y)
        return x, n


class WeightedEdgeReader:

    def read_edge(self, _input) -> tuple:
        """
        Read weighted graph edge from file input.

        :param _input: file input.
        :return:  tuple of (starting vertex, end edge node)
        """
        x, y, w = list(map(int, _input.readline().split()))
        n = WeightedEdgeNode(y, w)
        return x, n


class GraphReader:
    """Construct graph from file input."""

    def __init__(self, edge_reader):
        self.edge_reader = edge_reader

    @staticmethod
    def unweighted():
        return GraphReader(UnweightedEdgeReader())

    @staticmethod
    def weighted():
        return GraphReader(WeightedEdgeReader())

    def read_graph(self, _input, directed: bool) -> Graph:
        nvertices, nedges = list(map(int, _input.readline().split()))

        g = Graph(nvertices, directed)

        for i in range(nedges):
            x, n = self.edge_reader.read_edge(_input)
            g.insert_edge(x, n, directed)

        return g
