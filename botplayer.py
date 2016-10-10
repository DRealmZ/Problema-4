##### BOT OFENSIVO #####

import numpy
import random

def amenazas(amenazas):
    amenaza = amenazas.split(":")
    amenaza = amenaza[0].split("-"),amenaza[1].split("-")
    return amenaza

#Se ordena el string de amenaza en los grados y la cantidad de
#enemigos por cuadrante

def maxima_amenaza( amenaza ):
    max_am = 0
    for i in amenaza[0]:
        if i != "a" :
            if max_am < i:
                max_am = i
            else:
                max_am = 0
    return max_am

def Attack_zone(amenaza):
    max_enem=0
    max_cuad=""
    for i in amenaza[1]:
        if i > max_enem:
            max_enem = i
            max_cuad="C" + str(i + 1)
    return max_cuad

def escoger_movimiento(max_am):
    x = 0
    y = 0
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
    elif max_am == 0:
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

def escoger_disparo(max_am):
    dx = 0
    dy = 0
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
    elif max_am == 0:
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
        
    disparo_x = str(dx)
    disparo_y = str(dy)
    return disparo_x + "," + disparo_y
