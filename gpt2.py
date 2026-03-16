# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:39:18 2026

@author: praymond
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# -----------------------------
# Paramètres du problème
# -----------------------------
mu = 0.000003          # rapport de masse
omega = 1.0       # vitesse angulaire normalisée

# Positions des deux corps
x1, y1 = -mu, 0.0
x2, y2 = 1 - mu, 0.0

# -----------------------------
# Équations du PR3C
# -----------------------------
def pr3c(state, t):
    x, y, vx, vy = state

    # Distances aux deux corps
    r1 = np.sqrt((x + mu)**2 + y**2)
    r2 = np.sqrt((x - (1 - mu))**2 + y**2)

    # Accélérations dans le repère tournant
    ax = (2 * vy
          + x
          - (1 - mu) * (x + mu) / r1**3
          - mu * (x - (1 - mu)) / r2**3)

    ay = (-2 * vx
          + y
          - (1 - mu) * y / r1**3
          - mu * y / r2**3)

    return [vx, vy, ax, ay]

# -----------------------------
# Conditions initiales
# -----------------------------
x0, y0 = 1.01, 0.0
vx0, vy0 = 0.0, 0.0
state0 = [x0, y0, vx0, vy0]

# -----------------------------
# Intégration temporelle
# -----------------------------
t = np.linspace(0, 10, 500)
traj = odeint(pr3c, state0, t)

# -----------------------------
# Tracé
# -----------------------------
plt.figure(figsize=(6, 6))
plt.plot(traj[:, 0], traj[:, 1], 'b', label="Trajectoire")
plt.plot(x1, y1, 'yo', label="Corps 1")
plt.plot(x2, y2, 'yo', label="Corps 2")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.legend()
plt.title("Problème restreint à trois corps (repère tournant)")
plt.grid()
plt.show()
