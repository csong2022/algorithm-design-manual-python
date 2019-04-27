class BacktrackCallback:
    """
    Back track callback API.
    """

    def is_a_solution(self, a, k, input):
        """
         Test the first k elements of vector a are a complete solution for the given problem.

        :param a: solution vector.
        :param k: first k elements.
        :param input: allow pass general information.
        :return: true if the first k elements of vector a are a complete solution, otherwise false.
        """
        return False

    def process_solution(self, a, k, input):
        """
        Process a complete solution once it is constructed.

        :param a: solution vector.
        :param k: first k elements.
        :param input: allow pass general information.
        :return: None
        """
        pass

    def construct_candidates(self, a, k, input):
        """
        Fills an array c with the complete set of possible candidates for the kth position of a,
        given the contents of the first k - 1 positions.

        :param a: solution vector.
        :param k: first k elements.
        :param input: allow pass general information.
        :return: pair candidates and number of candidates and
        """
        return 0

    def make_move(self, a, k, input):
        """
        Make a move based on updated kth position of a.

        :param a: solution vector.
        :param k: first k elements.
        :param input: allow pass general information.
        :return: None
        """
        pass

    def unmake_move(self, a, k, input):
        """
        Undo the move based on updated kth position of a.

        :param a: solution vector.
        :param k: first k elements.
        :param input: allow pass general information.
        :return: None
        """
        pass


NMAX = 100  # maximum solution size
MAXCANDIDATES = 100  # max possible next extensions


class Backtrack:
    """
    A generic backtracking implementation.
    """

    def __init__(self):
        self.finished = False  # found all solutions yet?

    def backtrack(self, a, k, input, callback):
        if callback.is_a_solution(a, k, input):
            callback.process_solution(a, k, input)
        else:
            k += 1
            c, ncandidates = callback.construct_candidates(a, k, input)

            for i in range(ncandidates):
                a[k] = c[i]
                callback.make_move(a, k, input)
                self.backtrack(a, k, input, callback)
                if self.finished:  # terminate early
                    return
                callback.unmake_move(a, k, input)