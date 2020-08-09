

"""7) Leia valores numéricos e os coloque numa lista. A leitura
termina quando o valor 0 for digitado. Em seguida,
calcule a média dos valores digitados e informe o
usuário. """

contador = True

lista_numerica =[]

while contador != False:
    numeros = float(input("Digite o valor numérico: "))
    if numeros != 0:
        lista_numerica.append(numeros)
        continue

    else:
        contador = False
        break

print("\nVoce digitou: " + str(lista_numerica))

soma = 0

for i in lista_numerica:
    soma = soma + i

print("\nMédia dos valores digitados: " + str(float(soma/len(lista_numerica))))