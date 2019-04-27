from algorist.backtrack.backtrack import BacktrackCallback


class Subsets(BacktrackCallback):
    """
    Construct all subsets via backtracking.
    """

    def is_a_solution(self, a, k, n):
        return k == n

    def process_solution(self, a, k, n):
        print("{", end='')
        for i in range(1, k + 1):
            if a[i]:
                print(' %d' % i, end='')
        print(' }')

    def construct_candidates(self, a, k, n):
        c = [True, False]
        return c, len(c)
