from unittest import TestCase

from algorist.graph.graph import GraphReader
from algorist.wgraph.netflow import FlowEdgeReader, netflow, FlowGraphReader
from tests.algorist.test.test_engine import execute


class TestNetflow(TestCase):

    def process(self, input):
        source, sink = list(map(int, input.readline().split()))
        reader = FlowGraphReader()
        g = reader.read_graph(input, True)

        netflow(g, source, sink)
        g.print()

        flow = 0  # total flow
        for p in g.edges[source]:
            flow += p.flow

        print("total flow = %d" % flow)

    def test_netflow1(self):
        execute(self, "netflow1-in", "netflow1-out")

    def test_netflow2(self):
        execute(self, "netflow2-in", "netflow2-out")

    def test_netflow3(self):
        execute(self, "netflow3-in", "netflow3-out")
