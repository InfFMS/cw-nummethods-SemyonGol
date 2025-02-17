import numpy as np
import matplotlib.pyplot as plt

def f(V, T):
    return R*T/(V-b)- a/V**2

a = 0.1382
b = 3.19*10**(-5)
R = 8.314
T = 143
l = 0
eps = 0.001

V = np.linspace(b + 10 ** (-5), 10 ** (-3), 2000)
P = f(V, T)


for i in range(len(P)):
    if P[i] == min(P):
        x = V[i]
        break

while x >= min(V):
    l += (eps**2 + (f(x, T) - f(x+eps, T))**2)**0.5
    x -= eps
print(f' Длина равна: {l:.3f}')

plt.plot(V, P)
plt.show()