from tkinter import *
from math import sqrt
from tkinter import messagebox


class ViewCalculadora:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Calculadora')

        #deixar a janela centralizada
        window_height = 465
        window_width = 430
        screen_width = self.janela.winfo_screenwidth()
        screen_height = self.janela.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.janela.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #adicionar imagem de ícone da janela
        self.janela.iconbitmap('images/calc2.ico')

        #Fixar a janela em um só tamanho
        self.janela.resizable(False, False)

        #Comando para capturar caracter do teclado
        self.janela.bind(sequence="<KeyPress>", func=self.teclaLiberada)
        self.janela.bind("Return", self.igual)

        #variáveis auxiliares
        self.valorAtual = 0
        self.primeiroNum = ''
        self.operador = ''
        self.geraHistorico = ''

        #objestos da interface gráfica
        self.frameHistorico = Frame(self.janela)
        self.frameDisplayInfo = Frame(self.janela)
        self.frameDisplay = Frame(self.janela)
        self.frameButtons = Frame(self.janela)
        self.frameHistorico.pack()
        self.frameDisplayInfo.pack()
        self.frameDisplay.pack()
        self.frameButtons.pack() 

        self.image = PhotoImage(file='images/Historico.PNG')
        self.buttonHistorico = Button(self.frameHistorico, text='Histórico', font=('Heveltica 12'), image=self.image, bd=0.4, compound='left')
        self.buttonHistorico.grid()
        self.buttonHistorico.bind('<Button>', self.historico)

        self.displayInfo = Label(self.frameDisplayInfo, text='', font=('Arial Bold', 13))
        self.displayInfo.grid()
        self.displayInfo.config(width=45, justify='right', anchor='e')

        self.display = Label(self.frameDisplay, text='0', font=('Arial 37'))
        self.display.grid()
        self.display.config(width=14, justify='right', anchor='e')
        self.display.pack(expand=False, fill=BOTH)

        self.buttonApaga = Button(self.frameButtons, text='<-', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonApaga.bind('<Button>', self.apaga)
        self.buttonLimpaC = Button(self.frameButtons, text='C', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonLimpaC.bind('<Button>', self.limpaC)
        self.buttonLimpaCE = Button(self.frameButtons, text='CE', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonLimpaCE.bind('<Button>', self.limpaCE) 
        self.buttonTrocaSinal = Button(self.frameButtons, text='±', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonTrocaSinal.bind('<Button>', self.trocaSinal)

        self.buttonRaiz = Button(self.frameButtons, text='√', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonRaiz.bind('<Button>', self.raiz)
        self.buttonPorcentagem = Button(self.frameButtons, text='%', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonPorcentagem.bind('<Button>', self.porcentagem)
        self.buttonFatorial = Button(self.frameButtons, text='!', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonFatorial.bind('<Button>', self.fatorial)
        self.buttonElevado = Button(self.frameButtons, text='^', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonElevado.bind('<Button-1>', self.processa)

        self.button7 = Button(self.frameButtons, text='7', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.button7.bind('<Button-1>', self.setarLabel)
        self.button8 = Button(self.frameButtons, text='8', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.button8.bind('<Button-1>', self.setarLabel)
        self.button9 = Button(self.frameButtons, text='9', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.button9.bind('<Button-1>', self.setarLabel)
        self.buttonVezes = Button(self.frameButtons, text='x', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonVezes.bind('<Button-1>', self.processa)

        self.button4 = Button(self.frameButtons, text='4', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.button4.bind('<Button-1>', self.setarLabel)
        self.button5 = Button(self.frameButtons, text='5', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.button5.bind('<Button-1>', self.setarLabel)
        self.button6 = Button(self.frameButtons, text='6', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.button6.bind('<Button-1>', self.setarLabel)
        self.buttonMenos = Button(self.frameButtons, text='-', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonMenos.bind('<Button-1>', self.processa)
        
        self.button1 = Button(self.frameButtons, text='1', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.button1.bind('<Button-1>', self.setarLabel)
        self.button2 = Button(self.frameButtons, text='2', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.button2.bind('<Button-1>', self.setarLabel)
        self.button3 = Button(self.frameButtons, text='3', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.button3.bind('<Button-1>', self.setarLabel)
        self.buttonMais = Button(self.frameButtons, text='+', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonMais.bind('<Button-1>', self.processa)

        self.button0 = Button(self.frameButtons, text='0', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.button0.bind('<Button-1>', self.setarLabel)
        self.buttonPonto = Button(self.frameButtons, text='.', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.buttonPonto.bind('<Button-1>', self.setarLabel)
        self.buttonIgual = Button(self.frameButtons, text='=', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#ffffff")
        self.buttonIgual.bind('<Button>', self.igual)
        self.buttonDivisor = Button(self.frameButtons, text='÷', font=('Heveltica Bold', 14), width=9, height=2, bd=0.4, bg="#e0e8eb")
        self.buttonDivisor.bind('<Button-1>', self.processa)

        #Organização dos botões abaixo do display no seu respectivo Frame
        self.buttonApaga.grid(row=0, column=0)
        self.buttonLimpaC.grid(row=0, column=1)
        self.buttonLimpaCE.grid(row=0, column=2)
        self.buttonTrocaSinal.grid(row=0, column=3)
        self.buttonRaiz.grid(row=1, column=0)
        self.buttonPorcentagem.grid(row=1, column=1)
        self.buttonFatorial.grid(row=1, column=2)
        self.buttonElevado.grid(row=1, column=3)
        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)
        self.buttonVezes.grid(row=2, column=3)
        self.button4.grid(row=3, column=0)
        self.button5.grid(row=3, column=1)
        self.button6.grid(row=3, column=2)
        self.buttonMenos.grid(row=3, column=3)
        self.button1.grid(row=4, column=0)
        self.button2.grid(row=4, column=1)
        self.button3.grid(row=4, column=2)
        self.buttonMais.grid(row=4, column=3)
        self.button0.grid(row=5, column=0)
        self.buttonPonto.grid(row=5, column=1)
        self.buttonIgual.grid(row=5, column=2)
        self.buttonDivisor.grid(row=5, column=3)

        self.frameButtons.mainloop()
    
    #Tratando as entradas '.0123456789'seja pelo botão ou teclado -----------------------
    def tratarEntrada(self, evento):
        if evento == '.' and self.display['text']=='0':
            self.display['text'] = '0.'

        elif self.display['text'] == '0':
            self.display['text'] = evento
        
        elif evento == '.' and self.display['text'].count('.')==1:
            pass
            
        elif len(self.display['text'])<15:
            if self.display['text'].count('.')<=1:
                self.display['text'] += evento
    
    # Tratando as entradas '+-*/' seja pelo botão ou teclado -----------------------------
    def trataProcessa(self, evento):
        self.operador = evento
        self.displayInfo['text'] = self.display['text'] +' '+evento
        self.primeiroNum = self.display['text']
        self.display['text'] = '0'
    
    # Tratando o resultado da operação quando clicado: 'raiz, porcentagem, fatorial, igual' para não ultrapassar o display
    def resultado(self, display):
        if len(display) > 15:
            self.display['text'] = display[0:15]
        else:
            self.display['text'] = display

    ######################################################################
    def teclaLiberada(self, event):
        evento = repr(event.char)[1]
        enterBack = repr(event.char)[2:3]
        if evento in '.0123456789':
            self.tratarEntrada(evento)
        elif evento in '+-*/':
            self.trataProcessa(evento)
        elif enterBack=='x':
            self.trataApaga()
        elif enterBack=='r':
            self.trataIgual()
        #else:
            #print(evento)
    
    ######################################################################
    def setarLabel(self, event=None):
        evento = event.widget['text']
        self.tratarEntrada(evento)

    ######################################################################
    def limpaCE(self, event):
        self.display['text'] = '0'
        self.operador=''

    ######################################################################
    def limpaC(self, event):
        self.limpaCE(event)
        self.displayInfo['text'] = ''
    
    ######################################################################
    def apaga(self, event):
        self.trataApaga()

    ######################################################################
    def trataApaga(self):
        if len(self.display['text'])==1:
            self.display['text'] = '0'
        else:
            self.display['text'] = self.display['text'][:len(self.display['text'])-1]

    ######################################################################    
    def processa(self, event=None):
        evento = event.widget['text']
        self.trataProcessa(evento)
    
    ######################################################################
    def trataIgual(self):
        if self.operador != '':
            primeiroNum = float(self.primeiroNum)
            segundoNum = float(self.display['text'])
            
            error=False
            if self.operador == '^':
                resultado = primeiroNum ** segundoNum
            elif self.operador == 'x' or self.operador=='*':
                resultado = primeiroNum * segundoNum 
            elif self.operador == '-':
                resultado = primeiroNum - segundoNum
            elif self.operador == '+':
                resultado = primeiroNum + segundoNum
            elif self.operador == '÷' or self.operador =='/':
                if segundoNum!=0:
                    resultado = primeiroNum / segundoNum
                else:
                    self.display['text'] = 'Error!'
                    error=True
            else:
                pass
            
            if error==False:
                self.resultado(str(resultado)) 
                self.displayInfo['text'] += ' '+str(segundoNum) + ' ='
                self.geraHistorico += '=>> '+self.displayInfo['text'] + ' '+self.display['text']+'\n\n'

    ######################################################################
    def igual(self, event):
        self.trataIgual()

    ######################################################################
    def raiz(self, event):
        display = float(self.display['text'])
        resultado = sqrt(display)
        self.displayInfo['text'] += '√' + self.display['text']
        self.resultado(str(resultado))

    ######################################################################
    def porcentagem(self, event):
        if self.operador != '':
            primeiroNum = float(self.primeiroNum)
            segundoNum = float(self.display['text'])
            
            error=False
            if self.operador == '^':
                resultado = primeiroNum  ^ (segundoNum*primeiroNum)/100
            elif self.operador == 'x' or self.operador == '*':
                resultado = (segundoNum*primeiroNum)/100
            elif self.operador == '-':
                resultado = primeiroNum - (segundoNum*primeiroNum)/100
            elif self.operador == '+':
                resultado = primeiroNum + (segundoNum*primeiroNum)/100
            elif self.operador == '÷' or self.operador == '/':
                if segundoNum!=0:
                    resultado = (primeiroNum/segundoNum)*100
                else:
                    self.display['text'] = 'Error!'
                    error=True
            else:
                pass

            if error == False:
                self.resultado(str(resultado))
                self.displayInfo['text'] += str(segundoNum) + '%'
        else:
            resultado=float(self.display['text'])/100
            self.displayInfo['text'] += self.display['text'] + '%'
            self.resultado(str(resultado))

    ######################################################################
    def fatorial(self, event):
        if '.' not in self.display['text']:
            n = int(self.display['text'])
            fat = n
            for i in range(n-1, 1, -1):
                fat = fat * i
            self.displayInfo['text'] += self.display['text'] + '!' 
            self.resultado(str(fat))
        else:
            self.display['text'] +=  '!'

    ######################################################################
    def trocaSinal(self, event):
        if self.display['text'] != '0':
            if '-' in self.display['text']:
                self.display['text'] = self.display['text'][1:]
            else:
                self.display['text'] = '-' + self.display['text']
    
    ######################################################################
    def historico(self, event):
        messagebox.showinfo('Histórico das operações', self.geraHistorico)

######################################################################         
if __name__ == "__main__":
    calculadora = ViewCalculadora()