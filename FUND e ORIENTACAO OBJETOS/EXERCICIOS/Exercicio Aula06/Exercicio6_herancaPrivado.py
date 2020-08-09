class Veiculo:
    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado

    def getMarca(self):
        return self.__marca
    
    def getCor(self):
        return self.__cor
    
    def isMotorLigado(self):
        return self.__motorLigado
    
    def ligaMotor(self):
        if self.__motorLigado == True:
            print('O motor está ligado')
        else:
            self.__motorLigado = True
            print('O motor acaba de ser ligado')

class Carro(Veiculo):
    def __init__(self, marca, cor, motorLigado, portaMalasCheio):
        super().__init__(marca, cor, motorLigado)
        self.__portaMalasCheio = portaMalasCheio
    
    def isPortaMalasCheio(self):
        return self.__portaMalasCheio
    
    def enchePortaMalas(self):
        if self.__portaMalasCheio == True:
            print('Porta malas já está cheio')
        else:
            self.__portaMalasCheio = True
            print('Porta Malas acaba de ser carregado')
    
    def mostraAtributos(self):
        print('Este carro é um {} {}'.format(self.getMarca(), self.getCor()))
        if(self.isMotorLigado()):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')
        if(self.isPortaMalasCheio()):
            print('Seu porta malas está cheio')
        else:
            print('Seu porta malas está vazio')

class Motocicleta(Veiculo):
    def __init__(self, marca, cor, motorLigado, estilo):
        super().__init__(marca, cor, motorLigado)
        self.__estilo = estilo
    
    def getEstilo(self):
        return self.__estilo
    
    def mostraAtributos(self):
        print('Esta moto é uma {} {} estilo {}'.format(self.getMarca(), self.getCor(), self.getEstilo()))
        if(self.isMotorLigado()):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')


moto = Motocicleta('Honda', 'Azul', False, 'Naked')
moto.mostraAtributos()
moto.ligaMotor()
moto.mostraAtributos()
print()
carro = Carro('Chevrolet', 'Branco', False, False)
carro.mostraAtributos()
carro.enchePortaMalas()
carro.ligaMotor()
carro.mostraAtributos()



    

