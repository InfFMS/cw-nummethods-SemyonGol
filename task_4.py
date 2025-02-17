#x1 = 6.1406*10^(-5)
#x2 = 0.0001004
#x3 = 0.0001948

import numpy as np
import matplotlib.pyplot as plt

def f(V, T):
    return R*T/(V-b)- a/V**2 - P1

print('Enter minimum of x:', end=' ')
a1 = float(input())
a2 = a1
print('Enter maximum of x:', end=' ')
b1 = float(input())
b2 = b1

a = 0.1382
b = 3.19*10**(-5)
R = 8.314
T = 143.15
eps = 10**(-7)
P1 = 3664186.998
unsolved = True

V = np.linspace(b + 10 ** (-5), 10 ** (-3), 1000)
P = f(V, T)

while unsolved:
    c = (a1 + b1) / 2
    if f(c, T)*f(a1, T) < 0:
        b1 = c
    else:
        a1 = c
    if abs((b1 - a1)) / 2 <= eps:
        print('x ≈', c)
        unsolved = False

plt.plot(V, P)
plt.grid()
plt.show()