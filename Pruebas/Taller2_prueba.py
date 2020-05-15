
import numpy as np
import pandas as pd

casovid = pd.read_csv('./Casos_positivos_de_COVID-19_en_Colombia.csv')
#print(casovid.columns)

# Limpieza de datos

print(" is null \n")
print(casovid.isnull())

# print(drop na 1\n")
# print(casovid.)

# print(drop na 2\n")
# print(casovid.)

# print(drop na 3\n")
# print(casovid.)

# print(fill na 1\n")
# print(casovid.)

# print(fill na 2\n")
# print(casovid.)

# print(fill na 3\n")
# print(casovid.)
print("\n________________________ \n")
print("  filtrado y consulta \n")
print("________________________ \n")

print("\n Select columna >= valor \n")
print(casovid['ID de caso']>=12)

print("\n Select casovid[casovid['ID de caso']>=12] \n")
print(casovid[casovid['ID de caso']>=12])

print("\n Select casovid['ID de caso'][casovid['Edad']>=12] \n")
print(casovid['ID de caso'][casovid['Edad']>=12])

print("\n Select casovid[(casovid['ID de caso']>=12)&(casovid['Edad']>=13)] \n")
print(casovid[(casovid['ID de caso']>=12)&(casovid['Edad']>=13)])

# # Select where
# print()

# # Select MASK
# print()

# # Select IsIn
# print()

# # Select Query
# print()

# # Select Eval
# print()