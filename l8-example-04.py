import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,20.,40)
y = np.sin(x)*1.2

plt.subplot(3,3,1)
plt.plot(x, y, linewidth = 3, linestyle='-')

plt.subplot(3,3,2)
plt.plot(x, y, linewidth = 3, linestyle='--')

plt.subplot(3,3,3)
plt.plot(x, y, linewidth = 3, linestyle=':')

plt.subplot(3,3,4)
plt.plot(x, y, linewidth = 3, linestyle='-.')

plt.subplot(3,3,5)
plt.plot(x, y, linestyle='None', marker='+')

plt.subplot(3,3,6)
plt.plot(x, y, linestyle='None', marker=',')

plt.subplot(3,3,7)
plt.plot(x, y, linestyle='None', marker='.')

plt.subplot(3,3,8)
plt.plot(x, y, linestyle='None', marker='^')

plt.subplot(3,3,9)
plt.plot(x, y, linestyle='None', marker='o')

plt.show()