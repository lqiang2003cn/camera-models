import numpy as np
from matplotlib import pyplot as plt

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)

#
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(7, 2.7), layout='constrained')
l1, = ax1.plot(t, s)
ax2 = ax1.twinx()  # reuse x axis
l2, = ax2.plot(t, range(len(t)), 'C1')  # plot new y
ax2.legend([l1, l2], ['Sine (left)', 'Straight (right)'])

ax3.plot(t, s)
ax3.set_xlabel('Angle [rad]')
ax4 = ax3.secondary_xaxis('top', functions=(np.rad2deg, np.deg2rad))
ax4.set_xlabel('Angle [°]')
plt.show()
