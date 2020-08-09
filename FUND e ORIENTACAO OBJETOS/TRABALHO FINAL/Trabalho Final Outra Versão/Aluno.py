import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class AlunoDuplicado(Exception):
    pass

class AlunoNaoCadastrado(Exception):
    pass

class Aluno():
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
        
class LimiteInsereAluno():
    def __init__(self, controle, root):
        self.janela=tk.Toplevel()
        self.janela.geometry('300x100')
        self.janela.title('Insere Aluno')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameNro = tk.Frame(self.janela)
        self.frameNome = tk.Frame(self.janela)
        self.frameCurso = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameCurso.pack()
        self.frameButton.pack()
      
        self.labelNro = tk.Label(self.frameNro, text="Matrícula: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelCurso = tk.Label(self.frameCurso, text='Curso: ')
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelCurso.pack(side='left')  

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=35)
        self.inputNome.pack(side="left")
        self.inputCurso = tk.Entry(self.frameCurso, width=4)
        self.inputCurso.pack(side='left')             
      
        self.buttonEnter = tk.Button(self.frameButton ,text="Enter")      
        self.buttonEnter.pack(side="left")
        self.buttonEnter.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraMessagebox(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraAlunos():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)

class LimiteConsultaAluno():
    def __init__(self, controle, root):
        self.janela=tk.Toplevel()
        self.janela.geometry('250x100')
        self.janela.title('Consulta Aluno')
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
        self.buttonConsultar.bind('<Button>', controle.consultaAluno)

        self.buttonClear = tk.Button(self.frameButton ,text='Clear')      
        self.buttonClear.pack(side='left')
        self.buttonClear.bind('<Button>', controle.clearAluno)  

        self.buttonFecha = tk.Button(self.frameButton ,text='Finalizar')      
        self.buttonFecha.pack(side='left')
        self.buttonFecha.bind('<Button>', controle.fechaAluno)
    
    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class CtrlAluno():       
    def __init__(self):
        if not os.path.isfile("Aluno.pickle"):
            self.listaAlunos =  []
        else:
            with open("Aluno.pickle", "rb") as f:
                self.listaAlunos = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaAlunos(self):
        if len(self.listaAlunos) != 0:
            with open("Aluno.pickle","wb") as f:
                pickle.dump(self.listaAlunos, f)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------
    
    def getAluno(self, nroMatric):
        alunoRet = None
        for aluno in self.listaAlunos:
            if aluno.getNroMatric() == nroMatric:
                alunoRet = aluno
        return alunoRet
    
    def getListaNroMatric(self):
        listNroMatric = []
        for matric in self.listaAlunos:
            listNroMatric.append(matric.getNroMatric())
        return listNroMatric
    
    #Funções que serão chamadas na Main --- Instaciadores ---------------------------

    def insereAlunos(self, root):
        self.limiteIns = LimiteInsereAluno(self, root) 

    def mostraAlunos(self):
        str = 'Nro Matric. -- Nome -- Curso\n'
        for aluno in self.listaAlunos:
            str += aluno.getNroMatric() + ' -- ' + aluno.getNome() + ' -- '+aluno.getCurso()+'\n'       
        self.limiteLista = LimiteMostraAlunos(str)
    
    def consultaAlunos(self, root):
        self.limiteConsulta = LimiteConsultaAluno(self, root)
    
    #Funções dos Buttons Janela de Inserção de Aluno -----------------------------------

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        aluno = self.getAluno(nroMatric)
        try:
            if aluno != None:
                raise AlunoDuplicado()
        except AlunoDuplicado:
            messagebox.showerror('Alerta', 'A matrícula desse aluno já existe')
        else:
            nome = self.limiteIns.inputNome.get()
            aluno = Aluno(nroMatric, nome)
            aluno.setCurso(self.limiteIns.inputCurso.get())
            self.listaAlunos.append(aluno)
            self.limiteIns.mostraMessagebox('Sucesso', 'Aluno cadastrado com sucesso')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCurso.delete(0, len(self.limiteIns.inputCurso.get()))

    def fechaHandler(self, event):
        self.limiteIns.janela.destroy()
    
    #Funções dos Buttons Janela de Consulta do Aluno ----------------------------------------------

    def consultaAluno(self, event):
        nroMatric = self.limiteConsulta.inputTextMatricula.get()
        aluno = self.getAluno(nroMatric)
        try:
            if aluno == None:
                raise AlunoNaoCadastrado()
        except AlunoNaoCadastrado:
            messagebox.showerror('Alerta', 'Aluno não cadastrado')
        else:
            str = 'Aluno cadastrado \nMatrícula -- Nome -- Curso \n'+aluno.getNroMatric()+' -- '+aluno.getNome()+' -- '+aluno.getCurso()
            LimiteMostraAlunos(str)
        finally:
            self.clearAluno(event)
    
    def clearAluno(self, event):
         self.limiteConsulta.inputTextMatricula.delete(0, len(self.limiteConsulta.inputTextMatricula.get()))
    
    def fechaAluno(self, event):
        self.limiteConsulta.janela.destroy()