import numpy as np
import unittest
class TestSort(unittest.TestCase):
    def setUp(self):
        self.sortType=['quicksort', 'mergesort', 'heapsort', 'stable']
        self.intArr=np.array([[5,-2],[8,-1],[1,8],[0,-4]])
        self.resIntCol=np.array([[0,-4],[1,-2],[5, -1],[8,8]])
        self.resIntRow=np.array([[-2,5],[-1,8],[1, 8],[-4,0]])
        self.resIntFlatten=np.array([-4,-2,-1,0,1,5,8,8])

    def testInt2Dsort(self):
        for srt in self.sortType:
            self.assertTrue((np.sort(self.intArr,kind=srt,axis=0)==self.resIntCol).all())
            self.assertTrue((np.sort(self.intArr,kind=srt,axis=-1)==self.resIntRow).all())
            self.assertTrue((np.sort(self.intArr,kind=srt,axis=None)==self.resIntFlatten).all())
if __name__=='__main__':
        unittest.main()
