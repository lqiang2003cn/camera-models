import numpy as np
from matplotlib import pyplot as plt

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(figsize=(5, 2.7))
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
l.set_linestyle(':')  # from setter
plt.show()
