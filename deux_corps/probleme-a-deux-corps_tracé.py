"""Modélisation Python du mouvement d'une planète dans le champs gravitationnel d'une étoile"""

from math import *
import matplotlib.pyplot as plt
import numpy as np


# coordonnées polaires


mu = 0.001 #masse relative de la planète par rapport à l'étoile

v0 = 3351 #km/mois    vitesse approximative de la Terre
R = 6400
omega0 = v0 / R
x0, y0 = R/sqrt(2) + R, R/sqrt(2) + R/2


Lt = np.array([i/2 for i in range(28)])
Lx = []
Ly = []

for k in range(len(Lt)) :
    Lx.append(R * cos((omega0 * Lt[k])) + x0)
    Ly.append(R * sin((omega0 * Lt[k])) + y0)

plt.plot(Ly, Lx, '+')
plt.legend("distances en km")
plt.title("Mouvement d'une planète en rotation autour d'une étoile")
