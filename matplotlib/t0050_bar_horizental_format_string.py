from matplotlib import pyplot as plt

fruit_names = ['Coffee', 'Salted Caramel', 'Pistachio']
fruit_counts = [4000000, 2000000, 70000000]

fig, ax = plt.subplots()
bar_container = ax.bar(fruit_names, fruit_counts)
ax.set(ylabel='pints sold', title='Gelato sales by flavor', ylim=(-1000, 80000000))
ax.bar_label(bar_container, fmt='{:,.3f}')

plt.show()