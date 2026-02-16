# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 15:36:17 2025

@author: praymond
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import subprocess  
from math import *





def V(y,t):
  global nu
  x,px,y,py = y[0],y[1],y[2],y[3]   
  R1 = sqrt( (x+nu)**2 + y**2)
  R2 = sqrt( (x+nu-1)**2 + y**2)
  #print('R1=',R1, ' R2=',R2, ' x=',x , ' y=',y, ' nu=',nu)
  dxdt = px + y
  dpxdt = py - (1-nu)*(x+nu)/R1**3 - nu*(x+nu-1)/R2**3
  dydt = py-x
  dpydt = -px - (1-nu)*y/R1**3 - nu*y/R2**3
  return dxdt, dpxdt, dydt, dpydt



 
 
nu = 0.2 # parameters
R = 1.5 # zone de dessin x=-R->R, y=-R->R



def Animation_Flot_2D(x0,px0,y0,py0,tmax,N,opt):
   
   
    #plt.rc('text', usetex=True)
   # plt.rc('font', family='serif')
    t=0
    dt = tmax/N
    temps = np.linspace(0, tmax, N)
    
    global R
    
        
    plt.axis([-R,R, -R, R]) # selectionne la vue
    #plt.axis('equal') # pour avoir meme echelle en x,y
    plt.xlabel('x')
    plt.ylabel('y')




    if(opt == 'galileen'):
        text = 'Trajectoire du pb 3 corps dans ref. GalilÃ©en'
    else:
        text = 'Trajectoire du pb 3 corps dans ref. tournant'
    text += '\n nu='+ ('%4.3f'%nu)+ ', t='+ ('%4.2f'%t)
    plt.title(text)  

    #-- dessin des etoiles
    x2,y2= -nu,0
    if(opt == 'galileen'):
        x2,y2 =  x2*cos(t) - y2*sin(t), x2*sin(t) + y2*cos(t) # formule de rotation
    plt.plot([x2],[y2], color = 'yellow', marker = 'o', linestyle = 'none') 


    x2,y2= 1-nu,0
    if(opt == 'galileen'):
        x2,y2 =  x2*cos(t) - y2*sin(t), x2*sin(t) + y2*cos(t) # formule de rotation
    plt.plot([x2],[y2], color = 'yellow', marker = 'o', linestyle = 'none') 



    #--dessin du corps 3





    Ty = odeint(V, [x0,px0,y0,py0], temps)
    x = [Ty[1][0]]
    y = [Ty[1][2]]
    for k in range(len(Ty)) :
        x.append(Ty[k][0])
        y.append(Ty[k][2])
        """
    r = max(abs(x),abs(y))
    if(r>R/1.1):
        r=r*1.1
        plt.axis([-r,r, -r, r]) # selectionne la vue
        """
    print(x)
    print(y)
    plt.plot(x, y, "b+")

