import numpy as np
import timeit

def det_rec(A):

    if A.shape==(2,2): return A[0,0]*A[1,1]-A[0,1]*A[1,0]
    
    det = 0.
    reduced = np.zeros((A.shape[0]-1,A.shape[1]-1))
    
    for i in range(A.shape[1]):
        reduced[:,:i] = A[1:,:i]
        reduced[:,i:] = A[1:,i+1:]
        r = A[0,i]*det_rec(reduced)
        
	if i % 2==1: det -= r
	else:        det += r
	
    return det
         
def speed_test(n):
    A = np.random.rand(n**2).reshape((n,n))
    print '|A('+str(n)+'x'+str(n)+')| =',det_rec(A)

for n in range(2,11):
    t = timeit.timeit('speed_test('+str(n)+')',
    'from __main__ import speed_test',number=1)
    print '%.6f sec.\n' % t
