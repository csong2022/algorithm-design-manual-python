from unittest import TestCase

from algorist.graph.graph import GraphReader
from algorist.graph.topsort import topsort
from tests.algorist.test.test_engine import execute


class TestTopSort(TestCase):
    def process(self, input):
        reader = GraphReader.unweighted()
        g = reader.read_graph(input, True)
        g.print()

        out = topsort(g)

        for i in range(1, g.nvertices + 1):
            print(" %d" % out[i], end='')
        print()

    def test(self):
        execute(self, "grid", "grid-topsort-out")
