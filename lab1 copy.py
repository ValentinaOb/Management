import numpy as np
import matplotlib.pyplot as plt

c0, c1 = 1, 0.1
d0, d1, d2 = 1, 5, 6

a, b, c = 0.6, 0.3, 0.1

n, m, r = 5, 1, 100 

k = 1.0  

def adaptive_control(e, e_prev, e_sum, dt):
    global k
    de = (e - e_prev) / dt
    e_sum += e * dt
    k += n * e * dt  
    u0 = k * (m * e + r * de)
    return u0, e_sum

x_1, x0, x1, u_1, u0 = 0,0,0, 0,0
e_prev = 0
e_sum = 0
time, y_out, y_desired = [], [], []

plt.ion()
fig, ax = plt.subplots(figsize=(10, 5))
line, = ax.plot([], [], label="System response x(t)")
line1, = ax.plot([], [], label="Desired trajectory y(t)", linestyle='dashed')
ax.set_xlabel("Time")
ax.set_ylabel("Output")
ax.legend()
ax.grid()

t, dt = 0, 0.1

while True:
    y_d = 5 - np.exp(-t)
    e = y_d - x0

    u_1=u0
    u0, e_sum = adaptive_control(e, e_prev, e_sum, dt)

    x_1=x0
    x0=x1

    x1=dt/d0*(c0*(u0-u_1)+c1*u0*dt- d1*(x0-x_1) - d2*x0*dt) + 2*x0-x_1
    
    time.append(t)
    y_out.append(x0)
    y_desired.append(y_d)
    e_prev = e
    
    # Оновлення графіка
    if len(time) > 100:
        time, y_out, y_desired = time[-100:], y_out[-100:], y_desired[-100:]
    
    line.set_data(time, y_out)
    line1.set_data(time, y_desired)
    ax.set_xlim(time[0], time[-1])
    ax.set_ylim(min(y_out + y_desired) - 0.5, max(y_out + y_desired) + 0.5)
    
    plt.draw()
    plt.pause(0.01)
    t += dt
