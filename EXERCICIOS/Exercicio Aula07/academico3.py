from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, listaDisc):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__listaDisc = listaDisc

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco
        
    def getIdade(self):
        return self.__idade

    def getListaDisc(self):
        return self.__listaDisc
    
    def insereDisc(self, disc):
        self.__listaDisc.append(disc)

    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao, listaDisc):
        super().__init__(nome, endereco, idade, listaDisc)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereco: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Titulacao: {}'.format(self.getTitulacao()))
        print('Discilina(s) Ministrada(s)')
        listaDisc = self.getListaDisc()
        for disc in listaDisc:
            print('Nome: {} - Carga Horária: {}'.format(disc.getNomeDisc(), disc.getCargaHoraria()))

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso, listaDisc):
        super().__init__(nome, endereco, idade, listaDisc)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereco: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Curso: {}'.format(self.getCurso()))
        print('Discilina(s) Cursadas(s)')
        listaDisc = self.getListaDisc()
        for disc in listaDisc:
            print('Nome: {} - Carga Horária: {}'.format(disc.getNomeDisc(), disc.getCargaHoraria()))        

class Disciplina():
    def __init__(self, nomeDisc, cargaHoraria):
        self.__nomeDisc = nomeDisc
        self.__cargaHoraria = cargaHoraria

    def getNomeDisc(self):
        return self.__nomeDisc

    def getCargaHoraria(self):
        return self.__cargaHoraria


disc1 = Disciplina('Programacao OO', 64)
disc2 = Disciplina('Estruturas de Dados', 64)
disc3 = Disciplina('Banco de Dados', 64)

prof = Professor('Joao', 'Av. BPS, 1303', 33, 'doutorado', [])
prof.insereDisc(disc1)
prof.insereDisc(disc2)
prof.printDescricao()
print()
aluno = Aluno('Pedro', 'Av. Cesario Alvin, 234', 20, 'SIN', [])
aluno.insereDisc(disc2)
aluno.insereDisc(disc3)
aluno.printDescricao()  
aluno.insereDisc(disc1) 
aluno.printDescricao()  



    