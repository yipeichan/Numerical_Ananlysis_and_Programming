import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('testimage.jpg')

# convert to [0-1] array 
tmp = img.astype('float64')/255. 

x = np.linspace(-np.pi, np.pi, img.shape[1])
y = np.linspace(-np.pi, np.pi, img.shape[0])
xv, yv = np.meshgrid(x, y)
zv = abs(np.sin(np.arctan2(yv,xv)*3.))*np.exp(-0.1*(yv**2+xv**2))

for i in range(3):
    tmp[:,:,i] *= zv
    tmp[:,:,i] /= tmp[:,:,i].max()

plt.imshow(tmp)
plt.show()


