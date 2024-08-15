from matplotlib import pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax2 = fig.add_axes([0.1, 0.1, 0.7, 0.3])

for ax in fig.axes:
  ax.grid(True)

plt.show()
