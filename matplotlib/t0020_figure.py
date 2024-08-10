from matplotlib import pyplot as plt

fig = plt.figure(figsize=(4, 3), facecolor='lightskyblue', layout='constrained')
fig.suptitle('A nice Matplotlib Figure')
ax = fig.add_subplot()
ax.set_title('Axes', loc='center', fontstyle='oblique', fontsize='medium')
plt.show()
