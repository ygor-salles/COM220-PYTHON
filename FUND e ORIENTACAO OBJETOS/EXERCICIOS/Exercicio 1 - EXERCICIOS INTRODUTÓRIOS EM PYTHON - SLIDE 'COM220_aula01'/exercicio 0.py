#Imprimir Dia mês e Ano da data atual

from datetime import datetime
data_corrente = datetime.now()

print('Dia: ' + str(data_corrente.day))
print('Mês: ' + str(data_corrente.month))
print('Ano: ' + str(data_corrente.year))