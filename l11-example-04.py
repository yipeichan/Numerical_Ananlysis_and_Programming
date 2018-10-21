import numpy as np
import matplotlib.pyplot as plt

def f(t,y): return y

vt = np.zeros(200)
vy = np.zeros((4,200))

t = 0.
y1 = y2 = y4 = 1.
h = 0.001

for idx in range(200):
    for step in range(1000):
        k1  = f(t, y1)
        y1 += h*k1    
    
        k1  = f(t, y2)
        k2  = f(t+0.5*h, y2+0.5*h*k1)    
        y2 += h*k2

        k1  = f(t, y4)
        k2  = f(t+0.5*h, y4+0.5*h*k1)
        k3  = f(t+0.5*h, y4+0.5*h*k2)
        k4  = f(t+h, y4+h*k3)                
        y4 += h/6.*(k1+2.*k2+2.*k3+k4)
    
        t += h
    
    vt[idx] = t
    vy[0,idx] = np.exp(t)
    vy[1,idx] = y1
    vy[2,idx] = y2
    vy[3,idx] = y4

plt.plot(vt,abs(vy[1]-vy[0])/vy[0],lw=2,c='Blue')
plt.plot(vt,abs(vy[2]-vy[0])/vy[0],lw=2,c='Green')
plt.plot(vt,abs(vy[3]-vy[0])/vy[0],lw=2,c='Red')
plt.yscale('log')
plt.ylim(1E-16,0.2)
plt.xlim(0.,200.)
plt.show()