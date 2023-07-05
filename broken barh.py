import matplotlib.pyplot as plt
import matplotlib.image as image
import pandas as pd
import numpy as np

#Defining the x and y ranges
xranges = [(5,5), (20,5),(20,7)]
yrange = (2,1)
#Plotting the broken bar chart
plt.broken_barh(xranges, yrange, facecolors='green')
xranges = [(6,2), (17,5),(50,2)]
yrange = (15,1)
plt.broken_barh(xranges, yrange, facecolors='orange')
xranges = [(5,2), (28,5),(40,2)]
yrange = (30,1)
plt.broken_barh(xranges, yrange, facecolors='red')
plt.xlabel('Sales')
plt.ylabel('Days of the Month')
plt.show()