import math as mt
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#cree_liste = lambda x: [0 for i in range(x)]
#porte = lambda x: 1 if -0.5 < x < 0.5 else 0
#portes = lambda x: 1 if -0.5 < x < 0.5 else (0.8 if 0.7 < x < 1.7 else 0)

n = 4

# definition de a
a = np.zeros(n)
a[2] = 1

plt.subplot(311)
plt.plot( np.append(a, a[0]) )

A = np.fft.fft(a)
B = np.append(A, A[0])

plt.subplot(312)
plt.plot(np.real(B))
plt.ylabel("partie reelle")

plt.subplot(313)
plt.plot(np.imag(B))
plt.ylabel("partie imaginaire")

plt.show()

a = np.zeros(8)
a[2] = 1
a[3] = 2
a[4] = 1
a[5] = 1
a[6] = 1

plt.subplot(311)
plt.plot( np.append(a, a[0]) )

A = np.fft.fft(a)
B = np.append(A, A[0])

plt.subplot(312)
plt.plot(np.real(B))
plt.ylabel("partie reelle")

plt.subplot(313)
plt.plot(np.imag(B))
plt.ylabel("partie imaginaire")

plt.show()