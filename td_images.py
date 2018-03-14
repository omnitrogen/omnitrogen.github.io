from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from itertools import product

#import imageio
#im = imageio.imread("")

im = np.asarray(Image.open(""))

def delete_red_component(image):
    """return image without red component"""
    image[...,0] = 0
    return image

def decomp(image):
    """return 3 lists of integers representing red, green and blue value"""
    return map(lambda x: x.flatten().tolist(), [image[..., 0], image[..., 1], image[..., 2]])

def grey_scale(image):
    """return a grey scale image -> each pixel = (red + green + blue)/3"""
    for i, j in product(range(im.shape[0]), range(im.shape[1])):
        image[i, j][0] , image[i, j][1] , image[i, j][2] = [(int(image[i, j][0]) + int(image[i, j][1]) + int(image[i, j][2])) / 3] * 3
    return image

def reduction(image):
    """resize the image -> only select one row out of p"""
    test = plt.imshow(image)
    title = plt.title("Reduction une ligne sur p")

    axMoins = plt.axes([0.12, 0.01, 0.1, 0.05])
    axPlus = plt.axes([0.22, 0.01, 0.1, 0.05])

    class Index(object):
        p = 1

        def plus(self, event):
            self.p += 1
            test.set_data(image[::int(self.p)])
            title.set_text("p = {}".format(str(self.p)))
            plt.draw()

        def moins(self, event):
            if self.p >= 2:
                self.p -= 1
            test.set_data(image[::int(self.p)])
            title.set_text("p = {}".format(str(self.p)))
            plt.draw()


    callback = Index()
    bnext = Button(axPlus, 'p += 1')
    bnext.on_clicked(callback.plus)
    bprev = Button(axMoins, 'p -= 1')
    bprev.on_clicked(callback.moins)

    plt.show()
    pass

def rotate_90(image, n):
    """rotate the pic n * pi/2 times"""
    return np.rot90(image, n)

def inverser(image):
    """reverse black and white colors"""
    for i in np.nditer(image, op_flags=['readwrite']):
        i[...] = 255 - i
    return image

def rapproch_extreme(image):
    """bring extreme closer (so cute)"""
    for i in np.nditer(image, op_flags=['readwrite']):
        i[...] = abs(127 - i)
    return image

def filtrage(image):
    """mean of all the pixels around one pixel"""
    for i, j in product(range(image.shape[0]), range(image.shape[1])):
        image[i, j] = [round(sum(v) / len(v)) for v in zip(*[image[i + x, j + y].tolist() for (x, y) in product(range(-1, 2), range(-1,2)) if 0 <= (i+x) and (i + x) < image.shape[0] and 0 <= (j+y) and (j+y) < image.shape[1]])]
    return image


# image initiale
plt.imshow(im)
plt.xlabel((" ".join(["size: ", str(im.shape[0]), "x", str(im.shape[1]), "(format (y,x))"])))
plt.title("Image initiale")
plt.show()

# entiers codant les couleurs R, V, B
lr, lv, lb = decomp(im.copy())
#print(lr, lv, lb) # deconseille car bcp de valeurs
plt.text(.01, .75, "Lr: {0}".format([lr[i] for i in range(10)] + [" ... "] + [lr[i] for i in range(lr.__len__() - 10, lr.__len__())]), clip_on=True, fontsize=8)
plt.text(.01, .5, "Lv: {0}".format([lv[i] for i in range(10)] + [" ... "] + [lv[i] for i in range(lv.__len__() - 10, lv.__len__())]), clip_on=True, fontsize=8)
plt.text(.01, .2, "Lb: {0}".format([lb[i] for i in range(10)] + [" ... "] + [lb[i] for i in range(lb.__len__() - 10, lb.__len__())]), clip_on=True, fontsize=8)
plt.axis('off')
plt.title("Listes Lr, Lv, Lb des entiers codant les couleurs R, V, B")
plt.show()

# image sans sa composante rouge
withoutRed = delete_red_component(im.copy())
plt.imshow(withoutRed)
plt.title("Image sans sa composante rouge")
plt.show()

# niveau de gris
grey = grey_scale(im.copy())
plt.imshow(grey)
plt.title("Niveau de gris")
plt.show()

# selectionne une ligne sur p
reducted = reduction(im.copy())

# reduit en ne prenant qu'une ligne sur p
plt.imshow(im.copy()[::3])
plt.show()

# image retournee de 180 deg
rotated = rotate_90(im.copy(), 2)
plt.imshow(rotated)
plt.title("Image retournee de 180 deg")
plt.show()

# tete de viole verticale
vertical = rotate_90(im.copy(), -1)
plt.imshow(vertical)
plt.title("Tete de viole verticale")
plt.show()

# inverse les niveaux de gris
inverse = inverser(grey.copy())
plt.imshow(inverse)
plt.title("Inverse les niveaux de gris")
plt.show()

# rapprochement des extremes
extreme = rapproch_extreme(im.copy())
plt.imshow(extreme)
plt.title("Rapprochement des extremes")
plt.show()

# filtrage: remplace chaque pixel d’une image en nuances de gris par la moyenne des pixels qui lui sont voisins
filtre = filtrage(grey.copy())
plt.imshow(filtre)
plt.title("Filtre moyenne des pixels voisins (sorte de flou ou aplanissement)")
plt.xlabel("Flou pour les images petites et aplanissement pour les images plus grandes")
plt.show()

print("end")
