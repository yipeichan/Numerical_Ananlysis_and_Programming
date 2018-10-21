import matplotlib.pyplot as plt

img = plt.imread('testimage.jpg')

# convert to [0-1] array 
tmp = img.astype('float64')/255. 

# make 40x40 mosaic
n = 40
for i in range(0,img.shape[0],n):
    for j in range(0,img.shape[1],n):
        tmp[i:i+n,j:j+n,:] = tmp[i:i+n,j:j+n,:].mean((0,1))

plt.imshow(tmp)
plt.show()