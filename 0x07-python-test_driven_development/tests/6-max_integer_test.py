#!/usr/bin/python3
""" Unittest for max_integer([..]) """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_val_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_val_mid(self):
        self.assertEqual(max_integer([2, 4, 1, 7, 6]), 7)

    def test_max_val_first(self):
        self.assertEqual(max_integer([9, 7, 4, 6, 8]), 9)

    def test_one_arg_pos(self):
        self.assertEqual(max_integer([5]), 5)

    def test_one_arg_neg(self):
        self.assertEqual(max_integer([-7]), -7)

    def test_one_arg_none(self):
        self.assertEqual(max_integer([]), None)

    def test_only_neg(self):
        self.assertEqual(max_integer([-1, -14, -56, -9, -86, -65]), -1)

    def test_float(self):
        self.assertEqual(max_integer([5.7, 6.8, 8.2, 8.3]), 8.3)

    def test_TE_no_args(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            max_integer(['g', 6, 9])

if __name__ == '__main__':
    unittest.main()
