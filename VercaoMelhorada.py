import random

print("🎯 Jogo de Adivinhação 🎯")
print("Tente adivinhar um número de 1 a 100!")

numero_aleatorio = random.randint(1, 100)
tentativas = 0
limite = 5

while tentativas < limite:
    try:
        usuario = int(input("Digite seu palpite: "))
        tentativas += 1

        if numero_aleatorio > usuario:
            print("🔼 Tente um número maior.")
        elif numero_aleatorio < usuario:
            print("🔽 Tente um número menor.")
        else:
            print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
            break

    except ValueError:
        print("⚠️ Digite apenas números!")

else:
    print(f"😢 Suas tentativas acabaram. O número era {numero_aleatorio}.")
