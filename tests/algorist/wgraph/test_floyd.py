from unittest import TestCase

from algorist.wgraph.floyd import AdjacencyMatrix, floyd
from tests.algorist.test.test_engine import execute


class TestFloyd(TestCase):
    def process(self, input):
        g = AdjacencyMatrix.read_adjacency_matrix(input, False)
        g.print_graph()

        floyd(g)
        g.print()

    def test(self):
        execute(self, "wgrid", "wgrid-floyd-out")
