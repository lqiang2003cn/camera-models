import matplotlib.pyplot as plt
import numpy as np


plt.rcParams.update({'figure.autolayout': True})


def currency(x, pos):
  """The two arguments are the value and tick position"""
  if x >= 1e6:
    s = f'${x * 1e-6:1.1f}M'
  else:
    s = f'${x * 1e-3:1.0f}K'
  return s


data = {
  'Barton LLC': 109438.50,
  'Frami, Hills and Schmidt': 103569.59,
  'Fritsch, Russel and Anderson': 112214.71,
  'Jerde-Hilpert': 112591.43,
  'Keeling LLC': 100934.30,
  'Koepp Ltd': 103660.54,
  'Kulas Inc': 137351.96,
  'Trantow-Barrows': 123381.38,
  'White-Trantow': 135841.99,
  'Will LLC': 104437.60
}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

# use a style before plotting the subplots
print(plt.style.available)
plt.style.use('fivethirtyeight')

fig, ax = plt.subplots(figsize=(16, 8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

# Add a vertical line, here we set the style in the function call
ax.axvline(group_mean, ls='--', color='r')

# Annotate new companies: in the order of the data dictionary
for group in [1, 5, 7]:
  ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")

# Now we move our title up since it's getting a little cramped
ax.title.set(y=1.05)

ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company', title='Company Revenue')
ax.xaxis.set_major_formatter(currency)
ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
# fig.subplots_adjust(right=.1)

plt.show()
