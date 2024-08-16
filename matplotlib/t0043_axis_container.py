from matplotlib import pyplot as plt

fig, ax = plt.subplots()
axis = ax.xaxis
t = axis.get_ticklocs()
print(t)
l = axis.get_ticklabels()
print(l)
ll = axis.get_ticklines()
print(ll)

lm = axis.get_ticklabels(minor=True)
print(lm)
llm = axis.get_ticklines(minor=True)
print(llm)

plt.show()
