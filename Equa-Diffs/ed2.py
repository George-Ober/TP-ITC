from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from math import *

def f(u, t):
    return u


# t = np.linspace(0, 2 * pi, 50)
t = np.linspace(0, 300, 5000)

# Y = odeint(f, 1, t)
# Y_th = [exp(x + 3) for x in t]

# plt.plot(t, Y_th, color = 'cyan', linewidth = 7)
# plt.plot(t, Y)

# Résolution de y'''' + y''' + y'' + y' + y = 0

def f_vectorielle(Y, t):
    return [Y[1], -3 * Y[1] - Y[0] + sin(2*pi*t)]

Y = odeint(f_vectorielle, [0, 1], t)

sinus_ref = [sin(x) for x in t]

y_d = Y[:, 0]

# plt.plot(t, sinus_ref, color = 'cyan', linewidth = 9)

plt.plot(t, y_d, linewidth = 1)

plt.grid()
plt.show()

# Thinkpad X220
