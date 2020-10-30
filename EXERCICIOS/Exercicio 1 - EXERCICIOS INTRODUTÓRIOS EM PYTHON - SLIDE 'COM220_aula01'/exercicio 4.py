#Exercicio 4 - Slide
#Utilizando a tabela a seguir, escreva um código que permita obter a alíquota do imposto de renda de acordo com o valor da renda mensal. 
#Seu programa deve ler o valor da renda e imprimir o valor da alíquota, bem como o valor do imposto a pagar.

salario = float(input ('Digite o valor do seu salário: '))

if salario < 1903.99:
    aliq = 0
elif salario >= 1903.99 and salario < 2826.65 :
    aliquota = 7.5
elif salario >= 2826.66 and salario < 3751.05:
    aliquota = 15
elif salario >= 3751.06 and salario < 4664.68:
    aliquota = 22.5
else:
    aliquota = 27.5

valor_imposto = (salario * aliquota)/100

print('Valor da aliquota: ' + str(aliquota))
print('Valor do imposto: ' + str(valor_imposto))

