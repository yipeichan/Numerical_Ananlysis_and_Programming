import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import ode

fig = plt.figure(figsize=(6,6), dpi=80)
ax = plt.axes(xlim=(-1.2,+1.2), ylim=(-1.2,+1.2))

speed = 0.2
nseg = 50
m, dm = 1., 0.1/nseg
g, R0, k = 9.8, 1.0, 1000.*nseg

rope, = ax.plot([], [], lw=2, color='black')
ball,  = ax.plot([], [], 'ro', ms=10)
ax.text(0.,1.1,'Frame speed = '+str(speed)+'x', fontsize = 16, color='black', ha='center', va='center')

def f(t,y): 
    rx = y[nseg*0:nseg*1]
    ry = y[nseg*1:nseg*2]
    vx = y[nseg*2:nseg*3]
    vy = y[nseg*3:nseg*4]
    
    dx = rx.copy()
    dy = ry.copy()
    dx[1:] -= rx[:-1]
    dy[1:] -= ry[:-1]  
    R = (dx**2+dy**2)**0.5
    fs = -k*(R-R0/nseg)
    
    dydt = np.zeros(nseg*4)
    dydt[nseg*0:nseg*1] = vx
    dydt[nseg*1:nseg*2] = vy
    ax = dydt[nseg*2:nseg*3]
    ay = dydt[nseg*3:nseg*4]
    
    ax[:-1] = fs[:-1]*dx[:-1]/R[:-1]/dm \
            - fs[1: ]*dx[1: ]/R[1: ]/dm
    ay[:-1] = fs[:-1]*dy[:-1]/R[:-1]/dm \
            - fs[1: ]*dy[1: ]/R[1: ]/dm - g
    ax[-1 ] = fs[-1]*dx[-1]/R[-1]/m 
    ay[-1 ] = fs[-1]*dy[-1]/R[-1]/m - g

    return dydt
    
intr = ode(f).set_integrator('dop853',rtol=0.01)   
y_init = np.zeros(nseg*4)
y_init[nseg*0:nseg*1] = np.linspace(0.,0.8,nseg,endpoint=False)+0.8/nseg
y_init[nseg*1:nseg*2] = np.linspace(0.,0.6,nseg,endpoint=False)+0.6/nseg
intr.set_initial_value(y_init, 0.)
 
def init():
    rope.set_data([], [])
    ball.set_data([], [])
    return rope, ball

def animate(i):
    intr.integrate(intr.t+0.040*speed)
    
    rx = intr.y[nseg*0:nseg*1]
    ry = intr.y[nseg*1:nseg*2]
        
    ball.set_data(rx[nseg-1],ry[nseg-1])                                                                                                                                                                                                                                                                                                
    rope.set_data(rx,ry)
        
    return rope, ball

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=10, interval=40)
plt.show()    
