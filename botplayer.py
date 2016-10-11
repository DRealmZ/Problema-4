##### BOT OFENSIVO #####

import numpy
import random

def amenazas(amenazas):
    amenazas1 = amenazas.split(":")
    amenaza_global = amenazas1[1]
    amenaza_local = amenazas1[0]
    ga = amenaza_local.split("-")
    cac = amenaza_global.split("-")
    return ga,cac

#Se ordena el string de amenaza en los grados (variable ga) y la cantidad de
#enemigos por cuadrante

def maxima_amenaza( ga ):
    max_am = 0
    if len(ga) > 1:
        for i in ga:
            if i != "a" :
                if max_am <= i:
                    max_am = i
    else:
        max_am = '0'
    return max_am
#Determina el valor que indica la mayor amenaza

def densidad_cuadrante ( cac ):
    cant_enem={}
    c=1
    for i in cac:
        cant_enem["C"+str(c)]=i
        c+=1
    return cant_enem

#Se crea un diccionario que tiene como llave a cada uno de los cuadrantes y
#como valor tiene a la cantidad de enemigos en dicho cuadrante. 

def Attack_zone( cant_enem ):
    max_enem=0
    max_cuad=""
    for cuad,c_enem in cant_enem.items():
        if c_enem > max_enem:
            max_enem=c_enem
            max_cuad=str(cuad)
    return max_cuad
#Se determina el cuadrante que contiene el mayor numero de enemigos

def escoger_movimiento(max_am):
    x = 0
    y = 0
    if max_am == '3':
        move = [-3,3]
        if max_cuad == "C1":
            y = move[1]
            x = 0
        elif max_cuad == "C2":
            x = move[0]
            y = 0
        elif max_cuad == "C3":
            y = move[0]
            x = 0
        elif max_cuad == "C4":
            x = move[1]
            y = 0
    elif max_am == '2':
        move = [-1,1]
        if max_cuad == "C1":
            y = move[1]
            x = 0
        elif max_cuad == "C2":
            x = move[0]
            y = 0
        elif max_cuad == "C3":
            y = move[0]
            x = 0
        elif max_cuad == "C4":
            x = move[1]
            y = 0
    elif max_am == '1' or max_am == '0':
        move = [-3,3]
        if max_cuad == "C1":
            y = move[1]
            x = 0
        elif max_cuad == "C2":
            x = move[0]
            y = 0
        elif max_cuad == "C3":
            y = move[0]
            x = 0
        elif max_cuad == "C4":
            x = move[1]
            y = 0
    movimiento_x = str(x)
    movimiento_y = "0"
    return movimiento_x + "," + movimiento_y

def escoger_disparo(max_am):
    dx = 0
    dy = 0
    if max_am == '3':
        disp = [-1,1]
        if max_cuad == "C1":
            dy = disp[1]
            dx = 0
        elif max_cuad == "C2":
            dx = disp[0]
            dy = 0
        elif max_cuad == "C3":
            dy = disp[0]
            dx = 0
        elif max_cuad == "C4":
            dx = disp[1]
            dy = 0
        #dispara a la pos. adyacente con mas enemigos por cuadrante
    elif max_am == '2':
        disp = [(-3,-2),(2,3)]
        if max_cuad == "C1":
            dy = random.choice(disp[1])
            dx = 0
        elif max_cuad == "C2":
            dx = random.choice(disp[0])
            dy = 0
        elif max_cuad == "C3":
            dy = random.choice(disp[0])
            dx = 0
        elif max_cuad == "C4":
            dx = random.choice(disp[1])
            dy = 0
        #dispara al cuadrante con mas enemigos
    elif max_am == '1' or max_am == '0':
        disp = [(-5,-4),(4,5)]
        if max_cuad == "C1":
            dy = random.choice(disp[1])
            dx = 0
        elif max_cuad == "C2":
            dx = random.choice(disp[0])
            dy = 0
        elif max_cuad == "C3":
            dy = random.choice(disp[0])
            dx = 0
        elif max_cuad == "C4":
            dx = random.choice(disp[1])
            dy = 0
        #dispara al cuadrante con mas enemigos
        
    disparo_x = "0"
    disparo_y = str(dy)
    return disparo_x + "," + disparo_y
