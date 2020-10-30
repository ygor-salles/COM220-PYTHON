import Aluno as al
import Disciplina as dic
import Grade as gr

class Historico:
    def __init__(self, listaDisc, aluno, grade):
        self.__listaDisc = listaDisc
        self.__aluno = aluno
        self.__grade = grade
        self.__semestre = None
        self.__notaAluno = None
        self.__statusAprovacao = None
        self.__eletiva = 0
        self.__obrigatoria = 0
    
    def getListaDisc(self):
        return self.__listaDisc

    def getAluno(self):
        return self.__aluno
    
    def getGrade(self):
        return self.__grade
    
    def getSemestre(self):
        return self.__semestre
    
    def setSemestre(self, semestre):
        self.__semestre = semestre
    
    def getNotaAluno(self):
        return self.__notaAluno

    def setNotaAluno(self, notaAluno):
        self.__notaAluno = notaAluno
    
    def getStatusAprovacao(self):
        return self.__statusAprovacao
    
    def getEletiva(self):
        return self.__eletiva

    def getObrigatoria(self):
        return self.__obrigatoria

    def mostra(self):
        print('EMISSÃO DE HISTÓRICO DO ALUNO')
        print('Dados Pessoais::...')
        print('Matricula: {}'.format(self.__aluno.getNroMatric()))
        print('Aluno: {}'.format(self.__aluno.getNome()))
        print('Curso: {}'.format(self.__aluno.getCurso()))
        
        grade = self.__grade.getListaDisc()
        print('\n       HISTÓRICO   ')
        print(' Ano |   Semestre   |   COD  |   DISCIPLINA  |   CH  |   NOTA    |   STATUS APROVAÇÃO    |')
        for i in self.__listaDisc:
            encontrou=False
            print('{} |     {}     |  {}  |  {} |  {}  |   {}  |   {}      |'\
                .format(self.__grade.getAno(), self.getSemestre(), i.getCodigo(), i.getNome(), i.getCargaHoraria(), self.getNotaAluno(), self.getStatusAprovacao()))
            for j in grade:
                if i.getCodigo() == j.getCodigo():
                    self.__obrigatoria += i.getCargaHoraria()
                    encontrou=True
            if(encontrou==False):
                self.__eletiva += i.getCargaHoraria()
        print('\nTotal Carga Horária obrigatória: {} \nTotal Carga Horária eletiva: {}\n'.format(self.__obrigatoria, self.__eletiva)) 