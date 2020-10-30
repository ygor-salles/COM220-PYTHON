import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class DisciplinaNaoCadastrada(Exception):
    pass

class DisciplinaDuplicada(Exception):
    pass

class Disciplina:
    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        self.__notaAluno = None
    
    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getCargaHoraria(self):
        return self.__cargaHoraria
        

class LimiteInsereDisciplinas():
    def __init__(self, controle, root):
        self.janela = tk.Toplevel()
        self.janela.geometry('300x100')
        self.janela.title('Insere Disciplina')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameNome = tk.Frame(self.janela)
        self.frameCodigo = tk.Frame(self.janela)
        self.frameCargaHoraria =  tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameCargaHoraria.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelCargaHoraria = tk.Label(self.frameCargaHoraria, text='Carga Horária: ')
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelCargaHoraria.pack(side='left')  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=35)
        self.inputNome.pack(side="left")
        self.inputCargaHoraria = tk.Entry(self.frameCargaHoraria, width=5)
        self.inputCargaHoraria.pack(side='left')             
      
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraMessagebox(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraDisciplinas():
    def __init__(self, string):
        messagebox.showinfo('Lista de disciplinas', string)

class LimiteConsultaDisciplina():
    def __init__(self, controle, root):
        self.janela=tk.Toplevel()
        self.janela.geometry('200x100')
        self.janela.title('Consulta Disciplinas')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameCodigo = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameCodigo.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text='Codigo: ')
        self.labelCodigo.pack(side='left')

        self.inputTextCodigo = tk.Entry(self.frameCodigo, width=30)
        self.inputTextCodigo.pack(side='left')

        self.buttonConsultar = tk.Button(self.frameButton, text='Realizar Consulta')
        self.buttonConsultar.pack(side='left')
        self.buttonConsultar.bind('<Button>', controle.consultaHandler)

        self.buttonClear = tk.Button(self.frameButton ,text='Clear')      
        self.buttonClear.pack(side='left')
        self.buttonClear.bind('<Button>', controle.clearConsulta)  

        self.buttonFecha = tk.Button(self.frameButton ,text='Finalizar')      
        self.buttonFecha.pack(side='left')
        self.buttonFecha.bind('<Button>', controle.fechaConsulta)
    
    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

      
class CtrlDisciplina():       
    def __init__(self):
        if not os.path.isfile("Disciplina.pickle"):
            self.listaDisciplinas =  []
        else:
            with open("Disciplina.pickle", "rb") as f:
                self.listaDisciplinas = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaDisciplinas(self):
        if len(self.listaDisciplinas) != 0:
            with open("Disciplina.pickle","wb") as f:
                pickle.dump(self.listaDisciplinas, f)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------

    def getDisciplina(self, codDisc):
        discRet = None
        for disc in self.listaDisciplinas:
            if disc.getCodigo() == codDisc:
                discRet = disc
        return discRet

    def getListaCodDisciplinas(self):
        listaCod = []
        for disc in self.listaDisciplinas:
            listaCod.append(disc.getCodigo())
        return listaCod

    #Funções que serão chamadas na Main --- Instaciadores ---------------------------

    def insereDisciplinas(self, root):
        self.limiteIns = LimiteInsereDisciplinas(self, root) 

    def mostraDisciplinas(self):
        string = 'Código -- Nome -- Carga Horária\n'
        for disc in self.listaDisciplinas:
            string += disc.getCodigo()+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
        self.limiteLista = LimiteMostraDisciplinas(string)
    
    def consultaDisciplinas(self, root):
        self.limiteConsulta = LimiteConsultaDisciplina(self, root)
    
    #Funções dos Buttons Janela de Inserção de Disciplina -----------------------------------

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        disc = self.getDisciplina(codigo)
        try:
            if disc != None:
                raise DisciplinaDuplicada()
        except DisciplinaDuplicada:
            messagebox.showerror('Alerta', 'Disciplina já cadastrada!')
        else:
            nome = self.limiteIns.inputNome.get()
            ch = self.limiteIns.inputCargaHoraria.get()
            self.listaDisciplinas.append(Disciplina(codigo, nome, ch))
            self.limiteIns.mostraMessagebox('Sucesso', 'Disciplina cadastrada com sucesso')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCargaHoraria.delete(0, len(self.limiteIns.inputCargaHoraria.get()))

    def fechaHandler(self, event):
        self.limiteIns.janela.destroy()

    #Funções dos Buttons Janela de Consulta de Disciplina ----------------------------------------------
    
    def consultaHandler(self, event):
        codigo = self.limiteConsulta.inputTextCodigo.get()
        disc = self.getDisciplina(codigo)
        try:
            if disc == None:
                raise DisciplinaNaoCadastrada() 
        except DisciplinaNaoCadastrada:
            messagebox.showerror('Alerta', 'Disciplina não cadastrada')
        else:
            string = 'Disciplina cadastrada \nCódigo -- Nome -- Carga Horária \n'+codigo+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())
            LimiteMostraDisciplinas(string)
        finally:
            self.clearConsulta(event)
    
    def clearConsulta(self, event):
        self.limiteConsulta.inputTextCodigo.delete(0, len(self.limiteConsulta.inputTextCodigo.get()))
    
    def fechaConsulta(self, event):
        self.limiteConsulta.janela.destroy()