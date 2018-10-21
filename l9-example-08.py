import matplotlib.pyplot as plt

img = plt.imread('testimage.jpg')

print 'type:',type(img)
print 'shape:',img.shape
print 'datatype:',img.dtype

plt.imshow(img)
plt.show()

