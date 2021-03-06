import numpy as np

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
b = np.random.rand(3).reshape((3,1))

x = solve_gau2(A,b)

print 'Matrix A =\n',A
print 'Matrix b =\n',b
print 'Matrix x =\n',x
print 'Ax-b =\n',A.dot(x)-b