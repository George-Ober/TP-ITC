import matplotlib.pyplot as plt
from scipy import stats


X = [k*60 for k in range(30 + 1)]

Y = [8.33, 8.29, 8.26 8.23, 8.19, 8.16, 8.12, 8.09, 8.05, 8.02, 7.99, 7.96, 7.93, 7.90, 7.86, 7.83, 7.80, 7.78, 7.75, 7.71, 7.68, 7.65, 7.61, 7.58, 7.55, 7.53, 7.49, 7.43, 7.40, 7.37]

lr = stats.lineregress(X, Y)

pente = lr[0]
ord_orig = lr[1]
corr = lr[2]

print('Le coefficient de correlation est :', corr)

Yd = []
for x in X:
    Yd.append(pente*x + ord_orig)

#LIMITES DES AXES
plt.xlim(-1, 6)
plt.ylim(-1, 6)

plt.title('Régression linéaire')

plt.plot(X, Y, marker = "o", color = "black")
plt.plot(X, Yd, color = "black")

plt.savefig('Régression.pdf')
plt.show()