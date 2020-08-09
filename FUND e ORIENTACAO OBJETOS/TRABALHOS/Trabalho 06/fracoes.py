#Ygor Salles - 2017014382

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
        inteiro = (self.__num + outraFrac.getNum())//self.__den

        if novaFracao.getNum() / novaFracao.getDen() < 1:
            return novaFracao
        elif novaFracao.getNum() % novaFracao.getDen() == 0:
            return inteiro
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

    def __add__(self, outraFrac):
        #passando de mista para imprópria
        num = self.getDen() * self.__parteInteira + self.getNum()       
        novoNum = outraFrac.getDen() * outraFrac.getParteInteira() + outraFrac.getNum()
        den = self.getDen()
        novoDen = outraFrac.getDen()

        #fazendo o mmc borboleta
        Numerador = num * novoDen + den * novoNum
        Denominador = den * novoDen

        #passando de imprópria para mista
        parteInteira = Numerador//Denominador
        NumeradorFinal = Numerador%Denominador
        DenominadorFinal = Denominador

        #teste para soma de frações mistas que retornam inteiro ou não(retornam fração mista mesmo)
        if Numerador % Denominador == 0:
            return str(Numerador // Denominador)
        else:
            return FracaoMista(parteInteira, NumeradorFinal, DenominadorFinal)

print()
frac1 = Fracao (7, 6)
frac2 = Fracao(13, 7)
frac3 = frac1 + frac2
print(frac3)

print()

frac1 = Fracao (1, 3)
frac2 = Fracao(2, 3)
frac3 = frac1 + frac2
print(frac3)

print()

frac1 = FracaoMista(3, 1, 2)
frac2 = FracaoMista(4, 2, 3)
frac3 = frac1 + frac2
print(frac3)

print()

#um exemplo de soma de fração mista que devolve um valor inteiro
#frac1 = FracaoMista(3, 1, 3)
#frac2 = FracaoMista(1, 2, 3)
#frac3 = frac1 + frac2
#print(frac3)