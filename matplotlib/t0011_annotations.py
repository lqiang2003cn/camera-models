import numpy as np
from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(5, 2.7))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(3.5, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))
ax.set_ylim(-2, 2)
plt.show()
