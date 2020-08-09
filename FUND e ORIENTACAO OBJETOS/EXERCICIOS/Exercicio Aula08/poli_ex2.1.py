from abc import ABC, abstractmethod

class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria

    def getNome(self):
        return self.__nome

    def getMatricula(self):
        return self.__matricula

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def calculaValorImposto(self, salBruto):
        if salBruto < 1903.99:
            imposto = 0
        elif salBruto < 2926.66:
            imposto = 7.5
        elif salBruto < 3751.06:
            imposto = 15
        elif salBruto < 4664.68:
            imposto = 22.5
        else: 
            imposto = 27.5
        if imposto == 0 :
            return  
        else: 
          return (salBruto*imposto)/100

    @abstractmethod
    def getSalario(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioBruto):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioBruto = salarioBruto

    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto

    def getSalarioBruto(self):
        return self.__salarioBruto

    def getSalario(self):
        previd = self.__salarioBruto*0.11
        imposto = self.calculaValorImposto(self.__salarioBruto)
        return self.__salarioBruto-(previd+imposto)

class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    def setSalarioHora(self, salarioHora):
        self.__salarioHora = salarioHora 

    def getSalarioHora(self):
        return self.__salarioHora

    def getSalario(self):
        salBruto = self.__salarioHora * self.getCargaHoraria()
        imposto = self.calculaValorImposto(salBruto)
        return salBruto-imposto

    

prof1 = ProfDE('Joao', 12345, 40, 5000)
prof2 = ProfHorista('Paulo', 54321, 30, 75)
prof3 = ProfHorista('Ana', 56789, 38, 95)
profs = [prof1, prof2, prof3]
for prof in profs:
    print ('Nome: {} - Salário: {}'.format(prof.getNome(), prof.getSalario()))
