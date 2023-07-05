import numpy as np
import matplotlib.pyplot as plt

# We set the seed to reproduce the results
np.random.seed(19680801)

# We define the number of categories and the number of bins in the histogram
n_bins = 10

# We generate our data using np.random.randn()
# We have 1000 samples, and each sample has 3 coordinates
x = np.random.randn(1000, 3)

# We create a figure and define the sub-screens
fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

# We define the colors for the categories
colors = ['red', 'tan', 'lime']

# Define a histogram with bars and add the number of bins, density=True to have a normalized density,
# histtype='bar' to have bars and color for the colors of the bars
ax0.hist(x, bins=n_bins, density=True, histtype='bar', color=colors, label=colors)

# We add the legend with font size 10
ax0.legend(prop={'size': 10})

# We set the title of the sub-screen
ax0.set_title('bars with legend')

# We create a histogram with bars and stacked=True to have cumulative bars
ax1.hist(x, bins=n_bins, density=True, histtype='barstacked')

# We set the title of the sub-screen
ax1.set_title('stacked bar')

# We create a histogram with line shapes (step) and stacked=True for cumulative lines,
# while fill=False to not fill lines
ax2.hist(x, bins=n_bins, histtype='step', stacked=True, fill=False)

# We set the title of the sub-screen
ax2.set_title('stack step (unfilled)')

# We create a bar histogram for different numbers of samples in each category
x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
ax3.hist(x_multi, bins=n_bins, histtype='bar')

# We set the title of the sub-screen
ax3.set_title('different sample sizes')

# Adjust the layout of the subplots for better display
fig.tight_layout()

# We display the chart
plt.show()