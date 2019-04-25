from unittest import TestCase

from algorist.graph.bfs_dfs import BFS
from algorist.graph.graph import GraphReader, GraphSearchCallback
from tests.algorist.test.test_engine import execute


class BFSDemoCallback(GraphSearchCallback):
    def process_vertex_early(self, v):
        print("processed vertex %d" % v)

    def process_edge(self, x, y):
        print("processed edge (%d,%d)" % (x, y))


class BFSDemoTest(TestCase):
    def process(self, input):
        reader = GraphReader.unweighted()
        g = reader.read_graph(input, False)
        g.print()

        callback = BFSDemoCallback()
        bfs = BFS(g)
        bfs.search(1, callback)

        for i in range(1, g.nvertices + 1):
            print(" %d" % bfs.parent[i], end='')
        print()

        print()
        for i in range(1, g.nvertices + 1):
            path = bfs.find_path(1, i)
            path.print()

    def test(self):
        execute(self, "grid", "grid-bfs-demo-out")
