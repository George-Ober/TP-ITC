from numpy import *
import matplotlib.pyplot as plt
# Dosage d'oxydoréduction.
#
#   \ /
#   | |
#   |X|
#   |X|
#   |X|
#   |X|
#   |X|
#   |X|  <--- Solution titrante d'ions cériques Ce^(4+)
#   |X|       de concentration 10^(-2) mol/L
#   |X|       La réaction support s'écrit
#   |X|
#   |X|                 2+     4+        3+     3+
#   |X|               Fe   + Ce   <--> Fe   + Ce
#   |X|
#   |X|
#   |X|
#   |X|
#   |X|
#   |X|
#   |X|        ______________
#   |X|       |  1164 mV  o o|  <---- Voltmètre, mesure
#   ---I     /|______________|        le potentiel du milieu réactionnel
#   \ /     /
#          /
#  |      ||  /
#  |      || |  <---  Bécher contenant une solution d'ions Fer II
#  |------||-|        de concentration c0 = 10^(-2) mol/L
#  | /  / || |        éventuellement dilué dans de l'eau désionisée
#  |         |
#  |___@@@___|
# 
#

X = [0, 1, 2, 3, 4.2, 5, 6, 7, 7.5, 8.1, 8.5, 9, 9.5, 10, 10.6, 10.9, 11.2, 11.5, 12.0, 12.5, 13.0, 13.9, 14.8, 16.0, 17.0, 18.0, 18.9, 20.1, 21.0, 22.0, 23.1, 24.0, 25.0]

Y = [258, 322, 346, 355, 370, 377, 386, 398, 402, 414, 418, 423, 441, 467, 905, 950, 968, 985, 1000, 1015, 1025, 1040, 1055, 1069, 1082, 1089, 1096, 1104, 1109, 1115, 1120, 1125, 1128]

E = [u + 230 for u in Y]

plt.plot(X, E, color = '#dd00ff',
    marker = '+', markeredgewidth = 2,
    markersize = 8, markeredgecolor = 'black')

plt.title('Dosage\n')
plt.xlabel('Volume de $Ce(IV)$ versé en mL')
plt.ylabel('Potentiel $E$')
plt.grid()

plt.savefig('Courbe_Redox.pdf')
plt.show()
