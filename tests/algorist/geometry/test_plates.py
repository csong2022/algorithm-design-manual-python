from math import floor
from unittest import TestCase

from algorist.geometry.plates import dense_plates, grid_plates, dense_layers, plates_on_top
from tests.algorist.test.test_engine import execute


class TestPlates(TestCase):

    def process(self, input):
        print("input box width, box length, and plate radius:")
        w, l, r = list(map(float, input.readline().split()))
        print("box width=%lf, box length=%lf, and plate radius=%lf:" % (w, l, r))

        print("dense packing = %d" % dense_plates(w, l, r))
        print("grid packing = %d" % grid_plates(w, l, r))

        xmax = floor(w / (2 * r))
        ymax = dense_layers(w, l, r)

        for i in range(xmax):
            print("(0,%d) has %d on top." % (i, plates_on_top(0, i, w, l, r)))

    def test_plates1(self):
        execute(self, "plates1-in", "plates1-out")

    def test_plates2(self):
        execute(self, "plates2-in", "plates2-out")

    def test_plates3(self):
        execute(self, "plates3-in", "plates3-out")