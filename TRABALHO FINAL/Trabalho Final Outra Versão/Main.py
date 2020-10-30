import tkinter as tk
import Aluno as al 
import Curso as cr 
import Grade as gr 
import Disciplina as dic 
import Historico as hist
from tkinter import messagebox 

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('600x450')
        self.menubar = tk.Menu(self.root)        
        self.alunoMenu = tk.Menu(self.menubar)
        self.discipMenu = tk.Menu(self.menubar)
        self.gradeMenu = tk.Menu(self.menubar)
        self.cursoMenu = tk.Menu(self.menubar)
        self.historicoMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar) 
             
        self.alunoMenu.add_command(label="Insere", command=self.controle.insereAlunos)
        self.alunoMenu.add_command(label="Mostra", command=self.controle.mostraAlunos)
        self.alunoMenu.add_command(label="Consulta", command=self.controle.consultaAlunos)
        self.menubar.add_cascade(label="Aluno", menu=self.alunoMenu)

        self.discipMenu.add_command(label="Insere", command=self.controle.insereDisciplinas)
        self.discipMenu.add_command(label="Mostra", command=self.controle.mostraDisciplinas)
        self.discipMenu.add_command(label="Consulta", command=self.controle.consultaDisciplinas)        
        self.menubar.add_cascade(label="Disciplina", menu=self.discipMenu)

        self.gradeMenu.add_command(label="Insere", command=self.controle.insereGrade)
        self.gradeMenu.add_command(label="Mostra", command=self.controle.mostraGrade)
        self.gradeMenu.add_command(label="Consulta", command=self.controle.consultaGrade)        
        self.menubar.add_cascade(label="Grade", menu=self.gradeMenu)

        self.cursoMenu.add_command(label="Insere", command=self.controle.insereCursos)
        self.cursoMenu.add_command(label="Mostra", command=self.controle.mostraCursos)
        self.cursoMenu.add_command(label="Consulta", command=self.controle.consultaCursos)        
        self.menubar.add_cascade(label="Curso", menu=self.cursoMenu)

        self.historicoMenu.add_command(label="Insere", command=self.controle.insereHistoricos)
        self.historicoMenu.add_command(label="Mostra", command=self.controle.mostraHistoricos)
        self.historicoMenu.add_command(label="Consulta", command=self.controle.consultaHistoricos)        
        self.menubar.add_cascade(label="Histórico", menu=self.historicoMenu)

        self.sairMenu.add_command(label="Salva", command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", menu=self.sairMenu)

        self.root.config(menu=self.menubar)
      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlAluno = al.CtrlAluno()
        self.ctrlDisciplina = dic.CtrlDisciplina()
        self.ctrlGrade = gr.CtrlGrade(self)
        self.ctrlCurso = cr.CtrlCurso(self)
        self.ctrlHistorico = hist.CtrlHistorico(self)
    
        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Sistema Acadêmico YS")
        self.root.mainloop()

    ###############################################   
    def insereAlunos(self):
        self.ctrlAluno.insereAlunos(self.root)

    def mostraAlunos(self):
        self.ctrlAluno.mostraAlunos()
    
    def consultaAlunos(self):
        self.ctrlAluno.consultaAlunos(self.root)

    ###############################################
    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas(self.root)

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()

    def consultaDisciplinas(self):
        self.ctrlDisciplina.consultaDisciplinas(self.root)

    ###############################################
    def insereGrade(self):
        self.ctrlGrade.insereGrade(self.root)

    def mostraGrade(self):
        self.ctrlGrade.mostraGrade()
    
    def consultaGrade(self):
        self.ctrlGrade.consultaGrade(self.root)

    ###############################################
    def insereCursos(self):
        self.ctrlCurso.insereCursos(self.root)

    def mostraCursos(self):
        self.ctrlCurso.mostraCursos()
    
    def consultaCursos(self):
        self.ctrlCurso.consultaCursos(self.root)
    
    ###############################################
    def insereHistoricos(self):
        self.ctrlHistorico.insereHistoricos(self.root)

    def mostraHistoricos(self):
        self.ctrlHistorico.mostraHistoricos()
    
    def consultaHistoricos(self):
        self.ctrlHistorico.consultaHistoricos(self.root)

    ###############################################
    def salvaDados(self):
        self.ctrlAluno.salvaAlunos()
        self.ctrlDisciplina.salvaDisciplinas()
        self.ctrlGrade.salvaGrades()
        self.ctrlCurso.salvaCursos()
        self.ctrlHistorico.salvaHistoricos()
        messagebox.showinfo('Backup', 'Arquivos salvos com sucesso!')
        self.root.destroy()
    
if __name__ == '__main__':
    c = ControlePrincipal()