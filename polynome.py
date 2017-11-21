from itertools import zip_longest

class Polynome(object):
    """docstring for Polynome"""
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        string = ''
        for i, v in enumerate(self.coefficients):
            if i == 0:
                string += str(v)
            elif i == 1:
                string += str(v) + " X"
            else:
                string += str(v) + " X^" + str(i)
            if i < self.coefficients.__len__() - 1:
                string += " + "
        return string

    def __add__(self, autre_polynome):
        return Polynome([x + y for x, y in zip_longest(self.coefficients, autre_polynome.coefficients, fillvalue=0)])

    def __call__(self, x):
        px = 0
        for i,v in enumerate(self.coefficients):
            px += v * (x ** i)  
        return px
        
    def deg(self):
        return self.coefficients.__len__() - 1

p1 = Polynome([1,2,3])
print(p1)
print(p1.deg())
p2 = Polynome([4,5,6,7])
somme = p1 + p2
print(somme)
print(somme.deg())
print(somme(4))


class FracRat(Polynome):
    """docstring for FracRat"""
    def __init__(self, coeffs1, coeffs2):        
        pass


bruh = FracRat([33, 44, 55], [66, 77, 88, 99])
print(bruh.poly1, bruh.poly2)
        