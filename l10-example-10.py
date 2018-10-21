import numpy as np
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
    
plt.xlim(xmin, xmax)
plt.ylim(-1.,20.)
plt.show()
