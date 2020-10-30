import tkinter as tk
from tkinter import messagebox
import Disciplina as dic
import Curso as cr
import os.path
import pickle

class GradeDuplicada(Exception):
    pass

class GradeNaoEncontrada(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass

class Grade:
    def __init__(self, anoCurso, listaDisc):
        self.__anoCurso = anoCurso
        self.__listaDisc = listaDisc

    def getAnoCurso(self):
        return self.__anoCurso

    def getListaDisc(self):
        return self.__listaDisc
    
        
class LimiteInsereGrade():
    def __init__(self, controle, root, listaCodDisc):
        self.janela = tk.Toplevel()
        self.janela.geometry('300x250')
        self.janela.title('Insere Grade')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameAnoCurso = tk.Frame(self.janela)
        self.frameDisc = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameAnoCurso.pack()
        self.frameDisc.pack()
        self.frameButton.pack()
        
        self.labelAnoCurso = tk.Label(self.frameAnoCurso, text='Ano/Curso: ')
        self.labelDisc = tk.Label(self.frameDisc, text='Escolha as disciplinas: ')
        self.labelAnoCurso.pack(side='left')
        self.labelDisc.pack(side='left')

        self.inputAnoCurso = tk.Entry(self.frameAnoCurso, width=20)
        self.inputAnoCurso.pack(side='left')
        
        self.listbox = tk.Listbox(self.frameDisc)
        self.listbox.pack(side='left')
        for disc in listaCodDisc:
            self.listbox.insert(tk.END, disc)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Disciplina")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereHandler)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Grade")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaHandler)

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteMostra():
    def __init__(self, string):
        messagebox.showinfo('Lista de Grades', string) 

class LimiteConsultaGrade():
    def __init__(self, controle, root):
        self.janela=tk.Toplevel()
        self.janela.geometry('250x100')
        self.janela.title('Consulta Grade')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameAnoCurso = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameAnoCurso.pack()
        self.frameButton.pack()

        self.labelAnoCurso = tk.Label(self.frameAnoCurso, text='Ano/Curso: ')
        self.labelAnoCurso.pack(side='left')

        self.inputAnoCurso = tk.Entry(self.frameAnoCurso, width=20)
        self.inputAnoCurso.pack(side='left')

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

class CtrlGrade():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDiscGrade = []
        self.listaCodDisc = []
        
        if not os.path.isfile("Grade.pickle"):
            self.listaGrade =  []
        else:
            with open("Grade.pickle", "rb") as f:
                self.listaGrade = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaGrades(self):
        if len(self.listaGrade) != 0:
            with open("Grade.pickle","wb") as f:
                pickle.dump(self.listaGrade, f)
    
    #Funções que serão chamadas na Main --- Instaciadores ---------------------------

    def insereGrade(self, root):        
        self.listaDiscGrade = []
        self.listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.limiteIns = LimiteInsereGrade(self, root, self.listaCodDisc)
    
    def mostraGrade(self):
        string=''
        for grade in self.listaGrade:
            string += '\nGrade: '+grade.getAnoCurso()+'\n'
            for disc in grade.getListaDisc():
                string += disc.getCodigo()+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
            string += '--------------------------\n'
        self.limiteMostra = LimiteMostra(string)

    def consultaGrade(self, root):
        self.limiteConsulta = LimiteConsultaGrade(self, root)
    
    #Funções Auxiliares e de amarrações da classe -------------------------------------------------------------
    
    def mostraConsultaGrade(self, anoCurso):
        string = 'Grade Cadastrada \n'
        for grade in self.listaGrade:
            if grade.getAnoCurso()==anoCurso:
                string += '\nGrade: '+grade.getAnoCurso()+'\n Listas de disciplinas da Grade: \n'
                for disc in grade.getListaDisc():
                    string += disc.getCodigo()+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
        self.limiteMostra = LimiteMostra(string)
    
    def verificaListaGrade(self, AnoCurso):
        for grade in self.listaGrade:
            if grade.getAnoCurso()==AnoCurso:
                return True
        return False
    
    def getListaGradeAnoCurso(self):
        listGradeAnoCurso = []
        for grade in self.listaGrade:
            listGradeAnoCurso.append(grade.getAnoCurso())
        return listGradeAnoCurso
    
    def getGrade(self, AnoCursoGrade):
        gradeRet = None
        for grade in self.listaGrade:
            if grade.getAnoCurso() == AnoCursoGrade:
                gradeRet = grade
        return gradeRet
    
    def getListaGrade(self):
        return self.listaGrade

    #Funções dos Buttons Janela de Inserção de Grade -----------------------------------

    def insereHandler(self, event):
        anoCurso = self.limiteIns.inputAnoCurso.get()
        disciplinaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaSel)
        try:
            if self.verificaListaGrade(anoCurso) == True:
                raise GradeDuplicada()
            if len(anoCurso)==0 or disc==None:
                raise CamposNaoPreenchidos()
        except GradeDuplicada:
            messagebox.showerror('Error', 'Grade já existe!')
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        else:
            self.listaDiscGrade.append(disc)
            self.limiteIns.mostraMessagebox('Sucesso', 'Disciplina cadastrada com sucesso')
            self.limiteIns.listbox.delete(tk.ACTIVE)
    
    def criaHandler(self, event):
        anoCurso = self.limiteIns.inputAnoCurso.get()
        grade = Grade(anoCurso, self.listaDiscGrade)
        self.listaGrade.append(grade)
        self.limiteIns.mostraMessagebox('Sucesso', 'Grade criada com sucesso')
        self.limiteIns.janela.destroy()
    
    #Funções dos Buttons Janela de Consulta Grade -----------------------------------
    
    def consultaHandler(self, event):
        anoCurso = self.limiteConsulta.inputAnoCurso.get()
        try:
            if len(anoCurso)==0:
                raise CamposNaoPreenchidos()
            if self.verificaListaGrade(anoCurso) == False:
                raise GradeNaoEncontrada()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except GradeNaoEncontrada:
            messagebox.showerror('Error', 'Ano de Grade não encontrado')
        else:
            self.mostraConsultaGrade(anoCurso)
        finally:
            self.clearConsulta(event)
    
    def clearConsulta(self, event):
        self.limiteConsulta.inputAnoCurso.delete(0, len(self.limiteConsulta.inputAnoCurso.get()))

    def fechaConsulta(self, event):
        self.limiteConsulta.janela.destroy()