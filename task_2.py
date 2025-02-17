import numpy as np
import matplotlib.pyplot as plt

a = 0.1382
b = 3.19*10**(-5)
R = 8.314
T = -130 + 273

V = np.linspace(b + 10 ** (-5), 10 ** (-3), 2000)
P = R*T/(V-b) - a/V**2

locmin = min(P)
locmax = max(P)
print(f'Локальный минимум: {locmin/1000:.2f} кПа \n Локальный максимум:  {locmax/1000:.2f} кПа')
plt.plot(V, P)
plt.show()