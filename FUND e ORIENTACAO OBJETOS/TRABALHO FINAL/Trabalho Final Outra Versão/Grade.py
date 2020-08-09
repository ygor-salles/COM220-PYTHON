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

class Grade:
    def __init__(self, ano, listaDisc):
        self.__ano = ano
        self.__listaDisc = listaDisc
        self.__curso = None

    def getAno(self):
        return self.__ano

    def getListaDisc(self):
        return self.__listaDisc
    
    def setCurso(self, curso):
        self.__curso = curso
    
    def getCurso(self):
        return self.__curso
    
        
class LimiteInsereGrade():
    def __init__(self, controle, root, listaCodDisc):
        self.janela = tk.Toplevel()
        self.janela.geometry('300x250')
        self.janela.title('Insere Grade')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameAno = tk.Frame(self.janela)
        self.frameCurso = tk.Frame(self.janela)
        self.frameDisc = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameAno.pack()
        self.frameCurso.pack()
        self.frameDisc.pack()
        self.frameButton.pack()
        
        self.labelAno = tk.Label(self.frameAno, text='Ano da grade: ')
        self.labelCurso = tk.Label(self.frameCurso, text='Curso: ')
        self.labelDisc = tk.Label(self.frameDisc, text='Escolha as disciplinas: ')
        self.labelAno.pack(side='left')
        self.labelCurso.pack(side='left')
        self.labelDisc.pack(side='left')

        self.inputAno = tk.Entry(self.frameAno, width=4)
        self.inputAno.pack(side='left')
        self.inputCurso = tk.Entry(self.frameCurso, width=4)
        self.inputCurso.pack(side='left')
        
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
        self.janela.geometry('300x200')
        self.janela.title('Consulta Grade')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameAno = tk.Frame(self.janela)
        self.frameCurso = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameAno.pack()
        self.frameCurso.pack()
        self.frameButton.pack()

        self.labelAno = tk.Label(self.frameAno, text='Ano da grade: ')
        self.labelAno.pack(side='left')
        self.labelCurso = tk.Label(self.frameCurso, text='Curso da Grade')
        self.labelCurso.pack(side='left')

        self.inputAno = tk.Entry(self.frameAno, width=4)
        self.inputAno.pack(side='left')
        self.inputCurso = tk.Entry(self.frameCurso, width=3)
        self.inputCurso.pack(side='left')

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
            string += 'Ano '+grade.getAno()+'\nCurso '+grade.getCurso()+'\n'
            for disc in grade.getListaDisc():
                string += disc.getCodigo()+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
            string += '--------------------------\n'
        self.limiteMostra = LimiteMostra(string)

    def consultaGrade(self, root):
        self.limiteConsulta = LimiteConsultaGrade(self, root)
    
    #Funções Auxiliares e de amarrações da classe -------------------------------------------------------------
    
    def mostraConsultaGrade(self, ano, curso):
        string = 'Grade Cadastrada \n'
        for grade in self.listaGrade:
            if grade.getAno()==ano and grade.getCurso()==curso:
                string += '\nAno: '+grade.getAno()+'\nCurso: '+grade.getCurso()+'\n Listas de disciplinas da Grade: \n'
                for disc in grade.getListaDisc():
                    string += disc.getCodigo()+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
        self.limiteMostra = LimiteMostra(string)
    
    def verificaListaGrade(self, ano, curso):
        for grade in self.listaGrade:
            if grade.getAno()==ano and grade.getCurso()==curso:
                return True
        return False
    
    def getListaGradeCurso(self):
        listGradeCurso = []
        for grade in self.listaGrade:
            listGradeCurso.append(grade.getCurso())
        return listGradeCurso
    
    def getGrade(self, cursoGrade):
        gradeRet = None
        for grade in self.listaGrade:
            if grade.getCurso() == cursoGrade:
                gradeRet = grade
        return gradeRet
    
    def getListaGrade(self):
        return self.listaGrade

    #Funções dos Buttons Janela de Inserção de Grade -----------------------------------

    def insereHandler(self, event):
        ano = self.limiteIns.inputAno.get()
        curso = self.limiteIns.inputCurso.get()
        try:
            if self.verificaListaGrade(ano, curso) == True:
                raise GradeDuplicada()
        except GradeDuplicada:
            messagebox.showerror('Error', 'Grade já existe!')
        else:
            disciplinaSel = self.limiteIns.listbox.get(tk.ACTIVE)
            disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaSel)
            self.listaDiscGrade.append(disc)
            self.limiteIns.mostraMessagebox('Sucesso', 'Disciplina cadastrada com sucesso')
            self.limiteIns.listbox.delete(tk.ACTIVE)
    
    def criaHandler(self, event):
        ano = self.limiteIns.inputAno.get()
        curso = self.limiteIns.inputCurso.get()
        grade = Grade(ano, self.listaDiscGrade)
        grade.setCurso(curso)
        self.listaGrade.append(grade)
        self.limiteIns.mostraMessagebox('Sucesso', 'Grade criada com sucesso')
        self.limiteIns.janela.destroy()
    
    #Funções dos Buttons Janela de Consulta Grade -----------------------------------
    
    def consultaHandler(self, event):
        ano = self.limiteConsulta.inputAno.get()
        curso = self.limiteConsulta.inputCurso.get()
        try:
            if self.verificaListaGrade(ano, curso) == False:
                raise GradeNaoEncontrada()
        except GradeNaoEncontrada:
            messagebox.showerror('Error', 'Ano de Grade não encontrado')
        else:
            self.mostraConsultaGrade(ano, curso)
        finally:
            self.clearConsulta(event)
    
    def clearConsulta(self, event):
        self.limiteConsulta.inputAno.delete(0, len(self.limiteConsulta.inputAno.get()))
        self.limiteConsulta.inputCurso.delete(0, len(self.limiteConsulta.inputCurso.get()))

    def fechaConsulta(self, event):
        self.limiteConsulta.janela.destroy()