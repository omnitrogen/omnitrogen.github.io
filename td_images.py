import imageio
import numpy as np
import matplotlib.pyplot as plt
from itertools import product


im = imageio.imread("tete2.jpg")

def delete_red_component(im):
    image = im.copy()
    image[...,0] = 0
    return image

def decomp(image):
    """return 3 lists of integers representing red, green and blue value"""
    return map(lambda x: x.flatten().tolist(), [image[..., 0], image[..., 1], image[..., 2]])

def grey_scale(im):
    """return a grey scale image -> each pixel = (red + green + blue)/3"""
    image = im.copy()
    for i, j in product(range(im.shape[0]), range(im.shape[1])):
        image[i, j][0] , image[i, j][1] , image[i, j][2] = [(int(image[i, j][0]) + int(image[i, j][1]) + int(image[i, j][2])) / 3] * 3
    return image

def reduction(im, p):
    """resize the image while only selecting one row out of p"""
    pass

def rotate_90(im, n):
    """rotate the pic n * pi/2 times"""
    image = im.copy()
    return np.rot90(image, n)

def inverser(im):
    """reverse black and white colors"""
    image = im.copy()
    for i in np.nditer(image, op_flags=['readwrite']):
        i[...] = 255 - i
    return image

def rapproch_extreme(im):
    """bring extreme closer (so cute)"""
    image = im.copy()
    for i in np.nditer(image, op_flags=['readwrite']):
        i[...] = abs(127 - i)
    return image

def filtrage(im):
    """mean of all the pixels around one pixel"""
    image = im.copy()
    for i, j in product(range(im.shape[0]), range(im.shape[1])):
        image[i, j] = [round(sum(v) / len(v)) for v in zip(*[im[i + x, j + y].tolist() for (x, y) in product(range(-1, 2), range(-1,2)) if 0 <= (i+x) and (i + x) < im.shape[0] and 0 <= (j+y) and (j+y) < im.shape[1]])]
    return image


# image initiale
plt.imshow(im)
plt.xlabel((" ".join(["size: ", str(im.shape[0]), "x", str(im.shape[1]), "(format (y,x))"])))
plt.title("Image initiale")
plt.show()

# entiers codant les couleurs R, V, B
lr, lv, lb = decomp(im)
#print(lr, lv, lb)

# image sans sa composante rouge
withoutRed = delete_red_component(im)
plt.imshow(withoutRed)
plt.title("Image sans sa composante rouge")
plt.show()

# niveau de gris
grey = grey_scale(im)
plt.imshow(grey)
plt.title("Niveau de gris")
plt.show()

# image retournee de 180 deg
rotated = rotate_90(im, 2)
plt.imshow(rotated)
plt.title("Image retournee de 180 deg")
plt.show()

# tete de viole verticale
vertical = rotate_90(im, -1)
plt.imshow(vertical)
plt.title("Tete de viole verticale")
plt.show()


# inverse les niveaux de gris
inverse = inverser(grey)
plt.imshow(inverse)
plt.title("Inverse les niveaux de gris")
plt.show()

# rapprochement des extremes
extreme = rapproch_extreme(im)
plt.imshow(extreme)
plt.title("Rapprochement des extreme")
plt.show()


# filtrage: remplace chaque pixel d’une image en nuances de gris par la moyenne des pixels qui lui sont voisins
filtre = filtrage(grey)
plt.imshow(filtre)
plt.title("Filtre moyenne des pixels voisins (sorte de flou ou aplanissement)")
plt.show()

print("end.")
