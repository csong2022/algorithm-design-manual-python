from enum import Enum

from algorist.graph.bfs_dfs import BFS


class Color(Enum):
    UNCOLORED = 0  # vertex not yet colored
    WHITE = 1  # white vertex
    BLACK = 2  # black vertex


def complement(color):
    if color == Color.WHITE:
        return Color.BLACK
    elif color == Color.BLACK:
        return Color.WHITE
    else:
        return Color.UNCOLORED


class Bipartite:
    def __init__(self, g):
        self.color = [Color.UNCOLORED] * (g.nvertices + 1)  # assigned color of v
        self.bipartite = True  # is the graph bipartite?

        callback = BipartiteCallback(self)

        bfs = BFS(g)

        for i in range(1, g.nvertices + 1):
            if not bfs.discovered[i]:
                self.color[i] = Color.WHITE
                bfs.search(i, callback)


class BipartiteCallback:
    def __init__(self, bipartite):
        self.bipartite = bipartite

    def process_vertex_early(self, v):
        pass

    def process_vertex_late(self, v):
        pass

    def process_edge(self, x, y):
        if self.bipartite.color[x] == self.bipartite.color[y]:
            self.bipartite.bipartite = False
            print("Warning: graph not bipartite, due to (%d,%d)" % (x, y))

        self.bipartite.color[y] = complement(self.bipartite.color[x])
