""" 9) Escreva uma função booleana que recebe uma string e verifica se a mesma é um palíndromo. 
Em seguida, escreva um código para ler uma string e, usando a função criada,
 verifique se a mesma é uma string. """

#Função verifica se é palíndromo
def verifica_palindromo(str):
    palindromo=True
    
    for i in range(int(len(str)/2)):
        if str[i] != str[len(str) - i - 1]:
            palindromo = False
            break

    return palindromo

#Função Principal
str = input('Digite uma palavra: ')
if verifica_palindromo(str):
    print(str+ ' é Palíndromo')
else:
    print(str+ ' não é Palíndromo')
