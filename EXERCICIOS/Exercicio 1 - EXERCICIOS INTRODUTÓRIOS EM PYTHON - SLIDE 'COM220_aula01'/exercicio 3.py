# Exercicio 3  - SLide
#Leia uma data no passado e informe em qual dia da semana essa data caiu.

from datetime import datetime
data_str = input('Informe data nasc (dd/mm/yyyy): ')
data = datetime.strptime(data_str, '%d/%m/%Y')

print(data.strftime("%A"))