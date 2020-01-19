import unittest
import numpy as np
import math


# Test suite for the amax function of the statistics module
class TestAMax(unittest.TestCase):
    # Test that amax throws an exception if we try to get the minimum value of empty input
    def test_empty_input(self):
        with self.assertRaises(ValueError) as context:
            np.amax([])

        self.assertTrue('zero-size array' in str(context.exception))

    # Test that amax can handle infinity inputs
    def test_infinity_input(self):
        self.assertEqual(np.amax([
            math.inf,
            -math.inf
        ]), math.inf)

    # Test that amax can handle simple one dimension positive values
    def test_one_dimension_positive(self):
        self.assertEqual(np.amax(range(1000, 0, -1)), 1000)
        self.assertEqual(np.amax(range(20, 10, -1)), 20)

    # Test that amax can handle simple one dimension negative values
    def test_one_dimension_negative(self):
        self.assertEqual(np.amax(range(-1000, 0)), -1)
        self.assertEqual(np.amax(range(-1000, 1)), 0)

    # Test that amax can handle two dimensional positive values
    def test_two_dimension_positive(self):
        self.assertEqual(np.amax([
            range(10, 0, -1),
            range(20, 10, -1)
        ]), 20)

    # Test that amax can handle two dimensional negative values
    def test_two_dimension_negative(self):
        self.assertEqual(np.amax([
            range(0, -10, -1),
            range(-10, -20, -1)
        ]), 0)

    # Test that amax can handle imaginary input values
    def test_one_dimension_imaginary(self):
        self.assertEqual(np.amax([
            1j,
            2j,
            3j
        ]), 3j)

    # Test that amax can handle complex input values
    def test_one_dimension_complex(self):
        self.assertEqual(np.amax([
            1j + 4,
            2j + 3,
            3j + 1
        ]), 1j + 4)

    # Test that amax can handle a mix of complex and non complex values
    def test_one_dimension_complex_non_complex_mix(self):
        self.assertEqual(np.amax([
            1j + 4,
            2j + 3,
            3j + 1,
            1
        ]), 1j + 4)


if __name__ == '__main__':
    unittest.main()
