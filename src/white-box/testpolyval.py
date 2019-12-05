import numpy as np

print('(3x^2 + 2x + 1)(2)= ' + str(np.polyval(2,[1, 2, 3])))
#prints (3x^2 + 2x + 1)(2)= 17

A23 = np.array([[11,12,13],[21,22,23]],np.int32)



print(np.polyval(A23,A23))
