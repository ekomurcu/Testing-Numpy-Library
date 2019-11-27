import numpy as np
import unittest


class TestDet(unittest.TestCase):
    def test_det(self):
        array_1 = np.array([[3, 5], [9, 6]])
        array_2 = np.ones((3,3))
        array_3 = np.array([[0.4, 5.6, 1.0], [10.3, 17.23, 0.0], [4.3, 71.0, 22.91]])
        self.assertEqual(np.linalg.det(array_1), -27)
        self.assertEqual(np.linalg.det(array_2), 0)
        self.assertAlmostEqual(np.linalg.det(array_3), -506.34208)

    def test_det_exception_when_invalid_input(self):
        array_int = np.array([[9, 4], [3, 10], [16, 1]])
        array_char = np.array([['a', 'a'], ['a', 'a']])
        self.assertRaises(Exception, np.linalg.det, array_int)
        self.assertRaises(Exception, np.linalg.det, array_char)


class TestDot(unittest.TestCase):
    def test_dot(self):
        array_int_1 = [3, 4, 17, -2]
        array_int_2 = [1, 5, -9, 7]
        array_int_3 = [2, 4]
        array_double = [0.54, 13.5, 7.1, -3.3]
        matrix_1 = [[8, 14], [-11, 5]]
        matrix_2 = [[3, 15], [21, 1]]
        scalar_1 = 4
        scalar_2 = -6
        self.assertEqual(np.dot(array_int_1, array_int_2), -144)
        self.assertAlmostEqual(np.dot(array_int_1, array_double), 182.9200)
        self.assertTrue((np.dot(matrix_1, matrix_2) == np.array([[318, 134], [72, -160]])).all())
        self.assertTrue((np.dot(matrix_1, array_int_3) == np.array([72, -2])).all())
        self.assertTrue((np.dot(array_int_1, scalar_1) == np.array([12, 16, 68, -8])).all())
        self.assertEqual(np.dot(scalar_1, scalar_2), -24)

    def test_dot_exception_when_invalid_input(self):
        array_1 = [3, 17, 9]
        array_2 = [[8, 14], [-11, 5]]
        array_char = ['a', 'a', 'a']
        self.assertRaises(Exception, np.dot, array_char, array_char)
        self.assertRaises(Exception, np.dot, array_1, array_2)





if __name__ == "__main__":
    unittest.main()
