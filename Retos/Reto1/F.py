#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:33:44 2020

@author: juferoga
"""
import pandas as pd
import time
import numpy as np

query = np.array(np.random.randint(0, 3, 50))
query2 = np.array(np.random.randint(0, 3, 50))
sequence = np.array(np.random.randint(0, 3, 50))

dna1 = np.array(np.random.randint(0, 3, 50))
dnak = np.array(np.random.randint(0, 3, 50))
dna3 = np.array(np.random.randint(0, 3, 50))

print(dna1,"\n",dnak,"\n",dna3,"\n")

df = pd.DataFrame( data = {'posicionx':  [0, 0, 0],
                           'posiciony':  [0, 0, 0],
                           'valoresRepetidos': [0, 0, 0],
                           'acumulador': [0, 0, 0]})

# Distancia Hamming

def HammingDistance(p, q):
    score = 0
    if len(p) == len(q):
        for i in range (len(p)):
            if (p[i]) != q [i]:
                score = score+1
    return (score)


# PPatron para encontrar la similitud entre cadenas

def approx_pattern_match(query, sequence, max_mismatch):
    index= []
    for i in range(len(sequence)-len(query)+1):
        pattern = sequence [i:i+len(query)]
        if HammingDistance(query,pattern) <= max_mismatch:
            index.append(i)
            #print type(index)
    return ' '.join(map(str, index))


def menu():

   	print ("Selecciona una opción")
   	print ("\t1 - Hamming Distance (comprobar la similitud)")
   	print ("\t2 - Normal version 1 (beta -_-)")
   	print ("\t3 - Normal version 2")
   	print ("\t9 - salir")

while True:
    menu()
    opcionMenu = input("inserta un numero valor >> ")
    if opcionMenu=="1":
        t0=time.time()
        print("Con la cadena 1 y 2 :",approx_pattern_match(query, sequence, 50))
        print("Con la cadena 2 y 3 :",approx_pattern_match(query2, sequence, 50))

        #Fin
        t1 = time.time()
        total = t1-t0
        print ("Tiempo :",total)
        print ("")
        input("Has pulsado la opción 1...\npulsa una tecla para continuar")
    elif opcionMenu=="2":
        t0 = time.time()

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
        #Fin
        t1 = time.time()
        total = t1-t0
        print ("Tiempo :",total)
        print(" ")
        input("Has pulsado la opción 2...\npulsa una tecla para continuar")

    elif opcionMenu=="3":

        t0 = time.time()
        dna1 = ''
        dna2 = ''
        adn = ''
        
        #señalamos los Indices para el trrtamiento de datos
        index = np.array(['A', 'C', 'G', 'T',])
        
        #Creamos las 3 dna_chains de ADN
        adn1 = np.array(np.random.randint(0, 3, 50))
        adn2 = np.array(np.random.randint(0, 3, 50))
        dna = np.array(np.random.randint(0, 3, 50))
        
        #se colocan los Indices para cortar la dna_chain
        
        for i in adn1:
            dna1 = dna1 + index[i]
            
        for i in adn2:
            dna2 = dna2 + index[i]
        
        for i in dna:
            adn = adn + index[i]
        
        # La funcion para Comprobar la similitud
        def probe_simil(dna_chain):
            counter = 0
            vector = ''
            for i in range(0, len(dna_chain)):
                    if dna_chain[i]==dna[i]:
                        counter = counter+1
                        vector = vector+dna_chain[i]
            return counter, vector
            
        rep = []
        rep2 = []
        
        for i in range(0,50):
            counter, vector = probe_simil(dna1[i:20+i])
            rep.append(vector)
            rep2.append(counter)
        
        vmax=max(rep2)
        
        #print("Max: ",max(rep), vmax)
        print("chain: ",dna1[rep2.index(vmax):rep2.index(vmax)+50])
        print("chain dna: ",dna)
        
        rep = []
        rep2 = []
        
        for i in range(0, 50):
            counter, vector = probe_simil(dna2[i:20+i])
            rep.append(vector)
            rep2.append(counter)
        
        vmax = max(rep2)
        
        print("chain: ",dna2[rep2.index(vmax):rep2.index(vmax)+50])
        #print("max: ",max(rep), vmax)
        #Fin
        t1 = time.time()
        total = t1-t0
        print ("Tiempo :",total)
        print ("")
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif opcionMenu=="9":
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")