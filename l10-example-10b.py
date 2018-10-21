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
        
p_init = np.array([15.,125.,2.0,2.0,0.,0.])
rx,rcov = opt.curve_fit(model,vx[vy>0.],vy[vy>0.],p_init,vyerr[vy>0.])

if np.any(rx != p_init):
    print 'N(Higgs) = %.1f +- %.1f events' % (rx[0],rcov[0,0]**0.5)
    print 'M(Higgs) = %.1f +- %.1f GeV' % (rx[1],rcov[1,1]**0.5)
    
    cx = np.linspace(xmin,xmax,500)
    cy = model(cx,rx[0],rx[1],rx[2],rx[3],rx[4],rx[5]) 
    cy_bkg = model(cx,0.,rx[1],rx[2],rx[3],rx[4],rx[5])    
    
    plt.plot(cx, cy, c='red',lw=2)
    plt.plot(cx, cy_bkg, c='red',lw=2,ls='--')
    
plt.xlim(xmin, xmax)
plt.ylim(-1.,20.)
plt.show()
    