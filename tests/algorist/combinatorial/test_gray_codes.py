from unittest import TestCase

from algorist.combinatorial.gray_codes import generate_gray_codes


class TestGrayCodes(TestCase):
    def test_1_bit(self):
        gray_codes = generate_gray_codes(1)
        self.assertEqual(gray_codes, ["0", "1"])

    def test_2_bits(self):
        gray_codes = generate_gray_codes(2)
        self.assertEqual(gray_codes, ["00", "01", "11", "10"])

    def test_3_bits(self):
        gray_codes = generate_gray_codes(3)
        self.assertEqual(gray_codes, ["000", "001", "011", "010",
                                      "110", "111", "101", "100"])
    def test_4_bits(self):
        gray_codes = generate_gray_codes(4)
        self.assertEqual(gray_codes, ["0000", "0001", "0011", "0010", "0110", "0111", "0101", "0100",
                                      "1100", "1101", "1111", "1110", "1010", "1011", "1001", "1000"])