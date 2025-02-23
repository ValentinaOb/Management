import matplotlib.pyplot as plt
import numpy as np
import math
import csv

# Enable interactive mode
plt.ion()

# Create figure and axis
fig, ax = plt.subplots()
ax.set_ylim([0, 8])  # Змінений масштаб для видимих змін
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

output_data = np.loadtxt("file.csv", delimiter=",", skiprows=1)
new_data1 = output_data[:, 0] 
new_data2 = output_data[:, 1] 
data1 = np.array([])
data2 = np.array([])

data1=np.append(data1, new_data1)
data2=np.append(data1, new_data2)

#print(new_data1)

line1, = ax.plot([], [], label="X")
line2, = ax.plot([], [], label="Y")

while True:
    t += 0.01
    new_data = float(5 - math.exp(-t))

    print(t,' ', new_data)

    # Append new data and time
    data = np.append(data, new_data)
    time = np.append(time, t)

    # Keep the last 100 points
    if len(data) > 100:
        data = data[-100:]
        time = time[-100:]

    # Update the plot
    line.set_data(time, data)

    line1.set_data(time, data1)
    line2.set_data(time, data2)

    ax.set_xlim(time[0], time[-1])  # Adjust x-axis dynamically
    plt.draw()
    plt.pause(0.01)
