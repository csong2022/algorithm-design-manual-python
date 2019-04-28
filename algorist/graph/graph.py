from algorist.data_structure.linked_list import List


class UnweightedEdgeNode:
    def __init__(self, y: int):
        self.y = y  # adjancency info

    def copy(self, v: int):
        return UnweightedEdgeNode(v)


class WeightedEdgeNode:
    def __init__(self, y: int, weight):
        self.y = y  # adjancency info
        self.weight = weight  # edge weight

    def copy(self, v: int):
        return WeightedEdgeNode(v, self.weight)


class GraphSearchCallback:
    def process_vertex_early(self, v: int) -> None:
        pass

    def process_vertex_late(self, v: int) -> None:
        pass

    def process_edge(self, x: int, y: int) -> None:
        pass

    def valid_edge(self, e):
        return True


class Graph:
    """
    A generic adjacency list graph data type.
    """

    def __init__(self, nvertices: int, directed: bool):
        self.edges = [List() for i in range(nvertices + 1)]  # adjacency info
        self.degree = [0] * (nvertices + 1)  # outdegree of each vertex

        self.nvertices = nvertices  # number of vertices in the graph
        self.nedges = 0  # number of edges in the graph
        self.directed = directed  # is the graph directed?

    def find_edge(self, x: int, y: int):
        self.validate_vertex(x)
        self.validate_vertex(y)
        return next((p for p in self.edges[x] if p.y == y), None)

    def validate_vertex(self, v: int):
        if v < 1 or v > self.nvertices:
            raise IndexError('Invalid vertex %d' % v)

    def insert_edge(self, x: int, n, directed: bool) -> None:
        self.validate_vertex(x)
        self.validate_vertex(n.y)

        self.edges[x].insert(n)
        self.degree[x] += 1

        if not directed:
            self.insert_edge(n.y, n.copy(x), True)
        else:
            self.nedges += 1

    def delete_edge(self, x: int, y: int, directed: bool) -> None:
        self.validate_vertex(x)
        self.validate_vertex(y)

        n = self.find_edge(x, y)

        if n is not None:
            self.edges[x].delete(n)
            self.degree[x] -= 1
            if not directed:
                self.delete_edge(y, x, True)
            else:
                self.nedges -= 1
        else:
            print("Warning: deletion(%d,%d) not found in g" % (x, y))

    def print(self) -> None:
        for i in range(1, self.nvertices + 1):
            print("%d: " % i, end='')

            for p in self.edges[i]:
                print(" %d" % p.y, end='')
            print()


class UnweightedEdgeReader:
    def read_edge(self, input) -> tuple:
        x, y = list(map(int, input.readline().split()))
        n = UnweightedEdgeNode(y)
        return x, n


class WeightedEdgeReader:
    def read_edge(self, input) -> tuple:
        x, y, w = list(map(int, input.readline().split()))
        n = WeightedEdgeNode(y, w)
        return x, n


class GraphReader:
    def __init__(self, edge_reader):
        self.edge_reader = edge_reader

    @staticmethod
    def unweighted():
        return GraphReader(UnweightedEdgeReader())

    @staticmethod
    def weighted():
        return GraphReader(WeightedEdgeReader())

    def read_graph(self, input, directed: bool) -> Graph:
        nvertices, nedges = list(map(int, input.readline().split()))

        g = Graph(nvertices, directed)

        for i in range(nedges):
            x, n = self.edge_reader.read_edge(input)
            g.insert_edge(x, n, directed)

        return g
