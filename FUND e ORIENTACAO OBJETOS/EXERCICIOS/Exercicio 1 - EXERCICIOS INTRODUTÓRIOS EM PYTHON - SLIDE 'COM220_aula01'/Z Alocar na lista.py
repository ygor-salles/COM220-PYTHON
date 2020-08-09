#Colocar numeros a lista de forma dinâmica, e exibir o resultado 

numlist = list()
while True:
    leave = ' '
    num = int(input('Digite um numero para colocar na lista: '))
    numlist.append(num)

    while leave not in 'SsNn':
        leave = str(input('Você deseja continuar colocando numeros na lista? [S/N] '))
    if leave in 'Nn':
       break
numlist.sort()
print(f'Os números da sua lista são:\n{numlist}')