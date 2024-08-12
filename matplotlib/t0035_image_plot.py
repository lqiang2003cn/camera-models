from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('stinkbug.png'))
print(repr(img))

# return an Axes, a place to draw things
imgplot = plt.imshow(img)

plt.show()