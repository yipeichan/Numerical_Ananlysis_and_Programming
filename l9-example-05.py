import numpy as np

def solve_LU(A,b):
    
    tmp = A.copy()
    out = b.copy()
        
    for c in range(A.shape[1]):
        for r in range(A.shape[0]):
            if c>=r:
                tmp[r,c] -= (tmp[r,:r]*tmp[:r,c]).sum()
            else:
                tmp[r,c] -= (tmp[r,:c]*tmp[:c,c]).sum()
                tmp[r,c] /= tmp[c,c]
            
    for i in range(A.shape[0]):
            for j in range(i):
                out[i,:] -= out[j,:]*tmp[i,j]            
            
    for i in range(A.shape[0])[::-1]:
            for j in range(i+1,A.shape[1]):
                out[i,:] -= out[j,:]*tmp[i,j]
            out[i,:] /= tmp[i,i]
                        
    return out
    
A = np.random.rand(9).reshape((3,3))
b = np.random.rand(3).reshape((3,1))

x = solve_LU(A,b)

print 'Matrix A =\n',A
print 'Matrix b =\n',b
print 'Matrix x =\n',x
print 'Ax-b =\n',A.dot(x)-b