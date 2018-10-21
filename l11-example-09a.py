import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.io.wavfile as wavfile
from scipy.integrate import ode

fig = plt.figure(figsize=(10,5), dpi=80)
ax = plt.axes([0.1,0.1,0.85,0.85],xlim=(0.,1.), ylim=(-1.25,+1.25))

nseg = 500
T, m, L = 400., 0.01, 1.
nhamonic = 2

vel  = (T*L/m)**0.5 
lamb = L*2./nhamonic
freq = vel/lamb

# 1 - sine wave / single hamonic number
# 2 - sine wave / multiple hamonics
# 3 - trangle wave
# 4 - Gaussian pulse
# 5 - random wave
init_condition = 5

y_init = np.zeros(nseg*2)
x = np.linspace(1./(nseg+1),1.-1./(nseg+1),nseg)

if init_condition==1:
    y_init[:nseg] = np.sin(np.pi*nhamonic*x)
    ax.text(0.05,-1.1,
        'Tension = %g N, $\mu$ = %g kg/m, Hamonic #%g, Frequency = %g Hz' % (T,m/L,nhamonic,freq), 
        fontsize = 16, color='black', ha='left', va='center')
        
elif init_condition == 2:  
    for n in range(8):
        y_init[:nseg] += np.sin(np.pi*n*nhamonic*x)
    y_init[:nseg] /= abs(y_init[:nseg]).max()    
    ax.text(0.05,-1.1,
        'Tension = %g N, $\mu$ = %g kg/m, Base hamonic #%g, Base frequency = %g Hz' % (T,m/L,nhamonic,freq), 
        fontsize = 14, color='black', ha='left', va='center')
        
elif init_condition == 3: 
    y_init[:nseg] = 0.5 - abs(x-0.5)
    y_init[:nseg] /= abs(y_init[:nseg]).max()
    
elif init_condition == 4: 
    y_init[:nseg] = np.exp(-0.5*((x-0.5)/0.1)**2)
    
elif init_condition == 5: 
    rnd = np.random.randn(nseg/2)
    for i in range(nseg/2):
        y_init[i] = rnd[:i].sum()
    y_init[nseg/2:nseg] = y_init[:nseg/2][::-1]
    y_init[:nseg] /= abs(y_init[:nseg]).max()

y_init[nseg:] = 0.
rec_idx = np.argmax(y_init[:nseg])

ax.plot(x, y_init[:nseg], lw=1, color='cyan')     

rate = 110250
rec_max = rate/2 # 0.5 sec
rec_cnt = 0
data = np.zeros(rec_max)
time_step = 1./rate
steps_per_frame = 49
saved = False
filename = 'output.wav'
        
ax.plot([0.,1.], [0.,0.], lw=2, color='0.5', ls='--')
for i in range(1,10):
    ax.plot([0.1*i,0.1*i], [-0.1,+0.1], lw=1, color='0.5')
    ax.text(0.1*i,+0.1,'%.2f sec' % (0.01*i), 
        fontsize = 10, color='black', ha='center', va='bottom')               

wave, = ax.plot([], [], lw=1, color='green')        
string, = ax.plot([], [], lw=2, color='blue')
text = ax.text(0.05,+1.1,'', fontsize = 16, color='black', ha='left', va='center')

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
    wave.set_data([], [])
    string.set_data([], [])
    text.set(text='')
    return wave, string, text

def animate(i):
    global rec_cnt, data, saved
    
    if rec_cnt>=rec_max: 
        if not saved:
            data *= (23000./abs(data).max())
            wavfile.write(filename,rate,data.astype('int16'))    
            saved = True
            text.set(text='%.3f sec saved to %s' % (float(rec_cnt)/rate,filename))
    
        return wave, string, text
    
    for step in range(steps_per_frame):
        intr.integrate(intr.t+time_step)
        
        if rec_cnt<rec_max:
            data[rec_cnt] = intr.y[rec_idx]
            rec_cnt += 1            
    
    px = np.linspace(0.,1.,nseg+2)
    py = np.zeros(nseg+2)
    py[1:-1] = intr.y[:nseg]
        
    string.set_data(px,py) 
    
    wt = np.linspace(0.,1.*min(rec_cnt,rate/10)/(rate/10),min(rec_cnt,rate/10))
    wave.set_data(wt, data[rec_cnt-min(rec_cnt,rate/10):rec_cnt]*0.5)
    
    text.set(text='%.3f sec recorded' % (float(rec_cnt)/rate))
    
    return wave, string, text

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=10, interval=40)
plt.show()    
