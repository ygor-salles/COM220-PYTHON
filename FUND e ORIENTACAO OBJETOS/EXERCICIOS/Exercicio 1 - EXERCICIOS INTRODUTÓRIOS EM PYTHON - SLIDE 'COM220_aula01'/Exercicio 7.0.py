

"""7) Leia valores numéricos e os coloque numa lista. A leitura
termina quando o valor 0 for digitado. Em seguida,
calcule a média dos valores digitados e informe o
usuário. """

lista = []
soma = 0

while True:
    num = int(input('Digite num: '))
    if num != 0:
        lista.append(num)
        soma += num
        continue
    else:
        break

print('\nA lista de valores: ' + str(lista))
print('A media do resultado é: ' + str(float(soma/len(lista))))

        