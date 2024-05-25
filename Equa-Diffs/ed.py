from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from math import *

def f(u, t):
    return u


t = np.linspace(0, 2 * pi, 50)

# Y = odeint(f, 1, t)
# Y_th = [exp(x + 3) for x in t]

# plt.plot(t, Y_th, color = 'cyan', linewidth = 7)
# plt.plot(t, Y)

def f_vectorielle(Y, t):
    return [Y[1], -Y[0]]

Y = odeint(f_vectorielle, [0, 1], t)

sinus_ref = [sin(x) for x in t]

plt.plot(t, sinus_ref, color = 'cyan', linewidth = 9)

plt.plot(t, Y, marker = 'o')

plt.grid()
plt.show()

# Thinkpad X220
