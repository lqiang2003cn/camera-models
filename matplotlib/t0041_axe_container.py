import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()
rect = ax.patch  # a Rectangle instance
rect.set_facecolor('green')

x, y = np.random.rand(2, 100)
line, = ax.plot(x, y, '-', color='blue', linewidth=2)
plt.show()
