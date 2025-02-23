import matplotlib.pyplot as plt
import numpy as np
import math

import csv
# Увімкнення інтерактивного режиму
plt.ion()

# Створення фігури та осі
fig, ax = plt.subplots()
ax.set_ylim([-8, 8])  
ax.set_xlim([0, 1])  
ax.grid(True)  

# Ініціалізація порожніх масивів
data = np.array([])
data1 = np.array([])
time = np.array([])

# Створення ліній для оновлення
line1, = ax.plot([], [], label="x", color="blue")  
line2, = ax.plot([], [], label="y", color="red")   

ax.set_xlabel('Time (ms)')
ax.set_ylabel('Data')
ax.set_title('Real-time Data Plot')

# Ініціалізація змінних
t = 0
x1 = x0 = x_1 = 0
u1 = u_1 = 0

for i in range(300):
    u0 = u1
    u_1 = u0

    x0 = x1
    x_1 = x0

    t += 0.01
    e = 5 - math.exp(-t)

    u1 = 0.6 * ((5 - math.exp(-t) - x0)) + 6 * (e - x0) + 0.1 * (-x0 / t)
    u_ = 1 / t**2 * (u1 - 2 * u0 + u_1)
    x1 = 6 * x0 + (5 / t * (x1 - x0)) + (1 / t**2 * (x1 - 2 * x0 + x_1)) - 0.1 * u_

    # Додавання нових значень
    data = np.append(data, x1)
    data1 = np.append(data1, u1)
    time = np.append(time, t)

    # Set the new data
    line1.set_data(time, data)
    line2.set_data(time, data1)

    # Update axes limits
    ax.relim()  
    ax.autoscale_view()  

    print(data)

    
    output_data = np.column_stack((data, data1))

    np.savetxt("file.csv", output_data, delimiter=",", header="data1", comments='')


    plt.draw()
    plt.pause(0.01)

'''
    # Динамічна зміна меж X
    ax.set_xlim(min(time, default=0), max(time, default=1))

    # Оновлення масштабу
    ax.relim()
    ax.autoscale_view()

    #print('X_1: ', x_1, ' X0: ', x0, '  X1: ', x1)
    #print('U_1: ', u_1, ' U0: ', u0, '  U1: ', u1)
    print(data1)

    # Оновлення графіку
    #fig.canvas.flush_events()
    plt.draw()
    plt.pause(0.01)
    plt.show()
'''