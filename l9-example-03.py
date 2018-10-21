import numpy as np
import timeit

def det_gau(A):
    
    tmp = A.copy()
    
    for i in range(A.shape[0]):
        for j in range(i+1,A.shape[0]):
            scale = tmp[j,i]/tmp[i,i]
            tmp[j,:] -= tmp[i,:]*scale

    det = 1.
    for i in range(A.shape[0]):
        det *= tmp[i,i]
        
    return det
         
def speed_test(n):
    A = np.random.rand(n**2).reshape((n,n))
    print '|A('+str(n)+'x'+str(n)+')| =',det_gau(A)

for n in range(11)+[30,100,300,1000]:
    t = timeit.timeit('speed_test('+str(n)+')',
    'from __main__ import speed_test',number=1)
    print '%.6f sec.\n' % t
