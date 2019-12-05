import coverage

cov = coverage.Coverage()
cov.start()

# .. call your code ..

import numpy as np
import whitebox as w
#polyval(input,constants)
Alist= list([1,2,3])
w.polyval(np.nan,np.nan)#%69
w.polyval(2,np.nan)#%69
w.polyval(Alist,np.nan)#%77

w.polyval(5,5)#%85
print(w.polyval(2,Alist))#%92  

w.polyval(list([5,4]),Alist)#%92
w.polyval(np.array([[5,5], [5,5]]),Alist)#%100

cov.stop()
cov.save()

cov.html_report()
