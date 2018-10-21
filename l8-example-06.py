import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
xv, yv = np.meshgrid(x, y)
zv = np.sin(xv)*np.sin(yv)

plt.contourf(xv, yv, zv, 12, alpha=.75, cmap='Blues')
ctr = plt.contour(xv, yv, zv, 12, colors='black', linewidth=.5)
plt.clabel(ctr, fontsize=8)

plt.show()
