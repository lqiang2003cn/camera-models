import numpy as np
from matplotlib import pyplot as plt

data = {
  'a': np.arange(50),
  'c': np.random.randint(0, 50, 50),
  'd': np.random.randn(50)
}
data['b'] = data['a'] + np.random.randn(50) * 10
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
