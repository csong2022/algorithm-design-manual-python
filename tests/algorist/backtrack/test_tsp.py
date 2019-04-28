from unittest import TestCase

from algorist.backtrack.annealing import Annealing
from algorist.backtrack.tsp import TspInstance, TspSolution, solution_cost
from tests.algorist.test.test_engine import execute


class TestTsp(TestCase):
    def process(self, input):
        t = TspInstance.read(input)
        s = TspSolution.read(input)

        print("OPTIMAL SOLUTION COST = %7.1f" % solution_cost(s, t))
        s.print()

        s = TspSolution.initialize(t.n)
        print("solution_cost = %7.1f" % solution_cost(s, t))
        s.print()

        annealing = Annealing()
        s = annealing.repeated_annealing(t, 3)
        print("repeated annealing %d iterations, cost = %7.1f" %
              (annealing.solution_count, solution_cost(s, t)))

        s.print()

    # @unittest.skip
    def test(self):
        execute(self, "tsp48-in", "tsp48-out")
