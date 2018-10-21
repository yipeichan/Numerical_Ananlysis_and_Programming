import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(10000)

hist,bin_edges = np.histogram(data, bins=100, range=(-5.,+5.))
bin_centers = 0.5*(bin_edges[1:]+bin_edges[:-1])
bin_errors = np.sqrt(hist)

plt.subplot(2,1,1)
plt.bar(bin_edges[:-1], hist, width=bin_edges[1]-bin_edges[0],color='yellow')
plt.xlim(-5.,5.)

plt.subplot(2,1,2)
plt.errorbar(bin_centers, hist, yerr = bin_errors, fmt = 'o')
plt.xlim(-5.,5.)

plt.show()
