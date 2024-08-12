import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('stinkbug.png'))
print(img)

# luminosity
lum_img = img[:, :, 0]
print(lum_img)

# 1. cmap
# plt.imshow(lum_img, cmap="hot")

# 2. set_cmap
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
plt.colorbar()

plt.show()
