#P(V, T) = RT/(V-b) - a/V^2

import numpy as np
import matplotlib.pyplot as plt

n = 0
a = 0.1382
b = 3.19*10**(-5)
R = 8.314
T = np.array([-140, -130, -120, -110, -100])
Vcr = 3*b
Pcr = a/(27*b**2)
Tcr = 8*a/(27*R*b)

V = np.linspace(b + 10 ** (-5), 10 ** (-3), 2000)
T += 273
fig, axs = plt.subplots(3, 2, figsize=(10, 15))

for i in range(len(T)):
    P = R*T[i]/(V-b) - a/V**2
    axs[n, i%2].plot(V, P)
    axs[n, i%2].set_xlabel('Объём')
    axs[n, i%2].set_ylabel('Давление')
    axs[n, i % 2].set_title(f'T = {T[i]:.1f} K')
    if i%2 == 1:
        n += 1

plt.show()