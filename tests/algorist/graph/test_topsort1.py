from unittest import TestCase

from algorist.graph.graph import GraphReader
from algorist.graph.topsort1 import topsort
from tests.algorist.test.test_engine import execute


class TestTopSort1(TestCase):
    def process(self, input):
        reader = GraphReader.unweighted()
        g = reader.read_graph(input, True)
        g.print()

        topsort(g)

    def test(self):
        execute(self, "grid", "grid-topsort1-out")