def mdc(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def mesmaFracao(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())    

class Fracao:
    
    def __init__(self, num, den):
        self.__num = num        
        self.__den = den     

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den       

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum   

    def __add__(self,outraFrac):
        novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
        novoDen = self.__den * outraFrac.getDen()
        divComum = mdc(novoNum, novoDen)
        novaFracao = Fracao(novoNum//divComum, novoDen//divComum)
        if novaFracao.getNum() / novaFracao.getDen() < 1:
            return novaFracao
        else:
            parteInt = novaFracao.getNum() // novaFracao.getDen()
            novoNum2 = novaFracao.getNum() - parteInt * novaFracao.getDen()
            fracMista = FracaoMista(parteInt, novoNum2, novaFracao.getDen())
            return fracMista  

class FracaoMista(Fracao):
    def __init__(self, parteInteira, num, den):
        super().__init__(num, den)
        self.__parteInteira = parteInteira

    def getParteInteira(self):
        return self.__parteInteira

    def __str__(self):
        return str(self.__parteInteira)+' '+str(self.getNum())+'/'+str(self.getDen())       


frac1 = Fracao (3, 4)
frac2 = Fracao(5, 6)
frac3 = frac1 + frac2
print(frac3)

print()

frac1 = Fracao (1, 4)
frac2 = Fracao(1, 6)
frac3 = frac1 + frac2
print(frac3)

