import time
import random
from diccionario import diccionario

nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre, "Es hora de jugar al ahorcado Pokemon!")
print(" ")
time.sleep(1)
print("Adivina el nombre del Pokemon")
time.sleep(0.5)
palabra = random.choice(diccionario).lower()
tupalabra = ''
vidas = 5

while vidas > 0:
    fallas = 0
    for letra in palabra:
        if letra in tupalabra:
            print(letra, end="")

        else:
            print("*", end="")
            fallas += 1

    if fallas == 0:
        print("")
        print("Felicidades, ganaste")
        break

    tuletra = input("Introduce una letra: ")
    tupalabra += tuletra

    if tuletra not in palabra:
        vidas -= 1
        print("Te equivocaste! Prueba con otra letra")
        print("Te quedan ", +vidas, " vidas")

    if vidas == 0:
        print("Perdiste!")
else:
    print("Está vez no pudo ser pero hay que seguir intentando!")
