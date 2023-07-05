


from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# Fixing random state for reproducibility
np.random.seed(19680801)

def polygon_under_graph(x, y):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """
    return [(x[0], 0.), *zip(x, y), (x[-1], 0.)]

# Create a 3D plot
ax = plt.figure().add_subplot(projection='3d')

# Generate x values and a range of lambda values
x = np.linspace(0., 10., 31)
lambdas = range(1, 9)

# Generate the vertex list for each polygon under the line graph
verts = [polygon_under_graph(x, poisson.pmf(l, x)) for l in lambdas]

# Generate face colors for each polygon using the 'viridis_r' colormap
facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(verts)))

# Create a PolyCollection object with the vertex lists and face colors
poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)

# Add the PolyCollection to the plot with the corresponding lambda values
ax.add_collection3d(poly, zs=lambdas, zdir='y')

# Set the limits and labels for the plot
ax.set(xlim=(0, 10), ylim=(1, 9), zlim=(0, 0.35),
       xlabel='x', ylabel=r'$\lambda$', zlabel='probability')

# Display the plot
plt.show()
