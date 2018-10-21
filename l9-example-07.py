import numpy as np
import scipy.linalg as linalg

def solve_gau2(A,b):
    
    tmp = A.copy()
    out = b.copy()
	
    for i in range(A.shape[0]):
        for j in range(i+1,A.shape[0]):
            
            scale = tmp[j,i]/tmp[i,i]
            tmp[j,:] -= tmp[i,:]*scale
            out[j,:] -= out[i,:]*scale
            
    for i in range(A.shape[0])[::-1]:
            for j in range(i+1,A.shape[0]):
                out[i,:] -= out[j,:]*tmp[i,j]
            out[i,:] /= tmp[i,i]
                        
    return out
    
A = np.random.rand(9).reshape((3,3))
I = np.eye(3)

Ainv = solve_gau2(A,I)

print 'Matrix A =\n',A
print 'Matrix A^-1 =\n',Ainv
print 'A*A^-1 =\n',A.dot(Ainv)

Ainv2 = linalg.inv(A)

print 'A*A^-1 [calculated by linalg.inv()] =\n',A.dot(Ainv2)
