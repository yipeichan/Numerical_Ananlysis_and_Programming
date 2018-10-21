import numpy as np
import matplotlib.pyplot as plt

plt.ylim(0.,5.)
plt.xlim(-0.1,1.1)

plt.plot([0,1], [1,1], color = (0.1,0.5,0.7), linewidth = 5)

plt.plot([0,1], [2,2], color = 'red', linewidth = 5)

plt.plot([0,1], [3,3], color = '0.75', linewidth = 5)

plt.plot([0,1], [4,4], color = '#02ef20', linewidth = 5)

plt.show()