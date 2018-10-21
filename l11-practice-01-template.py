import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import ode

fig = plt.figure(figsize=(6,6), dpi=80)
ax = plt.axes(xlim=(-1.,1.), ylim=(-1.,1.))
blackhole,  = ax.plot([0.], [0.], 'bo', ms=20)
ball,  = ax.plot([], [], 'ro', ms=10)

t_init = 0.
y_init = [-1.,-1.,1.,0.5] # (px,py,vx,vy)

def f(t,y):     
###########################################
# modify the code below accordingly        
###########################################

    px = y[0]
    py = y[1]
    vx = y[2]
    vy = y[3]
    ax = 0.
    ay = 0.
    
    return np.array([vx,vy,ax,ay])
    
###########################################      
    
intr = ode(f).set_integrator('dop853')   
intr.set_initial_value(y_init, t_init) 

def init():
    ball.set_data([], [])
    return ball

def animate(i):
    intr.integrate(intr.t+0.025)
    
    px = intr.y[0]
    py = intr.y[1]
    
    ball.set_data(px, py)
    
    return ball

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=10, interval=40)
plt.show()
