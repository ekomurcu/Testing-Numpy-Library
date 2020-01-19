import numpy as np
import unittest
class TestSearch(unittest.TestCase):
    def setUp(self):
        self.array2D = np.array([[1,15,10],[21,28,23]])
    	
    def test2DSearch(self):
        # Testing functions argmax, argmin and where for a two
        # dimensional array containing integers
        self.arrayMax = np.argmax(self.array2D)
        self.assertEquals((self.arrayMax), 4)
        self.arrayMin = np.argmin(self.array2D)
        self.assertEquals((self.arrayMin), 0)
        self.numEq15 = np.where(self.array2D==15)
        indices = list(zip(self.numEq15[0], self.numEq15[1]))
        self.assertEquals(indices,[(0,1)])
        self.valLes12 = np.where(self.array2D<12)
        indices2 = list(zip(self.valLes12[0], self.valLes12[1]))
        self.assertEquals(indices2,[(0,0),(0,2)])


if __name__=='__main__':
        unittest.main()
