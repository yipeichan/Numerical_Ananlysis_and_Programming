import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.,40.,500)
y = np.sin(x)*np.exp(-x*0.1)

plt.plot(x,y)
plt.show()