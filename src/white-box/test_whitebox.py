import coverage

cov = coverage.Coverage()
cov.start()

# .. call your code ..

import numpy as np
import whitebox as w
#polyval(input,constants)
Alist= list([1,2,3])


print(w.polyval(np.nan,np.nan))#%69
print(w.polyval(2,np.nan))#%69
print(w.polyval(Alist,np.nan))#%77

print(w.polyval(5,5))#%85
print(w.polyval(5,Alist))#%92

print(w.polyval(list([5,4]),Alist))#%92
print(w.polyval(np.array([[5,5], [5,5]]),Alist))#%100

cov.stop()
cov.save()

cov.html_report()