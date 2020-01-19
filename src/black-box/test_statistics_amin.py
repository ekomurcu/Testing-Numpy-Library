import unittest
import numpy as np
import math


# Test suite for the amin function of the statistics module
class TestAMin(unittest.TestCase):
    # Test that amin throws an exception if we try to get the minimum value of empty input
    def test_empty_input(self):
        with self.assertRaises(ValueError) as context:
            np.amin([])

        self.assertTrue('zero-size array' in str(context.exception))

    # Test that amin can handle infinity inputs
    def test_infinity_input(self):
        self.assertEqual(np.amin([
            math.inf,
            -math.inf
        ]), -math.inf)

    # Test that amin can handle simple one dimension positive values
    def test_one_dimension_positive(self):
        self.assertEqual(np.amin(range(1000)), 0)
        self.assertEqual(np.amin(range(10, 20)), 10)

    # Test that amin can handle simple one dimension negative values
    def test_one_dimension_negative(self):
        self.assertEqual(np.amin(range(-1000, -1)), -1000)
        self.assertEqual(np.amin(range(-1000, 0)), -1000)

    # Test that amin can handle two dimensional positive values
    def test_two_dimension_positive(self):
        self.assertEqual(np.amin([
            range(0, 10),
            range(10, 20)
        ]), 0)

    # Test that amin can handle two dimensional negative values
    def test_two_dimension_negative(self):
        self.assertEqual(np.amin([
            range(-10, 0),
            range(-20, -10)
        ]), -20)

    # Test that amin can handle imaginary input values
    def test_one_dimension_imaginary(self):
        self.assertEqual(np.amin([
            1j,
            2j,
            3j
        ]), 1j)

    # Test that amin can handle complex input values
    def test_one_dimension_complex(self):
        self.assertEqual(np.amin([
            1j + 4,
            2j + 3,
            3j + 1
        ]), 3j + 1)

    # Test that amin can handle a mix of complex and non complex values
    def test_one_dimension_complex_non_complex_mix(self):
        self.assertEqual(np.amin([
            1j + 4,
            2j + 3,
            3j + 1,
            1
        ]), 1)


if __name__ == '__main__':
    unittest.main()
