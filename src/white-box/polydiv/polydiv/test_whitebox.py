import coverage
import numpy as np
import whitebox as w

#polyval(input,constants)
Alist= list([1,2,3])
Blist= list([4,5,6])
cov = coverage.Coverage()

cov.start()

#w.polydiv(np.nan,np.nan)#%69

w.polydiv(list([5,4]),Alist)#%92
w.polydiv(np.array([[5,5], [5,5]]),Alist)#%100
cov.stop()
cov.save()
cov.html_report()

#w.polydiv(2,np.nan)#%69
#w.polydiv(Alist,np.nan)#%77

#w.polydiv(5,5)#%85
#print(w.polydiv(2,Alist))#%92  

w.polydiv(list([5,4]),Alist)#%92
w.polydiv(np.array([[5,5], [5,5]]),Alist)#%100


