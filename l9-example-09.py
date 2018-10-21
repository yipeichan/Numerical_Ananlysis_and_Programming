import matplotlib.pyplot as plt

img = plt.imread('testimage.jpg')

plt.figure(figsize=(4, 9), dpi=80) 

img_r = img.copy()
img_r[...,...,1] = 0
img_r[...,...,2] = 0

img_g = img.copy()
img_g[...,...,0] = 0
img_g[...,...,2] = 0

img_b = img.copy()
img_b[...,...,0] = 0
img_b[...,...,1] = 0

plt.subplot(3,1,1)
plt.imshow(img_r)

plt.subplot(3,1,2)
plt.imshow(img_g)

plt.subplot(3,1,3)
plt.imshow(img_b)

plt.show()

