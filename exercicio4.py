# esse codigo usa bibliotecas time e random para criar um sistema 
# para o usuario adivinhar o numero que o computador pensou 
from random import randint
from time import sleep

computador = randint(0, 5)
print(" Vou pensar em um numero de 0 a 5, tente adivinhar.")
jogador = int(input("digite um numero de 0 a 5: "))
print("ESTOU PROCESSANDO...")
sleep(2)
if jogador == computador:
    print("parabéns, voce acertou.")
else:
    print(f"voce errou, eu pensei no numero {computador}.")

