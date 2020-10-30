#Ygor Salles - 2017014382

#definindo as exceptions
class TitulacaoInvalida(Exception):
    pass

class IdadeMaiorIgualTrinta(Exception):
    pass

class CursoInvalido(Exception):
    pass

class IdadeMaiorIgualDezoito(Exception):
    pass

class CpfDuplicado(Exception):
    pass

from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf, endereco, idade):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf

    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf

    def getEndereco(self):
        return self.__endereco
        
    def getIdade(self):
        return self.__idade
    
    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, titulacao):
        super().__init__(nome, cpf, endereco, idade)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('Professor: {}'.format(self.getNome()))
        print('CPF: {}'.format(self.getCpf()))
        print('Endereco: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Titulacao: {}'.format(self.getTitulacao()))

class Aluno(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, curso):
        super().__init__(nome, cpf, endereco, idade)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('Aluno: {}'.format(self.getNome()))
        print('CPF: {}'.format(self.getCpf()))
        print('Endereco: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Curso: {}'.format(self.getCurso()))

lista = [
    ('Joao', '142.455.454-44', 'Av. BPS, 1303', 33, 'doutorado', 'professor'),
    ('Maria', '115.248.369-77', 'Av. BPS, 1303', 28, 'doutorado', 'professor'),
    ('Bosco', '142.362.987-00', 'Av. BPS, 1303', 40, 'doutorado', 'professor'),
    ('Pedro', '142.362.987-00', 'Av. BPS, 1302', 29, 'mestrado', 'professor'),
    ('Roberto', '012.362.987-00', 'Av. BPS, 1303', 28, 'doutorado', 'professor'),
    ('José', '142.455.454-10', 'Av. Cesario Alvin, 234', 27, 'SIN', 'aluno'),
    ('Antonio', '323.254.126-89', 'Av. BPS, 1302', 28, 'CCO', 'aluno'),
    ('Kaique', '147.369.987-88', 'Av. Cesario Alvin, 234', 20, 'ELT', 'aluno'),
    ('Mauricio', '142.455.454-10', 'Av. BPS, 1305', 19, 'MAT', 'aluno'),
    ('Cassio', '142.362.987-00', 'Rua Dom Ferroso, 87', 20, 'SIN', 'aluno'),
    ('Frederico', '147.225.633-99', 'Rua São José, 234', 17, 'CCO', 'aluno'),
]
#foi adicionado um novo atributo para indicar se tal registro é de um aluno ou professor

cadastro = {}

print('\nEXCESSÕES GERADAS: ')
for nome, cpf, endereco, idade, titulacaoCurso, classe in lista:
    try:
        if cpf in cadastro:
            raise CpfDuplicado()
        if titulacaoCurso!='doutorado' and classe=='professor':
            raise TitulacaoInvalida()
        if idade<=30 and classe=='professor':
            raise IdadeMaiorIgualTrinta()
        if (titulacaoCurso!='SIN' and titulacaoCurso!='CCO') and classe=='aluno':
            raise CursoInvalido()
        if idade<18 and classe=='aluno':
            raise IdadeMaiorIgualDezoito()

    except TitulacaoInvalida:
        print("'{}' -- Titulação aceita é de doutorado, sua titulação é: '{}'".format(nome, titulacaoCurso))
    except IdadeMaiorIgualTrinta:
        print("'{}' -- Idade deve ser maior que 30, sua idade é: '{}'".format(nome, idade))
    except CursoInvalido:
        print("'{}' -- Curso incorreto, seu curso é: '{}'".format(nome, titulacaoCurso))
    except IdadeMaiorIgualDezoito:
        print("'{}' -- Idade deve ser maior que 18, sua idade é: '{}'".format(nome, idade))
    except CpfDuplicado:
        print("'{}' -- CPF já existente: '{}'".format(nome, idade))
    
    else:
        if classe=='aluno':
            cadastro[cpf] = Aluno(nome, cpf, endereco, idade, titulacaoCurso)
        else:
            cadastro[cpf] = Professor(nome, cpf, endereco, idade, titulacaoCurso)

print('\nPESSOAS CADASTRADAS: ')
for i in cadastro:
    cadastro[i].printDescricao()
    print()
    