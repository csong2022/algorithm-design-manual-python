from unittest import TestCase

from algorist.dp.partition import read_partition, partition
from tests.algorist.test.test_engine import execute


class TestPartition(TestCase):
    def process(self, input):
        s, n, k = read_partition(input)
        partition(s, n, k)

    def test_data1(self):
        execute(self, "partition-data1", "partition-data1-out")

    def test_data2(self):
        execute(self, "partition-data2", "partition-data2-out")
