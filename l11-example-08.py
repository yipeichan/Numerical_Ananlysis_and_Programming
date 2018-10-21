import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import ode

fig = plt.figure(figsize=(6,6), dpi=80)
ax = plt.axes(xlim=(-1.2,+1.2), ylim=(-1.2,+1.2))

spring, = ax.plot([], [], lw=2, color='black')
ball,  = ax.plot([], [], 'ro', ms=10)
text   = ax.text(0.,1.1,'', fontsize = 16, color='black', ha='center', va='center')

m, g, R0, k = 1., 9.8, 0.5, 100.

def f(t,y):     
    bx, by = y[0], y[1]
    vx, vy = y[2], y[3]
    R = (bx**2+by**2)**0.5
    
    fs = -k*(R-R0)
    ax = fs*bx/R/m
    ay = fs*by/R/m - g
    
    return np.array([vx,vy,ax,ay])
    
intr = ode(f).set_integrator('dop853')   
intr.set_initial_value(np.array([0.3,0.4,0.,0.]), 0.)
 
def init():
    spring.set_data([], [])
    ball.set_data([], [])
    text.set(text='')
    return spring, ball, text

def animate(i):
    intr.integrate(intr.t+0.040)
    
    bx, by = intr.y[0], intr.y[1]
    vx, vy = intr.y[2], intr.y[3]
    R = (bx**2+by**2)**0.5  
    ball.set_data(bx, by)          
    
    t = np.linspace(0.,1.,200)
    sx = bx*t + np.cos(60.*t)*0.03
    sy = by*t + np.sin(60.*t)*0.03
    sx[len(t)-15:] = np.linspace(sx[len(t)-15],bx,15)
    sy[len(t)-15:] = np.linspace(sy[len(t)-15],by,15)
    sx[:15] = np.linspace(0.,sx[14],15)
    sy[:15] = np.linspace(0.,sy[14],15)                                                                                                                                                                                                                                                                                                                  
    spring.set_data(sx, sy)
    
    E = m*g*by + 0.5*m*(vx**2+vy**2) + 0.5*k*(R-R0)**2
    text.set(text='E = %.16f' % E)
    
    return spring, ball, text

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=10, interval=40)
plt.show()    
