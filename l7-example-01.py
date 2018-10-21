import math

def f(x):  
    return x**2+math.exp(x)+math.log(x)+math.sin(x)
def fp(x): 
    return 2.*x+math.exp(x)+1./x+math.cos(x)

x, h = 0.5, 1E-2
fp_exact = fp(x)

while h>1E-15:
    fp_numeric = (f(x+h) - f(x))/h	
    print 'h = %e' % h
    print 'Exact = %.16f,' % fp_exact,
    print 'Numeric = %.16f,' % fp_numeric,		
    print 'diff = %.16f' % abs(fp_numeric-fp_exact)
    h /= 10.