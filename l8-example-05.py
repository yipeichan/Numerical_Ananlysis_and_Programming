import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(1000)
y = np.random.rand(1000)

plt.scatter(x, y, c = (x+y)*0.5, s=50, alpha=0.5)

plt.xlim(0.,1.)
plt.ylim(0.,1.)
plt.show()