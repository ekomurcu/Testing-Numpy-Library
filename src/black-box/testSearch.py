import numpy as np
import unittest
class TestSearch(unittest.TestCase):
    def setUp(self):
		# Working on 2D array
		self.array2D = np.array([[1,15,10],[21,28,23]])
		
		#print(self.array2D)
    	
    def test2DSearch(self):
    	
    	#argmax returns indices of max element
		self.arrayMax = np.argmax(self.array2D)
		#print(self.arrayMax)
		self.assertEquals((self.arrayMax), 4)
		
		#argmax returns indices of max element
		self.arrayMin = np.argmin(self.array2D)
		self.assertEquals((self.arrayMin), 0)

		#Finds the indices of value equals to 15 in an array
		self.numEq15 = np.where(self.array2D==15)
		#print(self.numEq15)
		#print the coordinates/ indices
		indices = list(zip(self.numEq15[0], self.numEq15[1]))
		#print(listOfCoordinates)
		self.assertEquals(indices,[(0,1)])

		#search value less than 12
		self.valLes12 = np.where(self.array2D<12)
		indices2 = list(zip(self.valLes12[0], self.valLes12[1]))
		#print(indices2)
		self.assertEquals(indices2,[(0,0),(0,2)])


if __name__=='__main__':
        unittest.main()
