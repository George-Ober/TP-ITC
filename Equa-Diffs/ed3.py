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

G = 1
M = 1

def f_vectorielle(Y, t):
    return [Y[1],
            -G*M* Y[0] / ((Y[0] ** 2 + Y[2] ** 2) ** (3/2)) ,
            Y[3],
            -G*M* Y[2] / ((Y[0] ** 2 + Y[2] ** 2) ** (3/2)) ]
m=6*(10**24)
M=2*(10**30)
G=6.8*(10**(-11))

def orbit(f, t):
    x, y, vx, vy = f
    r=sqrt((x**2)+(y**2))
    v=sqrt((vx**2)+(vy**2))
    dx=vx
    dy=vy
    dfx=-G*M*x/(r**3)
    dfy=-G*M*y/(r**3)
    dFdt = [dx, dy, dfx, dfy]
    return dFdt

t=np.linspace(0,3.2*(10**7))
x0=0
y0=1.5*(10**11)
vx0=3*(10**4)
vy0=0
f = odeint(orbit,(x0,y0, vx0, vy0),t)
plt.plot(t,f[:, 0])
#plt.plot(t, f[:,1])
plt.figure()
plt.plot(f[:,1],f[:,0])
plt.show()
# Y = odeint(f_vectorielle, [1, 10, 1, 8], t)
#
# sinus_ref = [sin(x) for x in t]
#
# y_d = Y[:, 0]
#
# # plt.plot(t, sinus_ref, color = 'cyan', linewidth = 9)
#
# plt.plot(t, y_d, linewidth = 1)
#
# plt.grid()
# plt.show()

# Thinkpad X220
