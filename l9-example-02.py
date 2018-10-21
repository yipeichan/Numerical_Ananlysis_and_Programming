import numpy as np

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
   
print 'test #1 - simply check the output'
T = np.array([[1.,1.,2.],[2.,1.,1.],[1.,2.,1.]]) 
print 'T =\n',T
print '|T| =',det_rec(T)
print '-'*20

print 'test #2 - |A| = |A^T|'
A = np.random.rand(25).reshape((5,5))
print '|A| =',det_rec(A)
print '|A.T| =',det_rec(A.T)
print '-'*20

print 'test #3 - |A*B| = |A|*|B|'
B = np.random.rand(25).reshape((5,5))
print '|A*B| =',det_rec(A.dot(B))
print '|A|*|B| =',det_rec(A)*det_rec(B)
print '-'*20

print 'test #4 - |A| does not change after row operation'
print '|A| =',det_rec(A)
A[1,:] += A[0,:]*0.5
print '|A| =',det_rec(A)
print '-'*20