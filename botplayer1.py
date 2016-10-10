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
    for i in ga:
        if i != "a" :
            if max_am <= int(ga[i]):
            max_am = int(ga[i])
    return max_am

def densidad_cuadrante ( cac ):
    cant_enem={}
    c=1
    for i in cac:
        cant_enem["C"+"c"]=i
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

def escoger_movimiento(max_am , max_cuad):
    if max_am == 3:
        move = [-3,3]
        if max_cuad == "C1":
            y= move[1]
            return y
        elif max_cuad == "C2":
            x = move[0]
            return x
        elif max_cuad == "C3":
            y = move[0]
            return y
        elif max_cuad == "C4":
            x = move[1]
            return x
    elif max_am == 2:
        move = [-1,1]
        if max_cuad == "C1":
            y= move[1]
            return y
        elif max_cuad == "C2":
            x = move[0]
            return x
        elif max_cuad == "C3":
            y = move[0]
            return y
        elif max_cuad == "C4":
            x = move[1]
            return x
    elif max_am == 1:
        move = [-3,3]
        if max_cuad == "C1":
            y= move[1]
            return y
        elif max_cuad == "C2":
            x = move[0]
            return x
        elif max_cuad == "C3":
            y = move[0]
            return y
        elif max_cuad == "C4":
            x = move[1]
            return x
    
    movimiento_x = str(x)
    movimiento_y = str(y)
    return movimiento_x + "," + movimiento_y

def escoger_disparo(max_am , max_cuad):
    if max_am == 3:
        disp = [-1,1]
        if max_cuad == "C1":
            dy= disp[1]
            return dy
        elif max_cuad == "C2":
            dx = disp[0]
            return dx
        elif max_cuad == "C3":
            dy = move[0]
            return dy
        elif max_cuad == "C4":
            dx = move[1]
            return dx
        #dispara a la pos. adyacente con mas enemigos por cuadrante
    elif max_am == 2:
        disp = [(-3,-2),(2,3)]
        if max_cuad == "C1":
            dy= random.choice(disp[1])
            return dy
        elif max_cuad == "C2":
            dx = random.choice(disp[0])
            return dx
        elif max_cuad == "C3":
            dy = random.choice(disp[0])
            return dy
        elif max_cuad == "C4":
            dx = random.choice(disp[1])
            return dx
        #dispara al cuadrante con mas enemigos
    elif max_am == 1:
        move = [-5,-4,4,5]
        if max_cuad == "C1":
            dy= random.choice(disp[1])
            return dy
        elif max_cuad == "C2":
            dx = random.choice(disp[0])
            return dx
        elif max_cuad == "C3":
            dy = random.choice(disp[0])
            return dy
        elif max_cuad == "C4":
            dx = random.choice(disp[1])
            return dx
        #dispara al cuadrante con mas enemigos
    disparo_x = str(dx)
    disparo_y = str(dy)
    return disparo_x + "," + disparo_y
