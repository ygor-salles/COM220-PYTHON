"""6) Leia uma string e verifique se a mesma é um
palíndromo."""

str = input("Digite uma palavra: ")
print("Voce digitou: " + str)

palindromo = True

for i in range(int(len(str)/2)):
    if str[i] != str[len(str) - i - 1]:
        palindromo = False
        break

print()
#PALINdromo JA É TRUE
if palindromo:
    print(str + " é palindromo!!")

else:
    print(str + " nao é palindromo!!")

print()