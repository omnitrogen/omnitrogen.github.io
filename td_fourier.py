import math as mt
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

cree_liste = lambda x: [0 for i in range(x)]
porte = lambda x: 1 if -0.5 < x < 0.5 else 0
portes = lambda x: 1 if -0.5 < x < 0.5 else (0.8 if 0.7 < x < 1.7 else 0)

