import numpy as np
import unittest

class Testndarray(unittest.TestCase):
    def setUp(self):
        #A full Array of 1 element with int32 values
        self.A11int32 = np.array([11],np.int32)
        #A full Array mxn with int32 values
        self.A23int32 = np.array([[11,12,13],[21,22,23]],np.int32)
        #A full Array nxn with int32 values
        self.A44int32 = np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]],np.int32)
        #A full Array mxn with int32 values
        self.A89int32 = np.array([[11,12,13,14,15,16,17,18,19],
                                 [21,22,23,24,25,26,27,28,29],
                                 [31,32,33,34,35,36,37,38,39],
                                 [41,42,43,44,45,46,47,48,49],
                                 [51,52,53,54,55,56,57,58,59],
                                 [61,62,63,64,65,66,67,68,69],
                                 [71,72,73,74,75,76,77,78,79],
                                 [81,82,83,84,85,86,87,88,89]],np.int32)

    def test_full_1_arrays(self):
        # A11int32 = np.array([11],np.int32)
        # A full Array mxn with int32 values
        # Testing if it is as defined int32
        self.assertEqual(self.A11int32.dtype,'int32')
        # Testing if the shape is the same as intented to be
        self.assertEqual(self.A11int32.shape,(1,))
        # Checking random numbers inside the matrix
        self.assertEqual(self.A11int32[0,], 11)


    def test_full_mxn_arrays(self):
        # A23int32 = np.array([[11,12,13],[21,22,23]],np.int32)
        # Testing if it is as defined int32
        self.assertEqual(self.A23int32.dtype,'int32')
        # Testing if the shape is the same as intented to be
        self.assertEqual(self.A23int32.shape,(2, 3))
        # Checking random numbers inside the matrix
        self.assertEqual(self.A23int32[1, 2], 23)

    def test_full_nxn_arrays(self):
        # A44int32 = np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]],np.int32)
        # Testing if it is as defined int32
        self.assertEqual(self.A44int32.dtype,'int32')
        # Testing if it is as defined int32
        self.assertEqual(self.A44int32.shape,(4, 4))
        # Checking random numbers inside the matrix
        self.assertEqual(self.A44int32[3, 3], 44)

    def test_full_bigger_mxn_arrays(self):
        # A89int32
        # Testing if it is as defined int32
        self.assertEqual(self.A89int32.dtype,'int32')
        # Testing if it is as defined int32
        self.assertEqual(self.A89int32.shape,(8, 9))
        # Checking random numbers inside the matrix
        self.assertEqual(self.A89int32[4, 4], 55)

if __name__ == '__main__':
    unittest.main()
