import tkinter as tk
from tkinter import messagebox

class EstudanteNaoCadastrado(Exception):
    pass

class Estudante:
    def __init__(self, nroMatric, nome):
        self.__nroMatric = nroMatric
        self.__nome = nome

    def getNroMatric(self):
        return self.__nroMatric
    
    def getNome(self):
        return self.__nome

class LimiteInsereEstudantes():
    def __init__(self, controle, root):
        self.janela=tk.Toplevel()
        self.janela.geometry('250x100')
        self.janela.title('Insere Estudante')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameNro = tk.Frame(self.janela)
        self.frameNome = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNro = tk.Label(self.frameNro,text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraEstudantes():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)

class LimiteConsultaEstudante():
    def __init__(self, controle, root):
        self.janela=tk.Toplevel()
        self.janela.geometry('250x100')
        self.janela.title('Consulta Estudante')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameMatricula = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameMatricula.pack()
        self.frameButton.pack()

        self.labelMatricula = tk.Label(self.frameMatricula, text='Matricula: ')
        self.labelMatricula.pack(side='left')

        self.inputTextMatricula = tk.Entry(self.frameMatricula, width=30)
        self.inputTextMatricula.pack(side='left')

        self.buttonConsultar = tk.Button(self.frameButton, text='Realizar Consulta')
        self.buttonConsultar.pack(side='left')
        self.buttonConsultar.bind('<Button>', controle.consultaHandler)

        self.buttonClear = tk.Button(self.frameButton ,text='Clear')      
        self.buttonClear.pack(side='left')
        self.buttonClear.bind('<Button>', controle.clearEstudante)  

        self.buttonFecha = tk.Button(self.frameButton ,text='Finalizar')      
        self.buttonFecha.pack(side='left')
        self.buttonFecha.bind('<Button>', controle.fechaEstudante)
    
    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
      
class CtrlEstudante():       
    def __init__(self):
        self.listaEstudantes = [
            Estudante('1001', 'Joao Santos'),
            Estudante('1002', 'Marina Cintra'),
            Estudante('1003', 'Felipe Reis'),
            Estudante('1004', 'Ana Souza')
        ]

    def getEstudante(self, nroMatric):
        estRet = None
        for est in self.listaEstudantes:
            if est.getNroMatric() == nroMatric:
                estRet = est
        return estRet

    def getListaNroMatric(self):
        listaNro = []
        for est in self.listaEstudantes:
            listaNro.append(est.getNroMatric())
        return listaNro

    def insereEstudantes(self, root):
        self.limiteIns = LimiteInsereEstudantes(self, root) 

    def mostraEstudantes(self):
        str = 'Nro Matric. -- Nome\n'
        for est in self.listaEstudantes:
            str += est.getNroMatric() + ' -- ' + est.getNome() + '\n'       
        self.limiteLista = LimiteMostraEstudantes(str)
    
    def consultaEstudantes(self, root):
        self.limiteConsulta = LimiteConsultaEstudante(self, root)

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        estudante = Estudante(nroMatric, nome)
        self.listaEstudantes.append(estudante)
        self.limiteIns.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.janela.destroy()
    
    def consultaHandler(self, event):
        matricula = self.limiteConsulta.inputTextMatricula.get()
        try:
            encontrou=False
            for i in self.listaEstudantes:                    
                if matricula == i.getNroMatric():
                    nomeEst = i.getNome()
                    matriculaEst = i.getNroMatric()
                    encontrou=True
            if encontrou==False:        
                raise EstudanteNaoCadastrado()
        except EstudanteNaoCadastrado:
            self.limiteConsulta.mostraMessagebox('Alerta', 'Estudante não cadastrado')
        else:
            str = 'Estudante cadastrado \nMatrícula -- Nome \n'+matriculaEst+' -- '+nomeEst
            LimiteMostraEstudantes(str)
        finally:
            self.clearEstudante(event)
    
    def clearEstudante(self, event):
         self.limiteConsulta.inputTextMatricula.delete(0, len(self.limiteConsulta.inputTextMatricula.get()))
    
    def fechaEstudante(self, event):
        self.limiteConsulta.janela.destroy()