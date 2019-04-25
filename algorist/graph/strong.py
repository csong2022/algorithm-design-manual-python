from algorist.data_structure.linked_stack import Stack
from algorist.graph.bfs_dfs import EdgeType, DFS


def strong_components(g):
    """
    Identify strongly connected components in a graph.
    """
    dfs = DFS(g)
    callback = StrongCallback(g, dfs)

    for i in range(1, g.nvertices + 1):
        if not dfs.discovered[i]:
            dfs.search(i, callback)


class StrongCallback:
    def __init__(self, g, dfs):
        self.dfs = dfs

        self.low = [0] * (g.nvertices + 1)  # oldest vertex surely in component of v
        self.scc = [0] * (g.nvertices + 1)  # strong component number for each vertex

        for i in range(1, g.nvertices + 1):
            self.low[i] = i
            self.scc[i] = -1

        self.components_found = 0  # number of strong components identified
        self.active = Stack()  # active vertices of unassigned component

    def process_vertex_early(self, v):
        self.active.push(v)

    def process_vertex_late(self, v):
        if self.low[v] == v:  # edge (parent[v],v) cuts off scc
            self.pop_component(v)

        parent = self.dfs.parent[v]
        if parent > 0 and self.entry_time(self.low[v]) < self.entry_time(self.low[parent]):
            self.low[parent] = self.low[v]

    def pop_component(self, v):
        self.components_found += 1
        print("%d is in component %d " % (v, self.components_found));

        self.scc[v] = self.components_found

        while not self.active.is_empty():
            t = self.active.pop()
            if t == v:
                break
            self.scc[t] = self.components_found
            print("%d is in component %d with %d " % (t, self.components_found, v));

    def process_edge(self, x, y):
        classification = self.dfs.edge_classification(x, y)

        if classification == EdgeType.BACK:
            if self.entry_time(y) < self.entry_time(self.low[x]):
                self.low[x] = y
        if classification == EdgeType.CROSS:
            if self.scc[y] == -1:
                if self.entry_time(y) < self.entry_time(self.low[x]):
                    self.low[x] = y

    def entry_time(self, v):
        return self.dfs.entry_time[v]
