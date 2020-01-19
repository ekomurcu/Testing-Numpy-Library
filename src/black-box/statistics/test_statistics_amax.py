import unittest
import numpy as np
import math


class TestAMax(unittest.TestCase):
    def test_empty_input(self):
        with self.assertRaises(ValueError) as context:
            np.amin([])

        self.assertTrue('zero-size array' in str(context.exception))

    def test_infinity_input(self):
        self.assertEqual(np.amax([
            math.inf,
            -math.inf
        ]), math.inf)

    def test_one_dimension_positive(self):
        self.assertEqual(np.amax(range(1000, 0, -1)), 1000)
        self.assertEqual(np.amax(range(20, 10, -1)), 20)

    def test_one_dimension_negative(self):
        self.assertEqual(np.amax(range(-1000, 0)), -1)
        self.assertEqual(np.amax(range(-1000, 1)), 0)

    def test_two_dimension_positive(self):
        self.assertEqual(np.amax([
            range(10, 0, -1),
            range(20, 10, -1)
        ]), 20)

    def test_two_dimension_negative(self):
        self.assertEqual(np.amax([
            range(0, -10, -1),
            range(-10, -20, -1)
        ]), 0)

    def test_one_dimension_imaginary(self):
        self.assertEqual(np.amax([
            1j,
            2j,
            3j
        ]), 3j)

    def test_one_dimension_complex(self):
        self.assertEqual(np.amax([
            1j + 4,
            2j + 3,
            3j + 1
        ]), 1j + 4)

    def test_one_dimension_complex_non_complex_mix(self):
        self.assertEqual(np.amax([
            1j + 4,
            2j + 3,
            3j + 1,
            1
        ]), 1j + 4)


if __name__ == '__main__':
    unittest.main()
