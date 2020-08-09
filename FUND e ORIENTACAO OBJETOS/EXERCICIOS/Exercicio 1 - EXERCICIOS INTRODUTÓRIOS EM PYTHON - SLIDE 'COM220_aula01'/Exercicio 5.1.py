"""5) Leia um conjunto de nomes e os armazene numa lista. Em
seguida, leia um nome e verifique se o mesmo faz parte
dessa lista."""

quantidade_de_nomes = int(input("\nQuantos nomes voce quer digitar? "))
print(str(quantidade_de_nomes) + " nomes a ser digitado")

lista_de_nomes = []

while quantidade_de_nomes != 0:
    nomes = input("Digite o nome: ")
    lista_de_nomes.append(nomes)
    quantidade_de_nomes = quantidade_de_nomes - 1

print("Sua Lista de nomes: " + str(lista_de_nomes))

print()
nome_buscar = input("Agora digite um nome qualquer: ")

if nome_buscar in lista_de_nomes:
    print(str(nome_buscar) + " esta na Lista de nomes!!")
else:
    print(str(nome_buscar) + " não esta na Lista de nomes!!")

print("\n\n")