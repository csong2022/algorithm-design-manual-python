from algorist.graph.bfs_dfs import BFS
from algorist.graph.graph import GraphSearchCallback, Graph


class ConnectedCallback(GraphSearchCallback):
    def process_vertex_early(self, v: int) -> None:
        print(" %d" % v, end='')


def connected_components(g: Graph):
    bfs = BFS(g)
    callback = ConnectedCallback()

    c = 0
    for i in range(1, g.nvertices + 1):
        if not bfs.discovered[i]:
            c += 1
            print("Component %d:" % c, end='')
            bfs.search(i, callback)
            print()
