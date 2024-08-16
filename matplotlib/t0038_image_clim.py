import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('stinkbug.png'))
print(img)

# luminosity
lum_img = img[:, :, 0]
print(lum_img)

r = lum_img.ravel()

# plt.imshow(lum_img, clim=(0, 175))
im = plt.imshow(lum_img)
im.set_clim(0, 175)
plt.colorbar()

plt.show()
