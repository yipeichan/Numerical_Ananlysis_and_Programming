import scipy.optimize as opt
 
def squareroot(R):
    def fsq(x):  return x*x-R
    def fsqp(x): return 2.*x
    
    return opt.newton(fsq,R*0.5,fsqp)

R = 1234.
   
print 'root = %.16f, diff = %.16f' % \
    (squareroot(R),abs(R**0.5-squareroot(R)))
