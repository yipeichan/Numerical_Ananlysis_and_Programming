import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

xmin, xmax, xbinwidth = 101.,182.,3.
vx = np.linspace(xmin+xbinwidth/2.,xmax-xbinwidth/2.,27)
vy = np.array(
[3., 2., 1., 3., 3., 1., 6., 6.,14., 5.,
 3., 3., 1., 4., 7., 4., 2., 5., 1., 3.,
 4., 3., 0., 1., 3., 1., 5.])
vyerr = vy**0.5    

plt.plot([xmin,xmax],[0.,0.],c='gray',lw=2)    
plt.errorbar(vx, vy, vyerr, c='blue', fmt = 'o')

def model(x, norm, mean, sigma, c0, c1, c2):
    
    polynomial = c0 + c1*((x-xmin)/(xmax-xmin)) + \
                      c2*((x-xmin)/(xmax-xmin))**2
    
    gaussian = norm*xbinwidth/(2.*np.pi)**0.5/sigma * \
               np.exp(-0.5*((x-mean)/sigma)**2)
    
    return polynomial + gaussian    
    
def fcn(p):    
    expected = model(vx,p[0],p[1],p[2],p[3],p[4],p[5])
    delta = (vy[vy>0.]-expected[vy>0.])/vyerr[vy>0.]
    return (delta**2).sum()    
    
p_init = np.array([15.,125.,2.0,2.0,0.,0.])
r = opt.minimize(fcn,p_init)   

if r.success:
    print 'N(Higgs)  = %.1f events' % r.x[0]
    print 'M(Higgs)  = %.1f GeV' % r.x[1]
    print 'chi^2/ndf = %.2f' % (fcn(r.x)/(len(vy[vy>0.])-len(r.x)))
    
    cx = np.linspace(xmin,xmax,500)
    cy = model(cx,r.x[0],r.x[1],r.x[2],r.x[3],r.x[4],r.x[5]) 
    cy_bkg = model(cx,0.,r.x[1],r.x[2],r.x[3],r.x[4],r.x[5])    
    
    plt.plot(cx, cy, c='red',lw=2)
    plt.plot(cx, cy_bkg, c='red',lw=2,ls='--')
else:
    print r.message
    
plt.xlim(xmin, xmax)
plt.ylim(-1.,20.)
plt.show()
    