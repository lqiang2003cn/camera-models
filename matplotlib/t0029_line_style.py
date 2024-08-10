from matplotlib import pyplot as plt

x = [1, 2, 3, 4]
y = [2, 3, 4, 2]
line, = plt.plot(x, y, '-')
line.set_antialiased(False)  # turn off antialiasing
plt.show()
