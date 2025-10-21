
import random

NumeroAleatorio = random.randint(1, 100)
#print(NumeroAleatorio)
usuario = int(input('Tente adivinhar um numero aleatório de 1 a 100: '))

while True:

    if NumeroAleatorio > usuario:
        usuario = int(input('tente um número maior: '))

    elif NumeroAleatorio < usuario:
        usuario = int(input('tente um número menor: '))

    else:
        print('Legal! você acertou. ')
        break