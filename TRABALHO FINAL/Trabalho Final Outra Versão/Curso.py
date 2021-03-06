import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Aluno as al
import Grade as gr
import os.path
import pickle

class CursoNaoCadastrado(Exception):
    pass

class Curso:
    def __init__(self, nome, listaAlunos, grade):
        self.__nome = nome
        self.__listaAlunos = listaAlunos
        self.__grade = grade
    
    def getNome(self):
        return self.__nome

    def getListaAlunos(self):
        return self.__listaAlunos
    
    def getGrade(self):
        return self.__grade

class LimiteInsereCurso():
    def __init__(self, controle, root, listaGradeCurso, listaNroMatric):
        self.janela=tk.Toplevel()
        self.janela.geometry('300x250')
        self.janela.title('Insere Curso')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameNomeCurso = tk.Frame(self.janela)
        self.frameGrade = tk.Frame(self.janela)
        self.frameAluno = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameNomeCurso.pack()
        self.frameGrade.pack()
        self.frameAluno.pack()
        self.frameButton.pack()       

        self.labelNomeCurso = tk.Label(self.frameNomeCurso,text="Nome do curso: ")
        self.labelNomeCurso.pack(side="left")
        self.inputNomeCurso = tk.Entry(self.frameNomeCurso, width=4)
        self.inputNomeCurso.pack(side="left")

        self.labelGrade = tk.Label(self.frameGrade,text="Escolha a grade: ")
        self.labelGrade.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameGrade, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaGradeCurso
          
        self.labelAluno = tk.Label(self.frameAluno,text="Escolha o aluno: ")
        self.labelAluno.pack(side="left") 
        self.listbox = tk.Listbox(self.frameAluno)
        self.listbox.pack(side="left")
        for nro in listaNroMatric:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere aluno")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereAluno)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Curso")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaCurso)    

    def mostraMessagebox(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraCursos():
    def __init__(self, str):
        messagebox.showinfo('Lista de Cursos', str)

class LimiteConsultaCursos():
    def __init__(self, controle, root):
        self.janela=tk.Toplevel()
        self.janela.geometry('400x200')
        self.janela.title('Consulta Cursos')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()
    
        self.frameNome = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text='Nome do curso: ')
        self.labelNome.pack(side='left')

        self.inputTextNome = tk.Entry(self.frameNome, width=4)
        self.inputTextNome.pack(side='left')

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

class CtrlCurso():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlunosCurso = []
        self.listaNroMatric = []

        if not os.path.isfile("Curso.pickle"):
            self.listaCursos =  []
        else:
            with open("Curso.pickle", "rb") as f:
                self.listaCursos = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaCursos(self):
        if len(self.listaCursos) != 0:
            with open("Curso.pickle","wb") as f:
                pickle.dump(self.listaCursos, f)

    # Funções instancioadores, recebe da main ---------------------------

    def insereCursos(self, root):
        self.listaAlunosCurso = []
        listaGradeCurso = self.ctrlPrincipal.ctrlGrade.getListaGradeCurso()
        self.listaNroMatric = self.ctrlPrincipal.ctrlAluno.getListaNroMatric()
        self.limiteIns = LimiteInsereCurso(self, root, listaGradeCurso, self.listaNroMatric)

    def mostraCursos(self):
        string = ''
        for curso in self.listaCursos:
            string += 'Nome do Curso: '+curso.getNome()+'\n'
            string += 'Grade: '+curso.getGrade().getCurso()+' -- '+curso.getGrade().getAno()+'\n'
            string += 'Listagem de alunos matriculados: \n'
            for aluno in curso.getListaAlunos():
                string += aluno.getNroMatric() + ' - ' + aluno.getNome() + '\n'
            string += '------------------------------------------------\n'
        self.limiteMostra = LimiteMostraCursos(string)
    
    def consultaCursos(self, root):
        self.limiteConsulta = LimiteConsultaCursos(self, root)
    
    
    #Funções de Buttons da Tela Insere Curso ------------------------------------------------------------
    
    def insereAluno(self, event):
        alunoSelecionado = self.limiteIns.listbox.get(tk.ACTIVE)
        aluno = self.ctrlPrincipal.ctrlAluno.getAluno(alunoSelecionado)
        self.listaAlunosCurso.append(aluno)
        self.limiteIns.mostraMessagebox('Sucesso', 'Aluno Matriculado no Curso')
        self.limiteIns.listbox.delete(tk.ACTIVE)

    def criaCurso(self, event):
        nomeCurso = self.limiteIns.inputNomeCurso.get()
        gradeSelecionada = self.limiteIns.escolhaCombo.get()
        grade = self.ctrlPrincipal.ctrlGrade.getGrade(gradeSelecionada)
        curso = Curso(nomeCurso, self.listaAlunosCurso, grade)
        self.listaCursos.append(curso)
        self.limiteIns.mostraMessagebox('Sucesso', 'Alunos matriculados no curso {} com sucesso'.format(nomeCurso))
        self.limiteIns.janela.destroy()     

    # Funções do Buttons de consulta do Curso -------------------------------------------------------

    def consultaHandler(self, event):
        nome = self.limiteConsulta.inputTextNome.get()
        encontrou=False
        try:    
            string = ''
            for curso in self.listaCursos:
                if nome == curso.getNome():
                    encontrou=True
                    string += 'Nome: '+curso.getNome()+'\n'
                    string += 'Grade: '+curso.getGrade().getCurso()+' -- '+curso.getGrade().getAno()+'\n'
                    string += 'Listagem de alunos matriculados: \n'
                    for aluno in curso.getListaAlunos():
                        string += aluno.getNroMatric() + ' - ' + aluno.getNome() + '\n'
                    break
            if encontrou==False:
                raise CursoNaoCadastrado()
        except CursoNaoCadastrado:
            messagebox.showerror('Error', 'Curso não cadastrado!')
        else:
            LimiteMostraCursos(string)
        finally:
            self.clearConsulta(event)
    
    def clearConsulta(self, event):
        self.limiteConsulta.inputTextNome.delete(0, len(self.limiteConsulta.inputTextNome.get()))

    def fechaConsulta(self, event):
        self.limiteConsulta.janela.destroy()

    