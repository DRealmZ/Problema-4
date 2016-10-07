##### BOT OFENSIVO #####

import numpy
import random

def amenazas(amenazas):
    am_g = []
    amenazas1 = amenazas.split(":")
    amenaza_global = amenazas1[1]
    amenaza_local = amenazas1[0]
    ga = amenaza_local.split("-")
    cac = amenaza_global.split("-")
    am_g.append(ga)
    am_g.append(cac)
    return am_g

def maxima_amenaza (am_g):
    max_am = 0
    am = am_g[0]
    for i in am:
        if i != "a":
            if max_am <= int(am[i])
            max_am = int(am[i])
    return max_am

def mov():


def dis( accion ):
    if ( accion == 1):
        m = [(-1),(1)]
        return m
    if ( accion == 2):
        m = [(-3,-2),(2,3)]
        return m
    if ( accion == 3):
        m = [(-5,-4),(4,5)]
        return m

def escoger_movimiento( amenazas ):
    if max_am == 3:
        if max_c == "c1":
            move = 1
            return "0," + str(move)
        elif max_c == "c2":
            move = 1
            return  str(move)
        elif max_c == "c3":
            move = 1
            return "0," + str(move)
        elif max_c == "c4":
            move = 1
            return "0," + str(move)
    elif max_am == 2:
        if max_c == "c1":
            move = 
            return "0," + str(move)
        elif max_c == "c2":
            move = 1
            return str(move) + ",0"
        elif max_c == "c3":
            move = 1
            return "0," + str(move)
        elif max_c == "c4":
            move = 1
            return str(move) +",0"
        return str(move) +",0"
    elif max_am == 1:
        move = mov(3)
        if ( random.randint(0,1) ):
            cord = "0," + str(move)
            return cord
        cord = str(move) +",0"
        return cord
    movimiento_x = str(move)
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
