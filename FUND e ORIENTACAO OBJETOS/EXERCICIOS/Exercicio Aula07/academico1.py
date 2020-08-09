from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco
        
    def getIdade(self):
        return self.__idade
    
    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao):
        super().__init__(nome, endereco, idade)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereco: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Titulacao: {}'.format(self.getTitulacao()))

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso):
        super().__init__(nome, endereco, idade)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereco: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Curso: {}'.format(self.getCurso()))

prof = Professor('Joao', 'Av. BPS, 1303', 33, 'doutorado')
prof.printDescricao()
print()
aluno = Aluno('Pedro', 'Av. Cesario Alvin, 234', 20, 'SIN')
aluno.printDescricao()    


    