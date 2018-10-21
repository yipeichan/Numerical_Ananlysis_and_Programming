import numpy as np
import matplotlib.pyplot as plt

def f(i,j): 
        return i+j+np.sin(i)*4.+np.sin(j)*4.

img = np.fromfunction(f,(20,20))

plt.imshow(img, interpolation='nearest', cmap='GnBu')
plt.colorbar()

plt.show()
