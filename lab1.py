import numpy as np
import matplotlib.pyplot as plt

c0 = 1
c1 = 0.1
d = [1, 5, 6] 

def plant_response(u, dt, x_prev):
    #Simulates the system response by means of discretisation
    x1, x2 = x_prev
    dx1 = x2
    dx2 = (c0 * u + c1 * u - d[1] * x2 - d[2] * x1) / d[0]
    x1_new = x1 + dx1 * dt
    x2_new = x2 + dx2 * dt
    return x1_new, x2_new

a, b, c = 0.6, 0.3, 0.1 

def pid_control(e, e_prev, e_sum, dt):
    #Implementation of the PID controller
    de = (e - e_prev) / dt
    e_sum += e * dt
    u = a * e + b * de + c * e_sum
    return u, e_sum


x = (0, 0)
e_prev = 0
e_sum = 0
time = []
y_out = []
y_desired = []


plt.ion()
fig, ax = plt.subplots(figsize=(10, 5))
line, = ax.plot([], [], label="System status x(t)")
line1, = ax.plot([], [], label="Desired trajectory y(t)", linestyle='dashed')
ax.set_xlabel("Time")
ax.set_ylabel("System output")
ax.set_title("System response with PID controller (without ready-made functions)")
ax.legend()
ax.grid()

t = 0
dt = 0.1
while True:
    y_d = 5 - np.exp(-t)
    e = y_d - x[0]
    u, e_sum = pid_control(e, e_prev, e_sum, dt)
    x = plant_response(u, dt, x)
    
    time.append(t)
    y_out.append(x[0])
    y_desired.append(y_d)
    e_prev = e
    
    # Update
    if len(time) > 100:
        time = time[-100:]
        y_out = y_out[-100:]
        y_desired = y_desired[-100:]
    
    min_len = min(len(time), len(y_out), len(y_desired))
    line.set_data(time[:min_len], y_out[:min_len])
    line1.set_data(time[:min_len], y_desired[:min_len])
    
    if len(time) > 0:
        ax.set_xlim(time[0], time[-1])
        ax.set_ylim(min(y_out + y_desired) - 0.5, max(y_out + y_desired) + 0.5)
    
    plt.draw()
    plt.pause(0.01)
    t += dt