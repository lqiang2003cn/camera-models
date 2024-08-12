import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('stinkbug.png'))
print(img)

# luminosity
lum_img = img[:, :, 0]
print(lum_img)

r = lum_img.ravel()

# bins 0 to 225
plt.hist(r, bins=range(256), fc='k', ec='k')

plt.show()
