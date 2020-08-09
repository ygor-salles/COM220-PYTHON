#Exercicio 1 - Slide
#Leia duas strings e verifique se a segunda está contida na primeira.

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

if str2 in str1: 
	print (str2 + " está contida em " + str1)
else:  
	print (str2 + " não está contida em " + str1)