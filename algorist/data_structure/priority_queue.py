class PriorityQueue:
    """
    Implementation of a heap / priority queue abstract data type.
    """

    def __init__(self):
        self.q = [None]  # body of queue
        self.n = 0  # number of queue elements

    def _parent(self, n):
        return -1 if n == 1 else int(n / 2)

    def _young_child(self, n):
        return 2 * n

    def bubble_up(self, p):
        parent = self._parent(p)
        if parent == -1:  # at root of heap, no parent
            return

        if self.q[parent] > self.q[p]:
            self.swap(p, parent)
            self.bubble_up(parent)

    def bubble_down(self, p):
        c = self._young_child(p)  # child index
        min_index = p

        for i in range(2):
            if c + i <= self.n:
                if self.q[min_index] > self.q[c + i]:
                    min_index = c + i

        if min_index != p:
            self.swap(p, min_index)
            self.bubble_down(min_index)

    def insert(self, x):
        self.q.append(x)
        self.n += 1
        self.bubble_up(self.n)

    def extract_min(self):
        min = None  # minimum value

        if self.is_empty():
            print("Warning: empty priority queue.")
        else:
            min = self.q[1]

            self.q[1] = self.q[self.n]
            self.q[self.n] = None
            self.n -= 1
            self.bubble_down(1)

        return min

    def is_empty(self):
        return self.n == 0

    def swap(self, i, j):
        if i != j:
            tmp = self.q[i]
            self.q[i] = self.q[j]
            self.q[j] = tmp

    def print(self):
        print(self.q[1: self.n], end=' ')

    def __len__(self):
        return self.n

    @staticmethod
    def make_heap(s, n):
        q = PriorityQueue()

        for i in range(0, n):
            q.q.append(s[i])

        q.n = n

        for i in range(n, 0, -1):
            q.bubble_down(i)

        return q

    @staticmethod
    def make_heap1(s, n):
        q = PriorityQueue()

        for i in range(0, n):
            q.insert(s[i])

        return q
