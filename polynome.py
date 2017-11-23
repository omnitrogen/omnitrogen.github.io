from itertools import zip_longest

class Polynome(object):
    """docstring for Polynome"""
    def __init__(self, coefficients):
        self.coefficients = [float(i) for i in coefficients]

    def __str__(self):
        string = ''
        for i, v in enumerate(self.coefficients):
            if v != 0:
                string += str(v) + " "
                string += "X^" + str(i)
                if i < sorted([i for i,v in enumerate(self.coefficients) if v != 0])[-1]:
                    string += " + "
            string = string.replace('X^0', '')
            string = string.replace('X^1', 'X')
            string = string.replace('  +', ' +')
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

p1 = Polynome([1, 1, 2, 0, 0, 3, 0, 4, 0, 0, 0, 0])
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

    def __str__(self):
        pass

bruh = FracRat([33, 44, 55], [66, 77, 88, 99])
print(bruh.coefficients)
        