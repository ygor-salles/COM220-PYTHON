""" 8) Escreva uma função que receba um float representando o valor da temperatura em Celsius
 e retorne a temperatura equivalente em Farenheit. Em seguida,
  escreva um código que leia uma temperatura em Celsius e informe o valor equivalente em Farenheit. """

def converte_temperatura(celcius):
    return (celcius * 9/5) + 32

celcius = float(input('Digite a temperatura em celsius: '))
Farenheit = converte_temperatura(celcius)

print('A temperatura em fareneit é: ' +str(Farenheit))

  
