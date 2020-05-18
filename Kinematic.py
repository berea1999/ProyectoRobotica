# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:16:55 2020

@author: elsir
"""

from mpl_toolkits import mplot3d
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, PathPatch
import mpl_toolkits.mplot3d.art3d as art3d

def getX( a, ang):
    return a * math.cos(math.radians(ang))

def getY(b, y):
    return math.sqrt((y)**2 - (b)**2)


if __name__ == '__main__':
    
    
    ex = False
    armAng = True
    grid = True
    mark = True
    
    while(ex == False):
        opcio = 5
        'Input de la distancia del brac i l angle en que es troba'
        if(armAng == True):
            arm = int(input("Arm length:"))
            ang = int(input("Angle of the actual position:"))
            armAng = False
        
        'Inicialitzem els eixos sobre els cuals es mourá el nostre brac simulat'
        'Horitzontal'
        z_base = np.array([0,0,0])
        y_base = np.array([0,0,0])
        x_base = np.array([-arm,0,arm])
        'Vertical'
        z_vrt = np.array([-arm,0,arm])
        y_vrt = np.array([0,0,0])
        x_vrt = np.array([0,0,0])
        
        '-------------------------Figure Options ------------------------'
        'Opcions per a la creació de la figura'
        fig = plt.figure(figsize=(10,10), dpi=100, edgecolor = 'red')
        'identifiquem que es una figura 3D'
        ax = plt.axes(projection="3d")
        
        if(grid == True):
            ax.grid(False)
        
        ax.set_facecolor('xkcd:black') 
        
        'Creació del cercle que indica per on pot pasar el brac al rotar'
        circle = plt.Circle((0,0), arm, color = 'r', fill = False)
        ax.add_patch(circle)
        ax.tick_params(colors = 'r')
        art3d.pathpatch_2d_to_3d(circle, z=0, zdir='y')
        
        'Limits dels eixos (del contrari es modifiquen segons el brac)'
        ax.set_xlim([-arm,arm])
        ax.set_ylim([-arm,arm])
        ax.set_zlim([-arm,arm])
        
        '----------------------------------------------------------------'
           
        '-------------------------Direct Kinematic-----------------------'
        x = getX(arm,ang)
        h = getY(x, arm)
        
        'utilitzem les cordenades calculades per crear la posició del brac'
        x_line = [0,x]
        y_line = [0,0]
        z_line = [0,h]
        
        x_pala = [x, x]
        y_pala = [0, -arm/3]
        z_pala = [h, h]
        'Marca desde la posició del brac fins al terra vert---------------'
    
        '-----------------------PLOT--------------------------------------3'
        x_mark = [x,x]
        y_mark = [0,0]
        z_mark = [0,h]
        '-----------------------------------------------------------------'
        ax.plot3D(x_base,y_base,z_base,'red')
        ax.plot3D(x_vrt,y_vrt,z_vrt,'red')
        if(mark == True):
            ax.plot3D(x_mark,y_mark,z_mark,'green')
        ax.plot3D(x_line,y_line,z_line,'blue')
        ax.plot3D(x_pala,y_pala,z_pala,'blue')
        
        plt.show()
        print('Coordenada X: ',x, '/ Coordenada Y :', h )
        print('---------------------------MENU----------------------------')
        print('Canviar mesures - 1')
        print('Activar/Desactivar grid - 2')
        print('Activar/Desactivar marca vertical - 3')
        print('Sortir - 0 \n')
        
        opcio = int(input("Que vols fer? "))
        '-----------------------------------------------------------------'
        if(opcio == 0):
            ex = True
        elif(opcio == 1):
            armAng = True
        elif(opcio == 2):
            if(grid == False):
                grid = True
            else:
                grid = False
        elif(opcio == 3):
            if(mark == False):
                mark = True
            else:
                mark = False
        
        
        
    
    
        
        

        
        
        