from unittest import TestCase

from algorist.graph.graph import GraphReader
from algorist.graph.strong import strong_components
from tests.algorist.test.test_engine import execute


class TestStrong(TestCase):
    def process(self, input):
        reader = GraphReader.unweighted()
        g = reader.read_graph(input, True)
        g.print()

        strong_components(g)

    def test_g_1(self):
        execute(self, "g-1", "strong-g-1")

    def test_g_2(self):
        execute(self, "g-2", "strong-g-2")

    def test_g_3(self):
        execute(self, "g-3", "strong-g-3")

    def test_g_4(self):
        execute(self, "g-4", "strong-g-4")

    def test_g_5(self):
        execute(self, "g-5", "strong-g-5")

    def test_strong_clr(self):
        execute(self, "strong-clr", "strong-clr-out")
