from unittest import TestCase

from algorist.graph.bfs_dfs import EdgeType, DFS
from algorist.graph.graph import GraphReader
from tests.algorist.test.test_engine import execute


class DFSDemoCallback:
    def __init__(self, dfs):
        self.dfs = dfs

    def process_vertex_early(self, v):
        self.dfs.time += 1
        self.dfs.entry_time[v] = self.dfs.time
        print("entered vertex %d at time %d" % (v, self.dfs.entry_time[v]))

    def process_vertex_late(self, v):
        self.dfs.time += 1
        self.dfs.exit_time[v] = self.dfs.time
        print("exit vertex %d at time %d" % (v, self.dfs.exit_time[v]));

    def process_edge(self, x, y):
        classification = self.dfs.edge_classification(x, y);

        if classification == EdgeType.BACK:
            print("back edge (%d,%d)" % (x, y))
        elif classification == EdgeType.TREE:
            print("tree edge (%d,%d)" % (x, y))
        elif classification == EdgeType.FORWARD:
            print("forward edge (%d,%d)" % (x, y))
        elif classification == EdgeType.CROSS:
            print("cross edge (%d,%d)" % (x, y))
        else:
            print("edge (%d,%d)\n not in valid class=%d" % (x, y, classification))


class DFSDemoTest(TestCase):
    def process(self, input):
        reader = GraphReader.unweighted()
        g = reader.read_graph(input, False)
        g.print()

        dfs = DFS(g)
        callback = DFSDemoCallback(dfs)
        dfs.search(1, callback)

        print()
        for i in range(1, g.nvertices + 1):
            path = dfs.find_path(1, i)
            print(path, end=' ')

    def test(self):
        execute(self, "grid", "grid-dfs-demo-out")
