import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)

plt.show()

'''import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Define data
data = np.array([2.64656711e+01, 3.07028315e+05, 7.63965307e+08])
time = np.array([1, 2, 3])

# Create the line with empty data
line1, = ax.plot([], [], label="x", color="blue")  

# Set the new data
line1.set_data(time, data)

# Update axes limits
ax.relim()  
ax.autoscale_view()  

# Draw the updated figure
plt.legend()
plt.draw()
plt.show()
'''