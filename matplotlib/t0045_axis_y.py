import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(100 * np.random.rand(20))

# Use automatic StrMethodFormatter
ax.yaxis.set_major_formatter('${x:1.3f}')

ax.yaxis.set_tick_params(which='major', labelcolor='green', labelleft=False, labelright=True)

plt.show()
