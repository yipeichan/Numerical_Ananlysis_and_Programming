import numpy as np
import scipy.linalg as linalg
    
A = np.random.rand(9).reshape((3,3))
b = np.random.rand(3).reshape((3,1))

x = linalg.solve(A,b)

print 'Matrix A =\n',A
print 'Matrix b =\n',b
print 'Matrix x =\n',x
print 'Ax-b =\n',A.dot(x)-b