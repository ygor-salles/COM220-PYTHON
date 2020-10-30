class Aluno:
    def __init__(self, nroMatric, nome):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = None

    def getNroMatric(self):
        return self.__nroMatric
    
    def getNome(self):
        return self.__nome
    
    def setCurso(self, curso):
        self.__curso = curso
    
    def getCurso(self):
        return self.__curso
        
    def __str__(self):
        return 'Matricula: {} -- Nome: {} -- Curso: {}'.format(self.__nroMatric, self.__nome, self.getCurso())