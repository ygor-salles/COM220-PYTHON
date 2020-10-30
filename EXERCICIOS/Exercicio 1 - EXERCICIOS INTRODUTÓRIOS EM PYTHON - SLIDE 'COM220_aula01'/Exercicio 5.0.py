"""5) Leia um conjunto de nomes e os armazene numa lista. Em
seguida, leia um nome e verifique se o mesmo faz parte
dessa lista."""

qtd = int(input('Digite a quantidade de nomes: '))

lista_nomes = []
for i in range(qtd):
    nomes = input('Digite nome: ')
    lista_nomes.append(nomes)

print('Sua lista de nomes é: '+str(lista_nomes))
nome_buscar = input('Digite um nome: ')

if nome_buscar in lista_nomes:
    print('\nO nome ' +nome_buscar+ ' está na lista nomes\n')
else:
    print('\nO nome '+nome_buscar+' NÃO está na lista\n')

