import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import ode

fig = plt.figure(figsize=(6,6), dpi=80)
ax = plt.axes(xlim=(-1.2,+1.2), ylim=(-1.2,+1.2))

spring, = ax.plot([], [], lw=2, color='black')
ball,  = ax.plot([], [], 'ro', ms=10)
text   = ax.text(0.,1.1,'', fontsize = 16, color='black', ha='center', va='center')

m, g, R0, k = 1., 9.8, 0.3, 200.

def f(t,y):     
    bx1, by1 = y[0], y[1]
    bx2, by2 = y[2], y[3]    
    vx1, vy1 = y[4], y[5]
    vx2, vy2 = y[6], y[7]    
    R1 = (bx1**2+by1**2)**0.5
    R2 = ((bx2-bx1)**2+(by2-by1)**2)**0.5
        
    fs1 = -k*(R1-R0)
    fs2 = -k*(R2-R0)    
    
    ax1 = fs1*bx1/R1/m - fs2*(bx2-bx1)/R2/m
    ay1 = fs1*by1/R1/m - fs2*(by2-by1)/R2/m - g
    ax2 = fs2*(bx2-bx1)/R2/m
    ay2 = fs2*(by2-by1)/R2/m - g
    
    return np.array([vx1,vy1,vx2,vy2,ax1,ay1,ax2,ay2])
    
intr = ode(f).set_integrator('dop853')   
intr.set_initial_value(np.array([0.18,0.24,0.42,0.42,0.,0.,0.,0.]), 0.)
 
def init():
    spring.set_data([], [])
    ball.set_data([], [])
    text.set(text='')
    return spring, ball, text

def animate(i):
    intr.integrate(intr.t+0.040)
    
    bx1, by1 = intr.y[0], intr.y[1]
    bx2, by2 = intr.y[2], intr.y[3]    
    vx1, vy1 = intr.y[4], intr.y[5]
    vx2, vy2 = intr.y[6], intr.y[7]    
    R1 = (bx1**2+by1**2)**0.5
    R2 = ((bx2-bx1)**2+(by2-by1)**2)**0.5

    ball.set_data([bx1,bx2],[by1,by2])          
    
    t = np.linspace(0.,1.,200)
    sx1 = bx1*t + np.cos(60.*t)*0.03
    sy1 = by1*t + np.sin(60.*t)*0.03
    sx1[len(t)-15:] = np.linspace(sx1[len(t)-15],bx1,15)
    sy1[len(t)-15:] = np.linspace(sy1[len(t)-15],by1,15)
    sx1[:15] = np.linspace(0.,sx1[14],15)
    sy1[:15] = np.linspace(0.,sy1[14],15)   

    sx2 = bx1 + (bx2-bx1)*t + np.cos(60.*t)*0.03
    sy2 = by1 + (by2-by1)*t + np.sin(60.*t)*0.03
    sx2[len(t)-15:] = np.linspace(sx2[len(t)-15],bx2,15)
    sy2[len(t)-15:] = np.linspace(sy2[len(t)-15],by2,15)
    sx2[:15] = np.linspace(bx1,sx2[14],15)
    sy2[:15] = np.linspace(by1,sy2[14],15)   
                                                                                                                                                                                                                                                                                                           
    spring.set_data(np.concatenate((sx1,sx2)), np.concatenate((sy1,sy2)))
    
    E = m*g*by1 + m*g*by2 + 0.5*m*(vx1**2+vy1**2) + 0.5*m*(vx2**2+vy2**2) + 0.5*k*(R1-R0)**2 + 0.5*k*(R2-R0)**2
    text.set(text='E = %.16f' % E)
    
    return spring, ball, text

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=10, interval=40)
plt.show()    
