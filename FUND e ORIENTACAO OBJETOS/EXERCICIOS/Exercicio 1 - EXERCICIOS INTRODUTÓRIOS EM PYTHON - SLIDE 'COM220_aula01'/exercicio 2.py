#Exercicio 2 - Slide
# Leia dois números correspondentes a um intervalo, gere e imprima um número randômico dentro desse intervalo.

import random
num1 = input("Digite um numero: ")
num2 = input("Digite um numero: ")

print(random.randrange(int(num1),int(num2)))
