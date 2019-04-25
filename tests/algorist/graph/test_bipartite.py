from unittest import TestCase

from algorist.graph.bipartite import Bipartite
from algorist.graph.graph import GraphReader
from tests.algorist.test.test_engine import execute


class TestBipartite(TestCase):
    def process(self, input):
        reader = GraphReader.unweighted()
        g = reader.read_graph(input, False)
        g.print()

        bipartite = Bipartite(g)

        for i in range(1, g.nvertices + 1):
            print(" %d", bipartite.color[i]),
        print()

    def test_grid(self):
        execute(self, "grid", "bipartite-grid")

    def test_tree(self):
        execute(self, "tree", "bipartite-tree")

    def test_art3(self):
        execute(self, "art3", "bipartite-art3")
