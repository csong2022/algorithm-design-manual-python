from algorist.data_structure.linked_stack import Stack
from algorist.graph.bfs_dfs import EdgeType, DFS


class TopSort1Callback:
    def __init__(self, dfs):
        self.dfs = dfs
        self.sorted = Stack()

    def process_vertex_early(self, v):
        pass

    def process_vertex_late(self, v):
        self.sorted.push(v)

    def process_edge(self, x, y):
        classification = self.dfs.edge_classification(x, y)

        if classification == EdgeType.BACK:
            print("Warning: directed cycle found, not a DAG")


def topsort(g):
    dfs = DFS(g)
    callback = TopSort1Callback(dfs)

    for i in range(1, g.nvertices + 1):
        if not dfs.discovered[i]:
            dfs.search(i, callback)

    callback.sorted.print()
