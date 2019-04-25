from unittest import TestCase

from algorist.graph.connected import connected_components
from algorist.graph.graph import GraphReader
from tests.algorist.test.test_engine import execute


class TestConnected(TestCase):
    def process(self, input):
        reader = GraphReader.unweighted()
        g = reader.read_graph(input, False)
        g.print()

        connected_components(g)

    def test_connected(self):
        self.assertTrue(execute(self, "connected-in", "connected-out"))

    def test_grid(self):
        self.assertTrue(execute(self, "grid", "grid-connected-out"))
