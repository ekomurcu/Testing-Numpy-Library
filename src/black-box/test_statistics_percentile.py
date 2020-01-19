import unittest
import numpy as np

# Test suite for the percentile function of the statistics module
class TestPercentile(unittest.TestCase):
    # Test that it works with zero as input
    def test_zero(self):
        self.assertEqual(np.percentile([0, 0, 0, 0], 0), 0)
        self.assertEqual(np.percentile([0, 0, 0, 0], 50), 0)
        self.assertEqual(np.percentile([0, 0, 0, 0], 100), 0)

    # Test that the trivial input of 0 and 1 works
    def test_simple_values(self):
        self.assertEqual(np.percentile([0, 1, 1, 0], 100), 1)
        self.assertEqual(np.percentile([0, 1, 1, 0], 50), .5)
        self.assertEqual(np.percentile([0, 1, 1, 0], 25), 0)

    # Test that we get expected values with the range [-10, 0]
    def test_negative_values(self):
        self.assertEqual(np.percentile(range(-10, 1), 100), 0)
        self.assertEqual(np.percentile(range(-10, 1), 50), -5)
        self.assertEqual(np.percentile(range(-10, 1), 0), -10)

    # Test that two dimensions work with some arbitrary positive values
    def test_two_dim_positive(self):
        a = [[10, 7, 4], [3, 2, 1]]
        self.assertEqual(np.percentile(a, 50), 3.5)
        self.assertEqual(np.percentile(a, 25), 2.25)

    # Test that two dimensions work with some arbitrary negative values
    def test_two_dim_negative(self):
        a = [[-10, -7, -4], [-3, -2, -1]]
        self.assertEqual(np.percentile(a, 50), -3.5)
        self.assertEqual(np.percentile(a, 25), -6.25)

    # Test a larger range of negative values
    def test_lower(self):
        for i in range(0, -1000):
            self.assertEqual(np.percentile(list(range(0, i + 1, -1)),0), 0)

    # Test a larger range of positive values
    def test_upper(self):
        for i in range(0, 1000):
            self.assertEqual(np.percentile(list(range(0, i + 1)), 100), i)

    # Test that we always get the median back with the 50-th percentile
    def test_median(self):
        for i in range(0, 1000):
            a = list(range(0, i + 1))
            self.assertEqual(np.percentile(a, 50), np.median(a))


if __name__ == '__main__':
    unittest.main()
