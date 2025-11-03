# importation des modules 
from scipy.integrate import odeint

# initialisation des variables globales



# equation du mouvement 
def eq(x,y,vx,vy):
  nx = x + vx*dt
  ny = y + vy*dt
  nvx = vx + (G * m_3 * ((1/d**3 - 1/r_2 ** 3) * m_2 * r_2 - (1/d**3 - 1/r_1 ** 3) * m_1 * r_1 ) + 2*m_3 * omega * vy) * dt
  nvy = vy + (2 * m_3 * omega * vx) * dt
  
  return nx, ny, nvx, nvy



# representation graphique
def trajectoire(tmax) :



  traj = odeint(eq, init, temps)
  liste_x = traj[1][0]
  liste_y = traj[1][2]
