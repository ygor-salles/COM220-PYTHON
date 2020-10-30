# Ygor Salles - 2017014382

class Aluno:
    def __init__(self, nroMatric, nome, historico, grade):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__historico = historico
        self.__grade = grade
    
    def getNome(self):
        return self.__nome
    
    def getNroMatric(self):
        return self.__nroMatric
    
    def getHistorico(self):
        return self.__historico
    
    def getGrade(self):
        return self.__grade

class Curso:
    def __init__(self, nome, listaAlunos, grade):
        self.__nome = nome
        self.__listaAlunos = listaAlunos
        self.__grade = grade
    
    def getNome(self):
        return self.__nome

    def getListaAlunos(self):
        return self.__listaAlunos
    
    def getGrade(self):
        return self.__grade

class Grade:
    def __init__(self, ano, listaDisc):
        self.__ano = ano
        self.__listaDisc = listaDisc

    def getAno(self):
        return self.__ano

    def getListaDisc(self):
        return self.__listaDisc

class Disciplina:
    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
    
    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getCargaHoraria(self):
        return self.__cargaHoraria

class Historico:
    def __init__(self, listaDisc):
        self.__listaDisc = listaDisc
    
    def getListaDisc(self):
        return self.__listaDisc


#adicionando disciplinas - lembrando que as matérias COM são obrigatórias para SIN e CCO
disc1 = Disciplina('COM110', 'Fundamentos de Programação', 80)
disc2 = Disciplina('COM111', 'Estrutura de Dados I', 96)
disc3 = Disciplina('MAT001', 'Calculo I', 96)
disc4 = Disciplina('SIN130', 'Fundamentos de Computação', 64)
disc5 = Disciplina('COM312', 'Informática e Sociedade', 64)
disc6 = Disciplina('MAT011', 'Geometria Analitica e Algebra Linear ', 64)
disc7 = Disciplina('CIC270', 'Computação Gráfica', 48)
disc8 = Disciplina('CIC271', 'Processamento de Imagens', 64)
disc9 = Disciplina('SIN414', 'Auditoria em SI', 48)
disc10 = Disciplina('SIN210', 'GOvernança em TI', 64)

#definindo grade de Sistemas 2018
listaGradeSin = [disc1, disc2, disc4, disc5, disc9, disc10]
gradeSin = Grade(2018, listaGradeSin)

#definindo grade de CCO
listaGradeCco = [disc1, disc2, disc3, disc5, disc6, disc7, disc8]
gradeCco = Grade(2018, listaGradeCco)

#processando o histórico dos alunos
listaCursadas1 = [disc1, disc2, disc3, disc4, disc5, disc6, disc7, disc8, disc9, disc10]
historico1 = Historico(listaCursadas1)
listaCursadas2 = [disc1, disc7, disc8, disc2, disc3]
historico2 = Historico(listaCursadas2)
listaCursadas3 = [disc1, disc2, disc9, disc10]
historico3 = Historico(listaCursadas3)
listaCursadas4 = [disc3, disc4, disc5, disc8, disc9, disc10]
historico4 = Historico(listaCursadas4)
aluno1 = Aluno(201701, 'Benedito Jose Bezerra', historico1, gradeSin)
aluno2 = Aluno(201702, 'Claudio Magalhaes', historico2, gradeSin)
aluno3 = Aluno(201703, 'Diana Jacinto', historico3, gradeCco)
aluno4 = Aluno(201704, 'Duarte Pereira', historico4, gradeCco)

#alunos matriculados em sistemas e alunos matriculas em CCO
listaAlunosSin = [aluno1, aluno2]
cursoSin = Curso('Sistemas de Informação', listaAlunosSin, gradeSin)
listaAlunosCco = [aluno3, aluno4]
cursoCco = Curso('Ciência da Computação', listaAlunosCco, gradeCco)

#Função imprime histórico da lista de disciplinas do Aluno
def imprimeDisciplinas(aluno):
    obrigatoria=0
    eletiva=0
    print('\nMatrícula: {} \nAluno(a): {}'.format(aluno.getNroMatric(), aluno.getNome()))
    print('Lista de Disciplinas do Histórico: ')
    lista = aluno.getHistorico().getListaDisc()
    grade = aluno.getGrade().getListaDisc()
    for i in lista:
        encontrou=False
        print('Codigo: {} -- Disciplina: {} -- Carga Horária: {}'.format(i.getCodigo(), i.getNome(), i.getCargaHoraria()))
        for j in grade:
            if i.getCodigo() == j.getCodigo():
                obrigatoria += i.getCargaHoraria()
                encontrou=True
        if(encontrou==False):
            eletiva += i.getCargaHoraria()
    print('Total Carga Horária obrigatória: {} \nTotal Carga Horária eletiva: {}\n'.format(obrigatoria, eletiva)) 

imprimeDisciplinas(aluno1)
imprimeDisciplinas(aluno2)
imprimeDisciplinas(aluno3)
imprimeDisciplinas(aluno4)