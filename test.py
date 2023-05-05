import numpy as np
import matplotlib.pyplot as plt


def circle_orbit(theta):
    x = np.cos(theta)*50
    y = np.sin(theta)*50
    return x, y

theta = np.linspace(0, 2*np.pi, 100)

x_data = []
y_data = []

for t in theta:
    x, y = circle_orbit(t)
    x_data.append(x)
    y_data.append(y)
    
print(circle_orbit(2*np.pi)[0])

# plt.figure(figsize=(4,4)) 
# plt.plot(x_data, y_data)
# plt.show()