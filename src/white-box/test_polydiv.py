import unittest
from polydiv import polydiv


class TestPolydiv(unittest.TestCase):
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            polydiv([3, 2, 1], [0])

    def test_case_1_and_2(self):
        c1 = [3]
        c2 = [3, 2]
        c3 = [5]

        r1 = polydiv(c1, c2)
        self.assertEqual(r1[0][0], 0)
        self.assertEqual(r1[1][0], 3)

        r2 = polydiv(c1, c3)
        self.assertAlmostEqual(r2[0][0], 0.6)
        self.assertAlmostEqual(r2[1][0], 0)

    def test_else(self):
        c1 = [1, 2, 3]
        c2 = [3, 2, 1]

        r1 = polydiv(c1, c2)
        self.assertEqual(r1[0][0], 3)
        self.assertEqual(r1[1][0], -8)
        self.assertEqual(r1[1][1], -4)

        r2 = polydiv(c2, c1)
        self.assertAlmostEqual(r2[0][0], 1 / 3)
        self.assertAlmostEqual(r2[1][0], 8 / 3)
        self.assertAlmostEqual(r2[1][1], 4 / 3)


if __name__ == '__main__':
    unittest.main()
