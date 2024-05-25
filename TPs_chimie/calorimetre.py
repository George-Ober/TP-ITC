# Léo KHAYAT et George OBER

from numpy import *
import matplotlib.pyplot as plt
from scipy import stats

# Il y a deux mesures

T_1 = [24.4, 24.4, 24.5, 24.5, 24.5, 24.9, 25.0, 25.2, 25.2, 25.4, 25.5, 25.6, 25.7, 25.9, 26.2, 26.7, 26.8, 26.8, 27.2, 27.7, 27.8, 27.8, 27.9, 27.9, 28.0, 28.7, 28.9, 29.0, 28.7, 28.6, 29.0, 29.2, 29.2, 29.5, 30.5, 30.9, 31.5, 31.5, 31.4, 32.1, 33.0, 33.2, 32.8, 33.6, 33.7]

T_2 = [26.60, 26.90, 26.40, 26.10, 26.00, 26.20, 26.30, 26.40, 26.40, 26.70, 26.80, 26.90, 27.00, 27.30, 27.70, 28.20, 28.40, 28.50, 28.80, 29.10, 29.30, 29.40, 29.70, 29.90, 30.00, 30.40, 30.60, 30.70, 30.70, 31.00, 31.30, 31.40, 31.50, 31.80, 31.90, 32.00, 32.50, 32.70, 32.50, 32.40, 33.10, 33.40, 33.60, 33.70, 34.20, 34.50, 34.60, 34.80, 34.90, 35.00, 35.00, 35.30, 35.30, 35.70, 35.80, 36.40, 36.00, 36.20, 36.40, 36.70]


t_1 = [5*k for k in range(len(T_1))]
t_2 = [5*k for k in range(len(T_2))]

lr = stats.linregress(t_2, T_2)

pente = lr[0] #K.s^-1
ordonnee_orig = lr[1]

m_eau = 0.2 # kg
U = 10 #Volts
I = 2 #Amperes
c_cal = 90 #J.K^-1  valeur du constructeur

c_eau = ((U*I / pente) - c_cal) / m_eau

print(pente, ordonnee_orig, c_eau)

Yd = []
for t in t_2:
    Yd.append(pente*t + ordonnee_orig)

plt.plot(t_2, T_2, color = 'green',
    marker = '+', markeredgewidth = 2,
    markersize = 8, markeredgecolor = 'black')
plt.plot(t_2, Yd, color = "black")

plt.title('Calorimétrie\n')
plt.xlabel('$t$')
plt.ylabel('$T$')
plt.grid()

plt.savefig('Courbe_calorimetrie.pdf')
plt.show()
