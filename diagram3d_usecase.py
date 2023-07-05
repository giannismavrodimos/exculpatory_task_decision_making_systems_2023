
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Define the coordinates and temperature values
x = np.linspace(0, 10, 11)
y = np.linspace(0, 10, 11)
X, Y = np.meshgrid(x, y)
Z = np.array([[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
              [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
              [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
              [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
              [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
              [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
              [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
              [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
              [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33],
              [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34],
              [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]])

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surface = ax.plot_surface(X, Y, Z, cmap='coolwarm')

# Add colorbar
fig.colorbar(surface)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Temperature (°C)')
ax.set_title('Temperature Variation')

# Display the plot
plt.show()