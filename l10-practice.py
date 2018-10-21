import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

xmin, xmax, xbinwidth = 0.,1.,0.01
vx = np.linspace(0.,1.,101)
vy = np.array(
[13,20,19,17,27,26,22,22,20,22,17,24,23,22,15,23,23,26,24,23,21,15,16,18,24,
 21,17,23,16,31,17,17,23,24,23,27,24,26,15,21,22,21,25,22,24,22,23,11,19,19,
 23,15,22,33,25,35,21,24,22,30,29,32,26,43,26,25,22,21,40,37,25,23,35,28,35,
 31,22,33,22,35,27,33,34,50,40,36,47,46,32,31,46,46,51,56,35,45,40,45,34,54,
 51],dtype='float64')
vyerr = vy**0.5    

plt.errorbar(vx, vy, vyerr, c='blue', fmt = 'o')
plt.show()

