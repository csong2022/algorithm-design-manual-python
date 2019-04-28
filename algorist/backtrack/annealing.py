# -*- coding: utf-8 -*-
"""
Simulated Annealing Implementation.

Translate from annealing.h, annealing.c.
"""

import copy
import random

from algorist.backtrack.tsp import TspSolution, TspInstance, solution_cost, transition

TRACE_OUTPUT = False  # print the swaps as they happen
PRINT_FREQUENCY = 10000  # how often we report progress
"""
how many solution attempts do you want?  More than 1 enables you to
eyeball the output and pick the best.  If you are getting stuck in
local optima, this good to try."""
REPEAT_COUNT = 1
"""start temperature -- probably leave intact"""
INITIAL_TEMPERATURE = 1

"""
how many times do we cool -- make higher to improve quality, lower to
speed the program up.  Move in tandem with the COOLING_FRACTION """
COOLING_STEPS = 500
"""
how much to cool each time -- make higher to improve quality, lower to
speed the program up. """
COOLING_FRACTION = 0.97

"""
lower makes it faster, higher makes it potentially better.
"""
STEPS_PER_TEMP = 1000

""" number e -- probably leave intact"""
E = 2.718

"""
problem specific Boltzman's constant May have to adjust if your global
value function changes the sizes of the numbers it produces.  It is
important that jumps seem random at the begining of the run, and rare
at the end of a run, and this is a knob to tweak that.
"""
K = 0.01


class Annealing:
    def __init__(self):
        self.solution_count = 0  # how many solutions evaluated

    def solution_count_update(self, s: TspSolution, t: TspInstance) -> None:
        self.solution_count += 1
        if self.solution_count % PRINT_FREQUENCY == 0:
            print("%d %7.1f" % (self.solution_count, solution_cost(s, t)))

    def random_sampling(self, t: TspInstance, nsamples: int) -> TspSolution:
        """
        Use random sampling to provide a heuristic solution to a given
        optimization problem.

        :param t: solution instance.
        :param nsamples:
        :return:
        """
        s = TspSolution.initialize(t.n)
        best_cost = solution_cost(s, t)
        bestsol = copy.copy(s)

        for i in range(1, nsamples + 1):
            s.random_solution()
            cost_now = solution_cost(s, t)
            if cost_now < best_cost:
                best_cost = cost_now
                bestsol = copy.copy(s)
            self.solution_count_update(s, t)

        return bestsol

    def hill_climbing(self, t: TspInstance) -> TspSolution:
        """
        Use hill climbing to provide a heuristic solution to a given
        optimization problem

        :param t:
        :return:
        """
        s = TspSolution.initialize(t.n)
        s.random_solution()
        cost = solution_cost(s, t)

        stuck = False
        while not stuck:
            stuck = True
            for i in range(t.n):
                for j in range(i + 1, t.n + 1):
                    delta = transition(s, t, i, j)
                    if delta < 0:
                        stuck = False
                        cost += delta
                    else:
                        transition(s, t, j, i)
                    self.solution_count_update(s, t)

        return s

    def repeated_hill_climbing(self, t: TspInstance, nsamples: int) -> TspSolution:
        s = TspSolution.initialize(t.n)
        best_cost = solution_cost(s, t)
        bestsol = copy.copy(s)

        for i in range(nsamples + 1):
            self.hill_climbing(t, s)
            cost_now = solution_cost(s, t)
            if cost_now < best_cost:
                best_cost = cost_now
                bestsol = copy.copy(s)

        return bestsol

    def anneal(self, t: TspInstance) -> TspSolution:
        """These routines implement simulated annealing.  Pairs of components
        of the same type will be swapped at random, and the new arrangment
        accepted either if (1) it is an improvement, or (2) the penalty is
        less than a random number, which is a function of the temperature
        of the system.

        We are seeking to *minimize* the current_value."""

        temperature = INITIAL_TEMPERATURE  # the current system temp
        s = TspSolution.initialize(t.n)
        current_value = solution_cost(s, t)  # value of current stat

        for i in range(1, COOLING_STEPS + 1):
            temperature *= COOLING_FRACTION
            start_value = current_value  # value at start of loop

            for j in range(1, STEPS_PER_TEMP + 1):
                # pick indices of elements to swap
                i1 = random.randint(1, t.n)
                i2 = random.randint(1, t.n)

                delta = transition(s, t, i1, i2)
                flip = random.uniform(0.0, 1.0)
                # exponent for energy funct
                exponent = (-delta / current_value) / (K * temperature)
                merit = pow(E, exponent)

                if delta < 0:  # ACCEPT-WIN
                    current_value += delta

                    if TRACE_OUTPUT:
                        print("swap WIN %d--%d value %f  temp=%f i=%d j=%d" %
                              (i1, i2, current_value, temperature, i, j))
                else:
                    if merit > flip:  # ACCEPT-LOSS
                        current_value += delta

                        if TRACE_OUTPUT:
                            print("swap LOSS %d--%d value %f merit=%f flip=%f i=%d j=%d" %
                                  (i1, i2, current_value, merit, flip, i, j))
                    else:  # REJECT
                        transition(s, t, i1, i2)

                self.solution_count_update(s, t)

            if (current_value - start_value) < 0.0:  # rerun at this temp
                temperature /= COOLING_FRACTION
                if TRACE_OUTPUT:
                    print("rerun at temperature %f" % temperature)

        return s

    def repeated_annealing(self, t: TspInstance, nsamples: int) -> TspSolution:
        s = TspSolution.initialize(t.n)
        best_cost = solution_cost(s, t)
        bestsol = copy.copy(s)

        for i in range(1, nsamples + 1):
            s = self.anneal(t)
            cost_now = solution_cost(s, t)
            if cost_now < best_cost:
                best_cost = cost_now
                bestsol = copy.copy(s)

        return bestsol
