from unittest import TestCase

from algorist.graph.biconnected import articulation_vertices
from algorist.graph.graph import GraphReader
from tests.algorist.test.test_engine import execute


class TestBiconnected(TestCase):
    def process(self, input):
        reader = GraphReader.unweighted()
        g = reader.read_graph(input, False)
        g.print()

        articulation_vertices(g)

    def test_grid(self):
        execute(self, "grid", "biconnected-grid")

    def test_tree(self):
        execute(self, "tree", "biconnected-tree")

    def test_art3(self):
        execute(self, "art3", "biconnected-art3")

    def test_baase(self):
        execute(self, "baase", "biconnected-baase")

    def test_clr_graph(self):
        execute(self, "clr-graph", "biconnected-clr-graph")
