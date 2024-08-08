import numpy as np
from matplotlib import pyplot as plt

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(np.arange(len(data1)), data1, label='data1')
ax.plot(np.arange(len(data2)), data2, label='data2')
ax.plot(np.arange(len(data3)), data3, 'd', label='data3')
ax.legend()
plt.show()
