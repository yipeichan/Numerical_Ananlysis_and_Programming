import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8), dpi=80) # initializing a fig with 8x8 inches

n = 3.
d = 8.
k = n/d
t = np.linspace(0.,np.pi*2.*d,1000*d)

x = np.cos(k*t)*np.cos(t)
y = np.cos(k*t)*np.sin(t)

plt.plot(x, y, linewidth=2, color='red')

plt.show()