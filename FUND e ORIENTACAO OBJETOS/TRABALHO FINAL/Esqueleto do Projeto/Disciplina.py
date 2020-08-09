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
    
    def __str__(self):
        return 'Codigo: {} -- Disciplina: {} -- Carga Horária: {}'.format(self.__codigo, self.__nome, self.__cargaHoraria)