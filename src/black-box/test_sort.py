import numpy as np
import unittest
class TestSort(unittest.TestCase):
    #setting up the variables including the 1d input vector, 2d input vectors
    #and the outputs of sort() function for different types of 2d vectors.
    def setUp(self):
        self.sort_type=['quicksort', 'mergesort', 'heapsort', 'stable']
        self.int_1D_arr=np.array([-2,2.6, -12, -8.9,0])
        self.int_2D_arr=np.array([[5,-2],[8,-1],[1,8],[0,-4]])
        self.res_int_2D_col=np.array([[0,-4],[1,-2],[5, -1],[8,8]])
        self.res_int_2D_row=np.array([[-2,5],[-1,8],[1, 8],[-4,0]])
        self.res_int_2D_flatten=np.array([-4,-2,-1,0,1,5,8,8])
    #perform blackbox testing for 1D array.
    def test_int_1D_sort(self):
        for srt in self.sort_type:
            self.assertTrue((np.sort(self.int_1D_arr,kind=srt,axis=None)==np.array([-12, -8.9,-2.,0.,2.6])).all())
    #perform blackbox testing for 2D array to sort according to columnwise, rowwise and flatten.
    def test_int_2D_sort(self):
        for srt in self.sort_type:
            self.assertTrue((np.sort(self.int_2D_arr,kind=srt,axis=0)==self.res_int_2D_col).all())
            self.assertTrue((np.sort(self.int_2D_arr,kind=srt,axis=-1)==self.res_int_2D_row).all())
            self.assertTrue((np.sort(self.int_2D_arr,kind=srt,axis=None)==self.res_int_2D_flatten).all())

if __name__=='__main__':
        unittest.main()
