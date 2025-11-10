# importation des modules 
from scipy.integrate import odeint
from math import *
import matplotlib.pyplot as plt
import numpy as np

# initialisation des variables globales
x0, y0 = 0.5*1.5e8, 0
vx0, vy0 = 0,0
init = [x0, y0, vx0, vy0]
G = 6.7e-11
m_1 = 2e30
m_2 = 6e24
m_3 = 6.5e3
omega = sqrt(G * (m_1 + m_2) / d**3)
r_1 = -m_2/(m_2 + m_1)
r_2 = m_1/(m_1 + m_2)

tmax = 10
N = 50
dt = tmax/N
temps = np.linspace(0, tmax, N)


# equation du mouvement 
def eq(x,y,vx,vy):
  nx = x + vx*dt
  ny = y + vy*dt
  nvx = vx + (G * m_3 * ((1/d**3 - 1/r_2 ** 3) * m_2 * r_2 - (1/d**3 - 1/r_1 ** 3) * m_1 * r_1 ) + 2*m_3 * omega * vy) * dt
  nvy = vy + (2 * m_3 * omega * vx) * dt
  
  return nx, ny, nvx, nvy



#obtention de la trajectoire dans le referentiel tournant
def trajectoire() :
  """ version sans odeint
  liste_x = [x0]
  liste_y = [y0]
  liste_vx = [vx0]
  liste_vy = [vy0]
    
  n = len(temps)
  for i in range(n) :
      nx, ny, nvx, nvy = eq(liste_x[-1], liste_y[-1], liste_vx[-1], liste_vy[-1])
      liste_x.append(nx)
      liste_y.append(ny)
      liste_vx.append(nvx)
      liste_vy.append(nvy)

  """
  traj = odeint(eq, init, temps)
  liste_x = traj[1][0]
  liste_y = traj[1][2]
  plt.plot(-r_1,0,"yo")
  plt.plot(r_2,0,"yo")
  plt.plot(liste_x,liste_y,"b+")
  

# representation graphique
