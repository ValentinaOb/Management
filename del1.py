import numpy as np
import matplotlib.pyplot as plt


c0, c1 = 1, 0.1
d1, d2 = 5, 6

n, m, r = 5, 1, 100
k = 1.0  

def plant_response(u, dt, x_0, x_one):
    x_two = (c0 * u + c1 * u - d1 * x_one - d2 * x_0)
    x1 = x_0 + x_one * dt 
    x_one_next = x_one + x_two * dt  
    return x1, x_one_next

def adaptive_control(e, e_prev, e_sum, dt, k):
    u_ = (e - e_prev) / dt
    e_sum += e * dt
    u = k * (n * e + m * u_ + r * e_sum)
    k += 0.01 * e * u
    return u, e_sum, k

x_0, x_one = 0, 0
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

t, dt = 0, 0.01
while True:
    y_d = 5 - np.exp(-t)
    e = y_d - x_0
    u, e_sum, k = adaptive_control(e, e_prev, e_sum, dt, k)
    x_0, x_one = plant_response(u, dt, x_0, x_one)
    
    time.append(t)
    y_out.append(x_0)
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
