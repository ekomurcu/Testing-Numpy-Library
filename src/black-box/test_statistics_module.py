import unittest
import numpy as np
import math


class TestAMin(unittest.TestCase):
    def test_empty_input(self):
        with self.assertRaises(ValueError) as context:
            np.amin([])

        self.assertTrue('zero-size array' in str(context.exception))

    def test_infinity_input(self):
        self.assertEqual(np.amin([
            math.inf,
            -math.inf
        ]), -math.inf)

    def test_single_dimension_positive(self):
        self.assertEqual(np.amin(range(1000)), 0)
        self.assertEqual(np.amin(range(10, 20)), 10)

    def test_single_dimension_negative(self):
        self.assertEqual(np.amin(range(-1000, -1)), -1000)
        self.assertEqual(np.amin(range(-1000, 0)), -1000)


if __name__ == '__main__':
    unittest.main()
