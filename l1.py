import matplotlib.pyplot as plt
import numpy as np
import math

# Enable interactive mode
plt.ion()

# Create figure and axis
fig, ax = plt.subplots()
ax.set_ylim([-100, 100])  # Змінений масштаб для видимих змін
ax.set_xlim([0, 100])
ax.grid(True)  # Додає сітку

# Initialize empty data arrays
data = np.array([])
time = np.array([])

# Create an empty plot and add a legend
line, = ax.plot([], [], label="Data")
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Data')
ax.set_title('Real-time Data Plot')
ax.legend()

t = 0
dt = 1


data1 = np.array([])
data2 = np.array([])


line1, = ax.plot([], [], label="X")
line2, = ax.plot([], [], label="Y")


x1 = x0 = x_1 = 0
u1 = u_1 = 0
S=0
plt.legend()

while True:
    t += dt
    new_data = float(5 - math.exp(-t))

    # Append new data and time
    data = np.append(data, new_data)
    time = np.append(time, t)

    # Keep the last 100 points
    if len(data) > 100:
        data = data[-100:]
        time = time[-100:]

        data1 = data1[-100:]
        data2 = data2[-100:]
        

    # Update the plot
    line.set_data(time, data)

#
    u0 = u1
    u_1 = u0

    x0 = x1
    x_1 = x0

    e = 5 - math.exp(-t)

    S+=dt*(math.exp(-t)-x0)
    u1=0.6 * ((e - x0)) + 6 *S+0.1*math.exp(-t) - 0.1*((x1-x0)/dt)
    u_=(u1-u0)/dt
    
    x1 = 6 * x0 + (5 / t * (x1 - x0)) + (1 / t**2 * (x1 - 2 * x0 + x_1)) - 0.1 * u_
    #print(S, " ", u1, " ", u_," ",x1)

    data1 = np.append(data1, x1)
    data2 = np.append(data2, u1)
    
    line1.set_data(time, data1)
    line2.set_data(time, data2)
    #print(data2)
  
    
    #




    ax.set_xlim(time[0], time[-1])  # Adjust x-axis dynamically
    #ax.set_ylim(data1[0], data1[-1])  # Adjust x-axis dynamically
    plt.draw()
    
    plt.pause(0.01)
