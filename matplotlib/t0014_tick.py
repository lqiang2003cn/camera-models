import numpy as np
from matplotlib import pyplot as plt

data1, data2, data3, data4 = np.random.randn(4, 100)

# two rows and one column
fig, axs = plt.subplots(2, 1, layout='constrained')
xdata = np.arange(len(data1))  # make an ordinal for this

axs[0].plot(xdata, data1)
axs[0].set_title('Automatic ticks')

axs[1].plot(xdata, data1)
axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
axs[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
axs[1].set_title('Manual ticks')
plt.show()
