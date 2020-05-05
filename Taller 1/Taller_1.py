# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # 👻  **Taller 1 - Operadores de Control y estructuras**
# 
# <img src="https://www.udistrital.edu.co/themes/custom/versh/images/default/preloader.png" align="left" width="192px" height="192px"/>
# <img align="left" width="0" height="192px" hspace="10"/>
# 
# > Juan Felipe Rodríguez Galindo  - **COD. 20181020158**
# <br></br>
# [![Juan Felipe Rodriguez Galindo](https://img.shields.io/badge/Juferoga-github-br?style=flat-square)](https://gitlab.com/Juferoga)
# [![License](https://img.shields.io/badge/License-GPL_V.3-blue?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0.html)
# 
# 
# Introducción a la Ciencia de Datos
# 
# Desarrrollo del taller propuesto en la clase de introducción a la ciencia de datos.
# %% [markdown]
# ## Taller
# 
# ```
# Utilizando la sentencia ELSE en bucles, desarrollar un juego que genere un número 
# entero aleatorio de 0 al 99 y le pida al usuario que lo adivine. 
# El número de intentos debe ser de 10. 
# Al finalizar (adivine o no) se debe indicar si el usuario ganó o perdió 
# y se le debe dar un puntaje.
# 
# Dar pistas.
# ```
# %% [markdown]
# ## **Desarrollo**
# %% [markdown]
#  ## Libreria Random
#  Librería de python que permite generar números pseudo-random.

# %%
# Importamos el modulo Random
import random

# definición de variables

# Creamos un número aleatorio del 0 al 99 y lo guardamos en num_rand
num_rand = random.randint(0,99)
print(num_rand)

# Creamos algo asi como un booleano para controlar si adivino o no el número
entrada = "lol"
x=0
puntaje=100

# %% [markdown]
# Utilizamos una sentencia ciclica para controlar el numero de intentos del usuario, y saber si gano o perdio. También se utilizara para dar un puntaje al usuario.

# %%
while x < 10 and entrada != num_rand:
  x=x+1
  entrada = int(input(" Adivina adivinador, cual es el número que random escogio \n"))

# %% [markdown]
# Con esta sentencia controlamos si el usuario llega al limite de bucles para imprimir el mensaje de puntuación y verificar si pierde.

# %%
# IF para controlar si el usuario gano o perdio
  if(x==10):
    print('Perdiste! \n Puntaje :',puntaje)
    break

# %% [markdown]
# Con esta sentencia generamos las pistas que le damos al usuario para que adivine el número.

# %%
# IF para controlar las pistas que da el programa
  if(entrada < num_rand):
    puntaje = 100-(x*10)
    print("el numero es mayor")
    continue
  elif(entrada > num_rand):
    puntaje = 100-(x*10)
    print("el numero es menor")
    continue

# %% [markdown]
# Con el ELSE del iterador damos el resultado (victoria) y su correspondiente puntaje al terminar.

# %%
# ELSE del while en el que controlamos si el usuario gana y le damos su puntaje.
else:
  print('Ganaste! \n Puntaje :',puntaje)

# %% [markdown]
# Imprimos el fin del juego.

# %%
print('Game over')

