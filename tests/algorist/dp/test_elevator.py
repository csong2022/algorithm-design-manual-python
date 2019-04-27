from unittest import TestCase

from algorist.dp.elevator import MAX_RIDERS, Elevator
from tests.algorist.test.test_engine import execute


class TestElevator(TestCase):
    def process(self, input):
        nriders, nstops = list(map(int, input.readline().split()))
        stops = [0] * MAX_RIDERS

        for i in range(1, nriders + 1):
            stops[i] = int(input.readline()[:-1])

        elevator = Elevator(stops, nstops)

        for i in range(1, nriders + 1):
            print("%d" % stops[i])

        laststop = elevator.optimize_floors()

        elevator.print_matrix(elevator.m)
        print()
        elevator.print_matrix(elevator.p)

        print("cost = %d" % elevator.m[laststop][nstops])
        elevator.reconstruct_path(laststop, nstops)

    def test(self):
        execute(self, "elevator-in", "elevator-out")
