import numpy as np
from scipy.integrate import ode

m, g, R = 1., 9.8, 1.
t = 0.
y = np.array([np.pi*0.9999,0.])

def f(t,y):     
    theta   = y[0] 
    thetap  = y[1]
    thetapp = -g/R*np.sin(theta)
    
    return np.array([thetap,thetapp])
    
intr = ode(f).set_integrator('dop853')   
intr.set_initial_value(y, t)

while intr.t<8.:        
    intr.integrate(intr.t+0.1)
    
    theta  = intr.y[0]
    thetap = intr.y[1]     
    
    print 'At %.2f sec : (%+14.10f, %+14.10f)' % (intr.t, theta, thetap)