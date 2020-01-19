import numpy as np
import unittest
from polyval import polyval


class TestPolyval(unittest.TestCase):
    def setUp(self):
        self.a = [1, 2]

    def test_nan(self):
        #checking for na values
        self.assertTrue(np.isnan(polyval(np.nan, np.nan)))
        self.assertTrue(np.isnan(polyval(2, np.nan)))
        self.assertTrue(np.isnan(polyval(self.a, np.nan))[0] and np.isnan(polyval(self.a, np.nan))[1])

    def test_full_coverage(self):
        self.assertEqual(polyval(5, 5), 5)
        self.assertEqual(polyval(2, self.a), 5)

        r1 = polyval([5, 4], self.a)
        self.assertEqual(r1[0], 11)
        self.assertEqual(r1[1], 9)

        r2 = polyval([[5, 5], [5, 5]], self.a)
        self.assertTrue(r2[0][0] == r2[0][1] == r2[1][0] == r2[1][1] == 11)

        # Path Coverage
        # loop none
        b = [1]
        r3 = polyval([5, 4], b)
        self.assertEqual(r3[0], 1)
        self.assertEqual(r3[1], 1)

        r4 = polyval([[5, 5], [5, 5]], b)
        self.assertTrue(r4[0][0] == r4[0][1] == r4[1][0] == r4[1][1] == 1)


        # loop once
        c = [1, 2]

        r5 = polyval([5, 4], c)
        self.assertEqual(r5[0], 11)
        self.assertEqual(r5[1], 9)

        r6 = polyval([[5, 5], [5, 5]], c)
        self.assertTrue(r6[0][0] == r6[0][1] == r6[1][0] == r6[1][1] == 11)

        # loop twice
        d = [1, 2, 3]

        r7 = polyval([5, 4], d)
        self.assertEqual(r7[0], 86)
        self.assertEqual(r7[1], 57)

        r8 = polyval([[5, 5], [5, 5]], d)
        self.assertTrue(r8[0][0] == r8[0][1] == r8[1][0] == r8[1][1] == 86)


if __name__ == '__main__':
    unittest.main()
