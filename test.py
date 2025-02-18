import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Sample data
x = np.linspace(0, 10, 100)
y = np.linspace(0.999, 1.001, 100)

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y)

formatter = ScalarFormatter()
formatter.set_useOffset(1)
# identical to formatter = ScalarFormatter(useOffset=1)
ax.yaxis.set_major_formatter(formatter)

plt.show()