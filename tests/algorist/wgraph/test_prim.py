from unittest import TestCase

from algorist.graph.bfs_dfs import GraphSearchUtils
from algorist.graph.graph import GraphReader
from algorist.wgraph.prim import prim
from tests.algorist.test.test_engine import execute


class TestPrim(TestCase):

    def process(self, input):
        reader = GraphReader.weighted()
        g = reader.read_graph(input, False)

        parent = prim(g, 1)
        print("Out of Prim")

        print()
        for i in range(1, g.nvertices + 1):
            path = GraphSearchUtils.find_path(1, i, parent)
            print(' '.join(str(x) for x in path))

    def test(self):
        execute(self, "wgrid", "wgrid-prim-out")
