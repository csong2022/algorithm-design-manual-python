from unittest import TestCase

from algorist.graph.bfs_dfs import DFS
from algorist.graph.findcycle import FindCycleCallback
from algorist.graph.graph import Graph, UnweightedEdgeNode


class TestFindCycle(TestCase):

    def test(self):
        g = Graph(4, True)
        g.insert_edge(1, UnweightedEdgeNode(2), True);
        g.insert_edge(2, UnweightedEdgeNode(3), True);
        g.insert_edge(3, UnweightedEdgeNode(1), True);
        g.insert_edge(3, UnweightedEdgeNode(4), True);
        g.print()

        dfs = DFS(g)
        callback = FindCycleCallback(dfs)
        dfs.search(1, callback)
