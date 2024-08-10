from matplotlib import pyplot as plt

x1 = [1, 2, 3, 4]
y1 = [2, 3, 4, 2]
x2 = [1, 2, 3, 4]
y2 = [20, 13, 40, 1]
lines = plt.plot(x1, y1, x2, y2)
# use keyword arguments: set properties
plt.setp(lines, color='r', linewidth=3.0)
plt.show()
