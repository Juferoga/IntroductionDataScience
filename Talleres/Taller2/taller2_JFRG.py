# -*- coding: utf-8 -*-
"""
Juferoga de Spyder
"""

import numpy as np

# creamos un array con los identificadores para poder manipularlos de una forma más simple
id = np.array([[0, 0, 0],[0, 0, 1],[0, 0, 2],[0, 1, 0],[0, 2, 2],[0, 2, 3],
               [0, 2, 0],[0, 2, 1],[0, 2, 2],[1, 0, 0],[1, 0, 1],[1, 0, 2],
               [1, 1, 0],[1, 1, 1],[1, 1, 2],[1, 2, 0],[1, 2, 1],[1, 2, 2],
               [2, 0, 0],[2, 0, 1],[2, 0, 2],[2, 1, 0],[2, 1, 1],[2, 1, 2],
               [2, 2, 0],[2, 2, 1],[2, 2, 2] ])

# Mostramos los identificadores para que el usuario pueda elejir el que desaea cambiar
print("identificadores de las matrices o de los cubos de Rubik \n",id)

########## Funciones utiles ##########

# lim : lo uilizamos para delimitar tanto el eje x,y,z del cubo
def lim(fil, col, z):
    # x
    row = np.arange(fil*3, fil*3+3, 1)
    # y
    col = np.arange(col*3, col*3+3, 1)
    # la Z
    la_z = np.arange(z*3, z*3+3, 1)
    return row, col, la_z

# cb : creamos un nuevo arreglo, le damos un amejor manejo por medio de la funcion
# meshgrid (https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html)
def cb(m1, m2, m3):
    return np.array(np.meshgrid(m1, m2, m3)).T.reshape(-1, 3)


# replace : lo utilizamos para reemplazar los datos de posicion a posicion 
def replace(nums, id_replazo, z):
    for i, val in enumerate(nums):
        z[id_replazo[i][0], id_replazo[i]
            [1], id_replazo[i][2]] = val

# cp: Creamos una copia que mantiene los datos que se reemplazaran primero
def cp(id, z):
    copia = []
    for i in id:
        copia.append(z.item(*i))
    return copia

# creamos el arreglo de 729 elementos y lo convertimos o realizamos un reshape
# para que cumpla con la condicion de se 9x9x9 (Solucion Punto 1)
elarreglo = np.arange(729).reshape(9, 9, 9)

# ingreso de datos de los respectivos identificadores que permitiran cambiar las
# posiciones de estos
num1 = int(input('Ingresa identificador 1: '))
num2 = int(input('Ingresa identificador 2: '))

# utilizamos los datos ingresados para ubicar un limite en las tres posiciones x,y,z con los identificadores
row, col, la_z = lim(*id[num1])
# convertimpos los ids para tratar de forma mas simple los datos
cmb1 = cb(row, col, la_z)
#print(cmb1)
cp1 = cp(cmb1, elarreglo)

# utilizamos los datos ingresados para ubicar un limite en las tres posiciones x,y,z con los identificadores
row, col, la_z = lim(*id[num2])
cmb2 = cb(row, col, la_z)
#print(cmb2)
copia2 = cp(cmb2, elarreglo)
# reeemplzamos 
replace(cp1, cmb2, elarreglo)
replace(copia2, cmb1, elarreglo)
# imprimimmos el resultado final
print(elarreglo)



#### Pruebas si lo envie fue por error####

# id1=[0,0,0]
# id2=[1,1,1]

# otras formas de llegar a la coordenada x,y,z
# def find_x(bb1):
#     return (bb1%3)*3
# def find_y(bb1):
#     return (bb1%9)//3*3
# def find_z(bb1):
#     return (bb1//9)*3

# def cambiar_posicion(b1,b2,z):
#     return 1

# Punto 1 => crear unarreglo 9x9x9 de 0 a 728

# Creamos el arreglo inicial
# aInicial = np.arange(0,729,1).reshape(9,9,9)

#  Creamos el arrego a con base al inicial, luego la redimiensionamos
#  con la forma 9x9x9
# a = aInicial.reshape(9,9,9)
# print (aInicial[0,0:3,0:3])
# print (aInicial)

# Pedimos los datos de cambio al usuario
# id1=int(input("digite identificador del bloque 1 \n =>"))
# print ("El identificador uno es:",id1)
# print ("\n",find_x(id1))
# print ("\n",find_y(id1))
# print ("\n",find_z(id1))

# id2=int(input("digite identificador del bloque 2 \n =>"))
# print ("El identificador dos es:",id2) 

# cambiar_posicion(id1,id2)     
