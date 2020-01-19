import unittest
import numpy as np


class TestPercentile(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(np.percentile([0, 0, 0, 0], 0), 0)
        self.assertEqual(np.percentile([0, 0, 0, 0], 50), 0)
        self.assertEqual(np.percentile([0, 0, 0, 0], 100), 0)

    def test_simple_values(self):
        self.assertEqual(np.percentile([0, 1, 1, 0], 100), 1)
        self.assertEqual(np.percentile([0, 1, 1, 0], 50), .5)
        self.assertEqual(np.percentile([0, 1, 1, 0], 25), 0)

    def test_negative_values(self):
        self.assertEqual(np.percentile(range(-10, 1), 100), 0)
        self.assertEqual(np.percentile(range(-10, 1), 50), -5)
        self.assertEqual(np.percentile(range(-10, 1), 0), -10)

    def test_two_dim_positive(self):
        a = [[10, 7, 4], [3, 2, 1]]
        self.assertEqual(np.percentile(a, 50), 3.5)
        self.assertEqual(np.percentile(a, 25), 2.25)

    def test_two_dim_negative(self):
        a = [[-10, -7, -4], [-3, -2, -1]]
        self.assertEqual(np.percentile(a, 50), -3.5)
        self.assertEqual(np.percentile(a, 25), -6.25)

    def test_lower(self):
        for i in range(0, -1000):
            self.assertEqual(np.percentile(list(range(0, i + 1, -1)), 100), i)

    def test_upper(self):
        for i in range(0, 1000):
            self.assertEqual(np.percentile(list(range(0, i + 1)), 100), i)

    def test_median(self):
        for i in range(0, 1000):
            a = list(range(0, i + 1))
            self.assertEqual(np.percentile(a, 50), np.median(a))


if __name__ == '__main__':
    unittest.main()
