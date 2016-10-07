##### BOT OFENSIVO #####

import numpy
import random

def amenazas( amenazas ):
    amenazas1=amenazas.split(":")
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
            if max_am <= str(ga[i]):
            max_am = str(ga[i])
    return max_am

#max_am = leer los grados y hacer un max asi si C <= Cn
#         C = Cn

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
            max_cuad="cuad"
    return max_cuad

def mov(max_cuad):
    if max_cuad == "C1":
        BLA
    if max_cuad == "C2":
        sjfah
    if max_cuad == "C3":
        lasjdkajh
    if max_cuad == "C4":
        askljaij

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
        #dispara al cuadrante con mas enemigos
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
        #dispara al cuadrante con mas enemigos
    disparo_x = ""
    disparo_y = ""
    return disparo_x + "," + disparo_y
