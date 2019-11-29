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

        #A full Array of 1 element with float32 values
        self.A11float32 = np.array([11.11],np.float32)
        #A full Array mxn with float32 values
        self.A23float32 = np.array([[11.11,12.12,13.13],[21.21,22.22,23.23]],np.float32)
        #A full Array nxn with float32 values
        self.A44float32 = np.array([[11.11,12.12,13.13,14.14],[21.21,22.22,23.23,24.24],[31.31,32.32,33.33,34.34],[41.41,42.42,43.43,44.44]],np.float32)
        #A full Array mxn with float32 values
        self.A89float32 = np.array([[11.11,12.12,13.13,14.14,15.15,16.16,17.17,18.18,19.19],
                                    [21.21,22.22,23.23,24.24,25.25,26.26,27.27,28.28,29.29],
                                    [31.31,32.32,33.33,34.34,35.35,36.36,37.37,38.38,39.39],
                                    [41.41,42.42,43.43,44.44,45.45,46.46,47.47,48.48,49.49],
                                    [51.51,52.52,53.53,54.54,55.55,56.56,57.57,58.58,59.59],
                                    [61.61,62.62,63.63,64.64,65.65,66.66,67.67,68.68,69.69],
                                    [71.71,72.72,73.73,74.74,75.75,76.76,77.77,78.78,79.79],
                                    [81.81,82.82,83.83,84.84,85.86,86.86,87.87,88.88,89.89]],np.float32)

    #Test int32
    def tesFull1x1ArraysInt32(self):
        # A11int32
        # A full Array mxn with int32 values
        # Testing if it is as defined int32
        self.assertEqual(self.A11int32.dtype,'int32')
        # Testing if the shape is the same as intented to be
        self.assertEqual(self.A11int32.shape,(1,))
        # Checking random numbers inside the matrix
        self.assertEqual(self.A11int32[0,], 11)


    def testFullmxnArraysInt32(self):
        # A23int32
        # Testing if it is as defined int32
        self.assertEqual(self.A23int32.dtype,'int32')
        # Testing if the shape is the same as intented to be
        self.assertEqual(self.A23int32.shape,(2, 3))
        # Checking random numbers inside the matrix
        self.assertEqual(self.A23int32[1, 2], 23)

    def testFullnxnArraysInt32(self):
        # A44int32
        # Testing if it is as defined int32
        self.assertEqual(self.A44int32.dtype,'int32')
        # Testing if it is as defined int32
        self.assertEqual(self.A44int32.shape,(4, 4))
        # Checking random numbers inside the matrix
        self.assertEqual(self.A44int32[3, 3], 44)

    def testFullBiggermxnArraysInt32(self):
        # A89int32
        # Testing if it is as defined int32
        self.assertEqual(self.A89int32.dtype,'int32')
        # Testing if it is as defined int32
        self.assertEqual(self.A89int32.shape,(8, 9))
        # Checking random numbers inside the matrix
        self.assertEqual(self.A89int32[4, 4], 55)

    #Test float32
    def tesFull1x1ArraysFloat32(self):
        # A11float32
        # A full Array mxn with int32 values
        # Testing if it is as defined int32
        self.assertEqual(self.A11float32.dtype,'float32')
        # Testing if the shape is the same as intented to be
        self.assertEqual(self.A11float32.shape,(1,))
        # Checking random numbers inside the matrix
        self.assertAlmostEqual(self.A11float32[0,], 11.11, places=2)


    def testFullmxnArraysFloatt32(self):
        # A23float32
        # Testing if it is as defined int32
        self.assertEqual(self.A23float32.dtype,'float32')
        # Testing if the shape is the same as intented to be
        self.assertEqual(self.A23float32.shape,(2, 3))
        # Checking random numbers inside the matrix
        self.assertAlmostEqual(self.A23float32[1, 2], 23.23, places=2)

    def testFullnxnArraysFloat32(self):
        # A44float32
        # Testing if it is as defined int32
        self.assertEqual(self.A44float32.dtype,'float32')
        # Testing if it is as defined int32
        self.assertEqual(self.A44float32.shape,(4, 4))
        # Checking random numbers inside the matrix
        self.assertAlmostEqual(self.A44float32[1, 2], 23.23, places=2)

    def testFullBiggermxnArraysFloat32(self):
        # A89float32
        # Testing if it is as defined int32
        self.assertEqual(self.A89float32.dtype,'float32')
        # Testing if it is as defined int32
        self.assertEqual(self.A89float32.shape,(8, 9))
        # Checking random numbers inside the matrix
        self.assertAlmostEqual(self.A89float32[4, 4], 55.55, places=2)

if __name__ == '__main__':
    unittest.main()
