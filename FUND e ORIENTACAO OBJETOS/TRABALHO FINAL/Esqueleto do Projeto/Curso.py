import Aluno as al
import Grade as gr

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

    def mostra(self):
        print ('Curso {}: \nGrade: Ano(a):{}'.format(self.__nome, self.__grade.getAno()))
        print('\nLista Disciplinas: ')
        listaDisc = self.__grade.getListaDisc()
        for i in listaDisc:
            print('Código: {} -- Disciplina: {} -- Carga Horária: {}'.format(i.getCodigo(), i.getNome(), i.getCargaHoraria()))
        print('\nLista dos Alunos: ')
        listaAlunos = self.__listaAlunos
        for i in listaAlunos:
            print('Matrícula: {} -- Aluno(a): {}'.format(i.getNroMatric(), i.getNome()))