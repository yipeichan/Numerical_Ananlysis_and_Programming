import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import ode

fig = plt.figure(figsize=(10,5), dpi=80)
ax = plt.axes([0.1,0.1,0.85,0.85],xlim=(0.,1.), ylim=(-1.25,+1.25))

nseg = 500
T, m, L = 1., 1., 1.
nhamonic = 1

vel  = (T*L/m)**0.5 
lamb = L*2./nhamonic
freq = vel/lamb

y_init = np.zeros(nseg*2)
y_init[:nseg] = np.sin(np.pi*nhamonic*np.linspace(1./(nseg+1),1.-1./(nseg+1),nseg))
y_init[nseg:] = 0.

ax.plot([0.,1.], [0.,0.], lw=2, color='0.5', ls='--')
ax.text(0.05,-1.1,
        'Tension = %g N, $\mu$ = %g kg/m, Hamonic #%d, Frequency = %g Hz' % (T,m/L,nhamonic,freq), 
        fontsize = 16, color='black', ha='left', va='center')

string, = ax.plot([], [], lw=2, color='blue')

def f(t,y): 
    ry = y[:nseg]
    vy = y[nseg:]
        
    dx = L/(nseg+1)
    dm = m/nseg
    
    dydt = np.zeros(nseg*2)    
    dydt[:nseg]     = vy
    dydt[nseg]      = T/dm*(ry[1]-ry[0]*2.)/dx
    dydt[nseg+1:-1] = T/dm*(ry[:-2]+ry[2:]-ry[1:-1]*2.)/dx
    dydt[-1]        = T/dm*(ry[-2]-ry[-1]*2.)/dx
    
    return dydt
    
intr = ode(f).set_integrator('dop853')   
intr.set_initial_value(y_init, 0.)
 
def init():
    string.set_data([], [])
    return string, 

def animate(i):
    intr.integrate(intr.t+0.040)
    
    px = np.linspace(0.,1.,nseg+2)
    py = np.zeros(nseg+2)
    py[1:-1] = intr.y[:nseg]
        
    string.set_data(px,py) 
    return string,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=10, interval=40)
plt.grid(True)
plt.show()    
