import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8), dpi=80) # initializing a fig with 8x8 inches

# initial some (x,y) data points in numpy array
x = np.linspace(0.,40.,1000)
y1 = np.sin(x)*np.exp(-x*0.10)
y2 = np.cos(x)*np.exp(-x*0.15)
y3 = np.sin(x*2.0)*np.sin(x*0.2)*np.random.rand(x.size)

plt.subplot(2, 1, 1) # initial a subplot, from grid of 1x2
plt.plot(x, y1, color = 'blue', linewidth = 2, linestyle = '-')
plt.plot(x, y2, color = 'red', linewidth = 2, linestyle = '--')
plt.ylim(-1.,+1.)

plt.subplot(2, 1, 2) # initial another subplot
plt.plot(x, y3, color = 'green', linewidth = 1)

plt.show()