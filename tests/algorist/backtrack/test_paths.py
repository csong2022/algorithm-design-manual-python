from unittest import TestCase

from algorist.backtrack.backtrack import Backtrack, NMAX
from algorist.backtrack.paths import Paths
from algorist.graph.graph import GraphReader
from tests.algorist.test.test_engine import execute


class TestPaths(TestCase):

    def process(self, input):
        reader = GraphReader.unweighted()
        g = reader.read_graph(input, False)
        g.print()

        backtrack = Backtrack()
        paths = Paths(g)

        a = [0] * NMAX  # solution vector
        for i in range(1, g.nvertices + 1):
            print("\nPaths from 1 to %d:" % i)
            backtrack.backtrack(a, 0, i, paths)

    def test(self):
        execute(self, "paths-graph", "paths-graph-out")
