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
        
        
    def deg(self):
        return self.coefficients.__len__() - 1
