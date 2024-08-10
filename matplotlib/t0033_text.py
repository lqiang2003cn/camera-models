import numpy as np
from matplotlib import pyplot as plt

mu, sigma = 100, 15
np.random.seed(42)
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('Smart', fontsize=14, color='red')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([0, 200, 0, 0.03])
plt.grid(True)
plt.show()