from algorist.graph.bfs_dfs import BFS


class ConnectedCallback:
    def process_vertex_early(self, v):
        print(" %d" % v)

    def process_vertex_late(self, v):
        pass

    def process_edge(self, x, y):
        pass


def connected_components(g):
    bfs = BFS(g)
    callback = ConnectedCallback()

    c = 0
    for i in range(1, g.nvertices + 1):
        if not bfs.discovered[i]:
            c += 1
            print("Component %d:" % c),
            bfs.search(i, callback)
            print()
