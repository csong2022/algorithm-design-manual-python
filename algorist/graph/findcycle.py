from algorist.graph.bfs_dfs import EdgeType
from algorist.graph.graph import GraphSearchCallback


class FindCycleCallback(GraphSearchCallback):
    def __init__(self, dfs):
        self.dfs = dfs

    def process_edge(self, x, y):
        classification = self.dfs.edge_classification(x, y)
        if classification == EdgeType.BACK:
            print("Cycle from %d to %d:" % (y,x))
            path = self.dfs.find_path(y, x)
            path.print()
            print()
            self.dfs.finished = True