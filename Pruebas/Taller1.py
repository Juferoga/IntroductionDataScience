import random

num_rand = random.randint(0,99)
print(num_rand)

entrada = "lol"
x=0

while x < 10 and entrada != num_rand:
  x=x+1
  entrada = int(input(" Adivina adivinador, cual es el número que random escogio \n"))
  puntaje = 100-(x*10)
  if(entrada < num_rand):
    print("el numero es mayor")
  elif(entrada > num_rand):
    print("el numero es menor")
  if(x==10):
    print('Perdiste! \n Puntaje :',puntaje)
    break
else:
  print('Ganaste! \n Puntaje :',puntaje)

print('Game over')