import numpy as np
import matplotlib.pyplot as plt

# Define the response times for each period (morning, afternoon, evening)
response_times = [
    [0.82, 0.76, 0.88, 0.79, 0.81, 0.85, 0.77, 0.83, 0.79, 0.81],  # Morning response times
    [0.75, 0.73, 0.77, 0.72, 0.76, 0.74, 0.76, 0.75, 0.78, 0.73],  # Afternoon response times
    [0.92, 0.88, 0.94, 0.89, 0.95, 0.93, 0.91, 0.94, 0.88, 0.92]   # Evening response times
]

# Set the number of bins in the histogram
n_bins = 10

# Create a figure and define the subplots
fig, ax = plt.subplots()

# Define the colors for the periods
colors = ['blue', 'green', 'orange']

# Create a histogram for each period
for i, period_times in enumerate(response_times):
    ax.hist(period_times, bins=n_bins, density=True, histtype='bar', color=colors[i], label=f'Period {i+1}')

# Add a legend
ax.legend()

# Set the title and labels for the chart
ax.set_title('Response Time Distribution')
ax.set_xlabel('Response Time')
ax.set_ylabel('Density')

# Adjust the layout for better display
fig.tight_layout()

# Display the chart
plt.show()