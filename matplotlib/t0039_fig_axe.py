import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

# set the position of the next subplot: 0-1 relative
# fig.subplots_adjust(top=1)
ax1 = fig.add_subplot(211)
ax1.set_ylabel('Voltage [V]')
ax1.set_title('A sine wave')

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax1.plot(t, s, color='blue', lw=2)

# Fixing random state for reproducibility
np.random.seed(19680801)

ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
n, bins, patches = ax2.hist(np.random.randn(1000), 50, facecolor='yellow', edgecolor='blue')
ax2.set_xlabel('Time [s]')

plt.show()