import Disciplina as dic

class Grade:
    def __init__(self, ano, listaDisc):
        self.__ano = ano
        self.__listaDisc = listaDisc
        self.__curso = None

    def getAno(self):
        return self.__ano

    def getListaDisc(self):
        return self.__listaDisc
    
    def setCurso(self, curso):
        self.__curso = curso

    def getCurso(self):
        return self.__curso
        
    def mostra(self):
        print ('Ano: {} \nLista de Disciplinas: '.format(self.__ano))
        print('Curso: {}'.format(self.getCurso()))
        lista = self.__listaDisc
        for i in lista:
            print('Código: {} -- Disciplina: {} -- Carga Horária: {}'.format(i.getCodigo(), i.getNome(), i.getCargaHoraria()))
