import math
import matplotlib.pyplot as plt
import numpy as np

def square(x):
    valid = []
    for i in x:
        for r in range(100):
            if math.sqrt(i[0] ** 2 + i[1] ** 2) > 2:
                break
            temp = [i[0], i[1]]
            i[0] = (i[0]**2) + (i[1]**2 * -1)
            i[1] = (temp[0] * i[1] * 2)

            a1 = np.array(i)
            a2 = np.array(temp)

            i = a1 + a2
        valid.append(i)
    return valid

div = 1000
loop = 100
colour = 'bone'
c = np.linspace(-2, 2, div)[:, np.newaxis] + 1j*np.linspace(-2, 2, div)[np.newaxis,:]
z = 0
mask = np.ones_like(c, dtype=bool)

ones = np.ones_like(c, dtype=int)
color = (ones * loop) + 5
np.seterr(over='ignore')
np.seterr(invalid='ignore')

for n in range(loop):
    z = z ** 2 + c
    diverged = np.abs(z)>2
    color[diverged] = np.minimum(color[diverged], ones[diverged]*n)

plt.contourf(c.real, c.imag, -color, cmap=colour)
plt.xlabel('Real')
plt.ylabel('i (imaginary)')
plt.xlim(-2, 2)
plt.ylim(-1.5, 1.5)
plt.savefig('mandelbrot.pdf')
plt.show()





