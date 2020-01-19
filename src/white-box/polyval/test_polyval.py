import coverage

cov = coverage.Coverage()
cov.start()

# .. call your code ..

import numpy as np
import polyval as p
#polyval(input,constants)

#Statement and Branch Coverage
Alist= list([1,2])
w.polyval(np.nan,np.nan)#%69
w.polyval(2,np.nan)#%69
w.polyval(Alist,np.nan)#%77

w.polyval(5,5)#%85
print(w.polyval(2,Alist))#%92

w.polyval(list([5,4]),Alist)#%92
w.polyval(np.array([[5,5], [5,5]]),Alist)#%100

#Path Coverage
Alist= list([1])
w.polyval(list([5,4]),Alist)
w.polyval(np.array([[5,5], [5,5]]),Alist)
#loop none , %92

Alist= list([1,2])
w.polyval(list([5,4]),Alist)
w.polyval(np.array([[5,5], [5,5]]),Alist)
#loop once , %100

Alist= list([1,2,3])
w.polyval(list([5,4]),Alist)
w.polyval(np.array([[5,5], [5,5]]),Alist)
#loop twice, %100

cov.stop()
cov.save()

cov.html_report()
