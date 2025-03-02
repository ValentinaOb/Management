import matplotlib.pyplot as plt
import numpy as np
import math

# Enable interactive mode
plt.ion()

# Create figure and axis
fig, ax = plt.subplots()
ax.set_ylim([-100, 100])  
ax.set_xlim([0, 100])
ax.grid(True)

# Initialize empty data arrays
data = np.array([])
time = np.array([])
data1 = np.array([])
data2 = np.array([])

# Create empty plots
line, = ax.plot([], [], label="Y")
line1, = ax.plot([], [], label="X")
line2, = ax.plot([], [], label="U")

ax.set_xlabel('Time (ms)')
ax.set_ylabel('Data')
ax.set_title('Real-time Data Plot')
ax.legend()

t =0  # Start with a small nonzero value
dt = 1
x1 = x0 = x_1 = 0
u1 = u_1 = 0
S = 0

while True:
    t += dt
    y = float(5 - math.exp(-t))

    # Append new data
    data = np.append(data, y)
    time = np.append(time, t)

    u0 = u1
    u_1 = u0

    x0 = x1
    x_1 = x0

    S += dt * (y - x0)

    u1 = 0.6 * ((y - x0)) + 6 * S + 0.1 * y + 0.1 * ((x1 - x0) / dt)
    u_ = (u1 - u0) / dt
    
    x1 = 6 * x0 + (5 / t * (x1 - x0)) + (1 / t**2 * (x1 - 2 * x0 + x_1)) - 0.1 * u_
    print("Y: ",y,"S: ",S, "U1: ",u1,"U_: ",u_, "X1: ",x1)
    data1 = np.append(data1, x1)
    data2 = np.append(data2, u1)

    # Keep only the last 100 points
    if len(data) > 100:
        data = data[-100:]
        time = time[-100:]
        data1 = data1[-100:]
        data2 = data2[-100:]

    # Ensure all arrays have the same length
    min_len = min(len(time), len(data1), len(data2))
    line.set_data(time[:min_len], data[:min_len])
    line1.set_data(time[:min_len], data1[:min_len])
    line2.set_data(time[:min_len], data2[:min_len])

    # Adjust X-axis dynamically
    if len(time) > 0:
        ax.set_xlim(time[0], time[-1])

    plt.draw()
    plt.pause(0.01)
