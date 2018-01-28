'''
import time

def bubbleSort(liste):
    for num in range(len(liste)-1,0,-1):
        for i in range(num):
            if liste[i] > liste[i+1]:
                liste[i],liste[i+1] = liste[i+1], liste[i]

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

start = time.time()
bubbleSort([54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20])
end = time.time()
print("bubbleSort: {}".format(end - start))

start2 = time.time()
quicksort([54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20])
end2 = time.time()
print("quicksort: {}".format(end2 - start2))
'''

'''
def creer_pile(c):
    p = (c+1) * [None]
    p[0] = 0
    return p

def empiler(p,v):
    n = p[0]
    assert n < len(p) - 1
    n += 1
    p[0] = n
    p[n] = v

def depiler(p):
    n = p[0]
    assert n > 0
    p[0] = n - 1
    a = p[n]
    p[n] = None
    return a

def taille(p):
    return p[0]

def pile_vide(p):
    return taille(p) == 0

def sommet(p):
    assert taille(p) > 0
    return p[p[0]]

m = creer_pile(6)
print(m)
'''

class Pile(object):
    """Class representing an unlimited pile. A pile is ruled by the LIFO rule (last in, first out)"""
    def __init__(self):
        self.p = []

    def show(self):
        return self.p

    def empiler(self, *args):
        for arg in args:
            self.p.append(arg)

    def depiler(self):
        return self.p.pop()

    def taille(self):
        return len(self.p)

    def pile_vide(self):
        return taille(self.p) == 0

    def sommet(self):
        return self.p[-1]

