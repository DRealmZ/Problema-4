##### BOT OFENSIVO #####

import numpy
import random

def amenazas( amenazas ):
    amenaza_total =
    amenazas1=amenazas.split(":")
    amenaza_global = amenazas1[1]
    amenaza_local = amenazas1[0]
    ga = amenaza_local.split("-")
    cac = amenaza_global.split("-")
    return ga and cac

def maxima_amenaza ( ga ):
    max_am = []
    for i in ga:
        if max_am <= str(ga[i]):
            max_am = str(ga[i])
    return max_am

#max_am = leer los grados y hacer un max asi si C <= Cn
#         C = Cn

def densidad_cuadrante ( amenazas ):
    max_c= []
    for i in cac:
        if max_c <= cac[i]:
            max_c = cac[i]
    return max_c

#mas_c = leer los enemigos por cuadrante y hacer un max para tener el cuadrante
#        con mas enemigos

def mov( accion ):
    if ( accion == 1):
        return m = [-1,1]
    if ( accion == 2):
        return m = [-2,2]
    if ( accion == 3):
        return m = [-3,3]

def dis( accion ):
    if ( accion == 1):
        return m = [(-1),(1)]
    if ( accion == 2):
        return m = [(-3,-2),(2,3)]
    if ( accion == 3):
        return m = [(-5,-4),(4,5)]

def escoger_movimiento( amenazas ):
    if max_am == 3:
        move = mov(1)
        if max_c == c1:
            move = 
            return "0," + str(move)
    elif max_am == 2:
        move = mov(random.choice([1,2]))
        if max_c == c2:
            return str(move) +",0"
        return str(move) +",0"
    elif max_am == 1:
        move = mov(3)
        if ( random.randint(0,1) ):
            cord = "0," + str(move)
            return cord
        cord = str(move) +",0"
        return cord
    movimiento_x = str()
    movimiento_y = "" 
    return movimiento_x + "," + movimiento_y

def escoger_disparo( amenazas ):
    if max_am == 3:
        disp = dis(1)
        if max_c == c1:
            disp = random.choice(dis[1])
            return "0," + str(disp)
        elif max_c == c2:
            disp = random.choice(dis[0])
            return str(disp) +",0"
        elif max_c == c3:
            disp = random.choice(dis[0])
            return "0," + str(disp)
        elif max_c == c4:
            disp = random.choice(dis[1])
            return str(disp) +",0"
        
    elif max_am == 2:
        disp = dis(random.choice([2,3]))
        if max_c == c1:
            disp = random.choice(dis[1])
            return "0," + str(disp)
        elif max_c == c2:
            disp = random.choice(dis[0])
            return str(disp) +",0"
        elif max_c == c3:
            disp = random.choice(dis[0])
            return "0," + str(disp)
        elif max_c == c4:
            disp = random.choice(dis[1])
            return str(disp) +",0"
        #dispara al cuadrante con mas wns
    elif max_am == 1:
        disp = dis(3)
        if max_c == c1:
            disp = random.choice(dis[1])
            return "0," + str(disp)
        elif max_c == c2:
            disp = random.choice(dis[0])
            return str(disp) +",0"
        elif max_c == c3:
            disp = random.choice(dis[0])
            return "0," + str(disp)
        elif max_c == c4:
            disp = random.choice(dis[1])
            return str(disp) +",0"
        #dispara al cuadrante con mas weones
    disparo_x = ""
    disparo_y = ""
    return disparo_x + "," + disparo_y
