from algorist.backtrack.backtrack import BacktrackCallback


class NQueens(BacktrackCallback):
    """
    Solve the eight queens problem using backtracking.
    """

    def __init__(self):
        self.solution_count = 0  # how many solutions are there?

    def is_a_solution(self, a, k, n):
        return k == n

    def process_solution(self, a, k, n):
        self.solution_count += 1

    def construct_candidates(self, a, k, n):
        c = [0] * (n + 1)

        ncandidates = 0
        for i in range(1, n + 1):
            legal_move = True
            for j in range(1, k):
                if abs(k - j) == abs(i - a[j]):  # diagonal threat
                    legal_move = False
                if i == a[j]:  # column threat
                    legal_move = False
            if legal_move:
                c[ncandidates] = i
                ncandidates += 1

        return c, ncandidates

