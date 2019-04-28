# -*- coding: utf-8 -*-
"""
Network flow implementation -- Ford-Fulkerson augmenting path algorithm.
"""
from algorist.graph.bfs_dfs import BFS
from algorist.graph.graph import Graph, GraphSearchCallback


class FlowEdgeNode:
    def __init__(self, y: int, capacity: int):
        self.y = y  # adjancency info
        self.capacity = capacity  # capacity of edge
        self.flow = 0  # flow through edg
        self.residual = capacity  # residual capacity of edge

    def increase_flow(self, delta: int) -> None:
        self.flow += delta
        self.residual -= delta

    def increase_residual(self, delta: int) -> None:
        self.residual += delta

    def copy(self, v: int):
        return FlowEdgeNode(v, self.capacity)

    def __str__(self):
        return "%d(%d,%d,%d)" % (self.y, self.capacity, self.flow, self.residual)


class FlowGraph(Graph):
    def __init__(self, nvertices: int, directed: bool):
        super().__init__(nvertices, directed)

    def add_residual_edges(self) -> None:
        for i in range(1, self.nvertices + 1):
            for p in self.edges[i]:
                if self.find_edge(p.y, i) is None:
                    self.insert_edge(p.y, FlowEdgeNode(i, 0), True)

    def print(self) -> None:
        for i in range(1, self.nvertices + 1):
            print("%d: " % i, end='')
            for p in self.edges[i]:
                print(" %s" % str(p), end='')
            print()


class FlowEdgeReader:
    def read_edge(self, input) -> tuple:
        x, y, w = list(map(int, input.readline().split()))
        n = FlowEdgeNode(y, w)
        return x, n


class FlowGraphReader:
    def __init__(self):
        self.edge_reader = FlowEdgeReader()

    def read_graph(self, input, directed: bool) -> Graph:
        nvertices, nedges = list(map(int, input.readline().split()))

        g = FlowGraph(nvertices, directed)

        for i in range(nedges):
            x, n = self.edge_reader.read_edge(input)
            g.insert_edge(x, n, directed)

        return g


class NetflowCallback(GraphSearchCallback):
    def valid_edge(self, e: FlowEdgeNode) -> bool:
        return e.residual > 0


def path_volume(g: Graph, start: int, end: int, parents: list) -> int:
    if parents[end] == -1:
        return 0

    e = g.find_edge(parents[end], end)

    if start == parents[end]:
        return e.residual
    else:
        return min(path_volume(g, start, parents[end], parents), e.residual)


def augment_path(g: Graph, start: int, end: int, parents: list, volume: int) -> None:
    if start == end: return

    e = g.find_edge(parents[end], end)
    e.increase_flow(volume)

    e = g.find_edge(end, parents[end])
    e.increase_residual(volume)

    augment_path(g, start, parents[end], parents, volume)


def netflow(g: Graph, source: int, sink: int):
    g.add_residual_edges()

    bfs = BFS(g)
    callback = NetflowCallback()

    bfs.search(source, callback)

    volume = path_volume(g, source, sink, bfs.parent)  # weight of the augmenting path

    while volume > 0:
        augment_path(g, source, sink, bfs.parent, volume)

        bfs.initialize()
        bfs.search(source, callback)

        volume = path_volume(g, source, sink, bfs.parent)

    return bfs.parent
