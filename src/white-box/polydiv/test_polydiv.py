import unittest
from polydiv import polydiv


class TestPolydiv(unittest.TestCase):
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            polydiv([3, 2, 1], [0])


if __name__ == '__main__':
    unittest.main()

