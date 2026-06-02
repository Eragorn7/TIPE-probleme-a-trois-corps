# importation des modules 
from scipy.integrate import odeint
from math import *
import matplotlib.pyplot as plt
import numpy as np

# initialisation des variables globales
x0, y0 = 0.5, 0
vx0, vy0 = 0,0
init = [x0, y0, vx0, vy0]
mu = 0.2

r_1 = mu
r_2 = 1-mu
omega = sqrt(1/(1-mu))


tmax = 10
N = 50
dt = tmax/N
temps = np.linspace(0, tmax, N)

def eq(coord, t):
    x, y, vx, vy = coord[0], coord[1], coord[2], coord[3]
    
    r = np.sqrt(x**2 + y**2)
    
    # Accélérations (gravité + forces de Coriolis et centripète)
    ax = -mu * x / r**3 + 2 * omega * vy
    ay = -mu * y / r**3 - 2 * omega * vx
    
    # Calcul de la position et de la vitesse
    nx = x + vx * dt
    ny = y + vy * dt
    nvx = vx + ax * dt
    nvy = vy + ay * dt
    
    return [nvx, nvy, ax, ay]

# Correcting the plotting part
def trajectoire():
    traj = odeint(eq, [x0, y0, vx0, vy0], temps)
    liste_x = []
    liste_y = []
    for k in range(len(traj)):
        liste_x.append(traj[k][0])
        liste_y.append(traj[k][1])  # Corrected from traj[k][2] to traj[k][1]

    plt.plot(-r_1, 0, color="yellow", marker="o")
    plt.plot(r_2, 0, color="yellow", marker="o")
    plt.plot(liste_x, liste_y, "b+")
    plt.show()

trajectoire()
