#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 18:57:38 2020

@author: juferoga
"""

import numpy as np

# definimos
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

for i in adn:
    dna = dna + index[i]

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
    counter, vector = probe_simil(dna1[i:50+i])
    rep.append(vector)
    rep2.append(counter)

vmax=max(rep2)

print(max(rep), vmax)
print(dna1[rep2.index(vmax):rep2.index(vmax)+50])
print(dna)

rep = []
rep2 = []

for i in range(0, 50):
    counter, vector = probe_simil(dna2[i:50+i])
    rep.append(vector)
    rep2.append(counter)

vmax = max(rep2)

print(dna1[rep2.index(vmax):rep2.index(vmax)+50])
print(max(rep), vmax)