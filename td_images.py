import imageio
import numpy as np
import matplotlib.pyplot as plt

im = imageio.imread("tete2.jpg")

def decomp(image):
    return image[..., 0], image[..., 1], image[..., 2]

def grey_scale(image):
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            mean = (int(image[i, j][0]) + int(image[i, j][1]) + int(image[i, j][2])) / 3
            image[i, j][0] , image[i, j][1] , image[i, j][1] = mean, mean, mean
    return image

def reduction(image, p):


#plt.imshow(im)
#plt.show()

#print(decomp(im))

# lr, lv, lb = decomp(im)
# print(lr, lv, lb)

# imageio.imwrite("testest0.png", lr)
# imageio.imwrite("testest1.png", lv)
# imageio.imwrite("testest2.png", lb)

image = grey_scale(im)
imageio.imwrite("blahfefsfs.png", image)

print(im.shape)
