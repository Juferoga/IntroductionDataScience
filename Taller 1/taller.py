# Importamos el modulo Random
import random

# definición de variables

# Creamos un número aleatorio del 0 al 99 y lo guardamos en num_rand
i=0
num_rand = random.randint(0,99)
print(num_rand)

# Creamos algo asi como un booleano para controlar si adivino o no el número
Verificador = False

while i < 10 and Verificador !=True:
  entrada = int(input(" Adivina adivinador, cual es el número que random escogio \n"))
  puntaje = 100-(i*10)
  if (entrada >= num_rand):
    print("Pista : El número es menor..")
  elif (entrada <= num_rand):
    print("Pista : El número es mayor..")
  elif (entrada == num_rand) :
    Verificador = True
  else:
    print('Perdiste! \n Puntaje :',puntaje)

else:
  print('Ganaste! \n Puntaje :',puntaje)
