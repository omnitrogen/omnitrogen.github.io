import math as mt
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# np.zeros(N,dtype=complex)

def f():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    a = np.zeros(5)
    a[2] = 1

    ax.plot([i for i in range(-2, 3)], a)

    #ax.plot([i for i in range(-2, 3)], [0, 0, 1, 0, 0])
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.show()
    pass

f()

def g():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    a = np.zeros(9)
    a[2] = 1
    a[3] = 2
    a[4] = 1
    a[5] = 1
    a[6] = 1

    ax.plot([i for i in range(-3, 6)], a)

    #ax.plot([i for i in range(-3, 6)], [0, 0, 1, 2, 1, 1, 1, 0, 0])
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.show()
    pass

g()