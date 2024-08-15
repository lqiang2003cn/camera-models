import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

n, bins, rectangles = ax.hist(np.random.randn(1000), 50)

ax.patch.set_facecolor('blue')

print(len(ax.patches))
ax.tick_params(axis='x', labelcolor='orange')
plt.show()
