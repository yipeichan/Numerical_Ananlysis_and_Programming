import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode

###########################################
# put the correct initial conditions here
###########################################
y_init = [0.,0.]
t_init = 0.
###########################################   

def f(t,y):     
###########################################
# modify the code below accordingly        
###########################################
    return np.array([0.,0.])
###########################################      
    
intr = ode(f).set_integrator('dop853')   
intr.set_initial_value(y_init, t_init) 

vx = np.zeros(200)
vt = np.zeros(200)
 
for step in range(200):
    intr.integrate(intr.t+0.1)

###########################################
# modify the code below accordingly        
###########################################
    x = 0.
    vx[step] = x
    vt[step] = intr.t 
###########################################    
    
    print 'At %.1f sec : x = %.5f' % (intr.t, x)
    
plt.plot(vt,vx,lw=2,color='blue')    
plt.xlim(0.,20.)
plt.ylim(-0.3,0.3)
plt.grid(True)
plt.xlabel('time (s)')
plt.ylabel('x (m)')
plt.show()
