#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:33:44 2020

@author: juferoga
"""
import pandas as pd

import numpy as np

dna1 = np.array(np.random.randint(0, 3, 5))
dnak = np.array(np.random.randint(0, 3, 5))
dna3 = np.array(np.random.randint(0, 3, 5))

print(dna1,"\n",dnak,"\n",dna3,"\n")

df = pd.DataFrame( data = {'posicionx':  [0, 0, 0],
                           'posiciony':  [0, 0, 0],
                           'valoresRepetidos': [0, 0, 0],
                           'acumulador': [0, 0, 0]})

def menu():

	print ("Selecciona una opción")
	print ("\t1 - Hamming Distance")
	print ("\t2 - segunda opción")
	print ("\t3 - tercera opción")
	print ("\t9 - salir")

while True:
	# Mostramos el menu
	menu()
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
    elif opcionMenu=="3":
        print(x)
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


for x in range(5):
    print(dna1[x],dnak[x],dna3[x],"\n")
    
    if dna1[x] == dnak[x] and dnak[x] == dna3[x]:
        print("all equal")
    elif dna1[x] == dnak[x] and dnak[x] != dna3[x]:
        print("equall on", dna1[x] ,"and", dnak[x])
    elif dna1[x] != dnak[x] and dnak[x] == dna3[x]:
        print("equall on", dna3[x],"and", dnak[x])
    else:
        print('No matches in', x, x)
        
print("-----------------------The end--------------------------------- \n")

for x in range(5):
    print(dna1[x],dnak[x],dna3[-(x+1)],"\n")
    if dna1[x] == dnak[x] and dnak[x] == dna3[-(x+1)]:
        print("all equal")
    elif dna1[x] == dnak[x] and dnak[x] != dna3[-(x+1)]:
        print("equall on", dna1[-(x+1)] ,"and", dnak[x])
    elif dna1[x] != dnak[x] and dnak[x] == dna3[-(x+1)]:
        print("equall on", dna3[-(x+1)],"and", dnak[x])
    else:
        print('No matches in', x, -(x+1))
        
# for x in range(5):
#     print(dna1[-(x+1)],dnak[x],dna3[-(x+1)],"\n")
#     if dna1[-(x+1)] == dnak[x] and dnak[x] == dna3[-(x+1)]:
#         print("all equal")
#     elif dna1[-(x+1)] == dnak[x] and dnak[x] != dna3[-(x+1)]:
#         print("equall on", dna1[-(x+1)] ,"and", dnak[x])
#     elif dna1[-(x+1)] != dnak[x] and dnak[x] == dna3[-(x+1)]:
#         print("equall on", dna3[-(x+1)],"and", dnak[x])
#     else:
#         print('No matches in', x, -(x+1))