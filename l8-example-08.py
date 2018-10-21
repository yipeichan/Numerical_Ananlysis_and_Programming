import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(10000)

plt.subplot(2,1,1)
plt.hist(data, bins=100, range=(-5.,+5.), color='yellow')
plt.xlim(-5.,5.)

plt.subplot(2,1,2)
plt.hist(data, bins=20, range=(-5.,+5.), normed=True, color='green')
plt.xlim(-5.,5.)

plt.show()
