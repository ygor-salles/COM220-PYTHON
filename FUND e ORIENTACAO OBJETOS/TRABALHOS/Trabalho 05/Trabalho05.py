from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
    
    def getNome(self):
        return self.__nome
    
    def getTelefone(self):
        return self.__telefone
    
    def setNome(self, name):
        self.__nome = name
    
    def setTelefone(self, fone):
        self.__telefone = fone
    
    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.horasTrabalhadas = horasTrabalhadas
        self.valorPorHora = valorPorHora
    
    def getSalario(self):
        return self.horasTrabalhadas*self.valorPorHora


class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.diasTrabalhados = diasTrabalhados
        self.valorPorDia = valorPorDia
    
    def getSalario(self):
        return self.diasTrabalhados*self.valorPorDia


class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.valorMensal = valorMensal
    
    def getSalario(self):
        return self.valorMensal


horista1 = Horista('Luzidelma', '(35)98414-1352', 160, 10)
diarista1 = Diarista('Francisca', '(35)98752-3654', 20, 55)
mensalista1 = Mensalista('Maria', '(35)97414-9635', 1000)

lista = [horista1, diarista1, mensalista1]

print('\nO valor mensal de cada uma é: ')
menor = horista1.getSalario() #primeiro elemento da lista
for elem in lista:
    print(elem.getSalario())
    if (elem.getSalario() < menor):
        menor = elem.getSalario()
        nome = elem.getNome()
        telefone = elem.getTelefone()

print('\nA EMPREGADA MAIS BARATA PARA A REPÚBLIC SERÁ A... ')
print('Mensalista: {} \nTelefone: {} \nValor Mensal: {}'.format(nome, telefone, menor)+'\n')
