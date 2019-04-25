class SetUnion:
    """
    Union-find data structure implementation.
    """

    def __init__(self, n):
        self.n = n  # number of elements in set
        self.p = list(range(0, n + 1))  # parent element
        self.size = [1] * (n + 1)  # number of elements in set

    def find(self, x):
        if self.p[x] == x:
            return x
        else:
            return self.find(self.p[x])

    def union_sets(self, s1, s2):
        r1 = self.find(s1)
        r2 = self.find(s2)

        print("s1=%d r1=%d s2=%d r2=%d" % (s1, r1, s2, r2));

        if r1 == r2: return  # already in same set

        if self.size[r1] >= self.size[r2]:
            self.size[r1] += self.size[r2]
            self.p[r2] = r1
        else:
            self.size[r2] += self.size[r1]
            self.p[r1] = r2

    def same_component(self, s1, s2):
        return self.find(s1) == self.find(s2)

    def print(self):
        for i in range(1, self.n + 1):
            print("%i  set=%d size=%d " % (i, self.p[i], self.size[i]))
