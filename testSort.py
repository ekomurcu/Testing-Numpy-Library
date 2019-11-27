import numpy as np
import unittest
class TestSort(unittest.TestCase):
        def setUp(self):
                self.intArr=np.array([[5,-2],[8,-1],[1,8],[0,-4]])
                self.resIntCol=np.array([[0,-4],[1,-2],[5, -1],[8,8]])
                self.resIntRow=np.array([[-2,5],[-1,8],[1, 8],[-4,0]])
                self.resIntFlatten=np.array([-4,-2,-1,0,1, 5,8,8])

        def testQuicksort(self):
                self.assertEqual(np.sort(self.intArr,kind='quicksort',axis=0),self.resIntCol)
                self.assertEqual(np.sort(self.intArr,kind='quicksort',axis=1),self.resIntRow)
                self.assertEqual(np.sort(self.intArr,kind='quicksort',axis=None),self.resIntFlatten)
if __name__=='__main__':
        unittest.main()
