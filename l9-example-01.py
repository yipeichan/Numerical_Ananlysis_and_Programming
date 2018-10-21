import numpy as np

A = np.random.rand(9).reshape((3,3))
B = np.random.rand(9).reshape((3,3))
C = np.random.rand(9).reshape((3,3))

M = A.dot(B).dot(C).T
N = C.T.dot(B.T).dot(A.T)

print '(A*B*C)^T =\n',M
print 'C^T * B^T * A^T =\n',N
print 'Difference =\n',M-N
