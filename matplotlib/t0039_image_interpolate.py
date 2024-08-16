from PIL import Image
from matplotlib import pyplot as plt

img = Image.open('stinkbug.png')
img.thumbnail((64, 64))  # resizes image in-place
# imgplot = plt.imshow(img)
# imgplot = plt.imshow(img, interpolation="bilinear")
imgplot = plt.imshow(img, interpolation="bicubic")
# plt.colorbar()
plt.show()