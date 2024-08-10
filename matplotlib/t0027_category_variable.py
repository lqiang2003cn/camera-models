from matplotlib import pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

# figure size: width * height
plt.figure(figsize=(12, 3))

# 1 row, 3 column, first column
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()