import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import estudante as est 
import disciplina as disc

class DisciplinaNaoCadastrada(Exception):
    pass

class SomenteUmaTurma(Exception):
    pass

class Turma:
    def __init__(self, codigo, disciplina, estudantes):
        self.__codigo = codigo
        self.__disciplina = disciplina
        self.__estudantes = estudantes

    def getCodigo(self):
        return self.__codigo
    
    def getDisciplina(self):
        return self.__disciplina

    def getEstudantes(self):
        return self.__estudantes


class LimiteInsereTurma():
    def __init__(self, controle, root, listaCodDiscip, listaNroMatric):
        self.janela=tk.Toplevel()
        self.janela.geometry('300x250')
        self.janela.title('Insere Turma')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameCodTurma = tk.Frame(self.janela)
        self.frameDiscip = tk.Frame(self.janela)
        self.frameEstudante = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameCodTurma.pack()
        self.frameDiscip.pack()
        self.frameEstudante.pack()
        self.frameButton.pack()        

        self.labelCodTurma = tk.Label(self.frameCodTurma,text="Informe o código da turma: ")
        self.labelCodTurma.pack(side="left")
        self.inputCodTurma = tk.Entry(self.frameCodTurma, width=20)
        self.inputCodTurma.pack(side="left")

        self.labelDiscip = tk.Label(self.frameDiscip,text="Escolha a disciplina: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameDiscip, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodDiscip
          
        self.labelEst = tk.Label(self.frameEstudante,text="Escolha o estudante: ")
        self.labelEst.pack(side="left") 
        self.listbox = tk.Listbox(self.frameEstudante)
        self.listbox.pack(side="left")
        for nro in listaNroMatric:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Aluno")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereAluno)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Turma")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaTurma)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraTurmas():
    def __init__(self, str):
        messagebox.showinfo('Lista de turmas', str)

class LimiteConsultaTurmas():
    def __init__(self, controle, root):
        self.janela=tk.Toplevel()
        self.janela.geometry('300x250')
        self.janela.title('Consulta Turmas')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()
    
        self.frameCodigo = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameCodigo.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text='Codigo da Disciplina: ')
        self.labelCodigo.pack(side='left')

        self.inputTextCodigo = tk.Entry(self.frameCodigo, width=30)
        self.inputTextCodigo.pack(side='left')

        self.buttonConsultar = tk.Button(self.frameButton, text='Realizar Consulta')
        self.buttonConsultar.pack(side='left')
        self.buttonConsultar.bind('<Button>', controle.consultaHandler)

        self.buttonClear = tk.Button(self.frameButton ,text='Clear')      
        self.buttonClear.pack(side='left')
        self.buttonClear.bind('<Button>', controle.clearTurma)  

        self.buttonFecha = tk.Button(self.frameButton ,text='Finalizar')      
        self.buttonFecha.pack(side='left')
        self.buttonFecha.bind('<Button>', controle.fechaTurma)
    
    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class CtrlTurma():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaTurmas = []
        self.listaAlunosTurma = []

        self.listaNroMatric = []

    def insereTurmas(self, root):        
        self.listaAlunosTurma = []
        listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.listaNroMatric = self.ctrlPrincipal.ctrlEstudante.getListaNroMatric()
        self.limiteIns = LimiteInsereTurma(self, root, listaCodDisc, self.listaNroMatric)

    def criaTurma(self, event):
        codTurma = self.limiteIns.inputCodTurma.get()
        discSel = self.limiteIns.escolhaCombo.get()
        disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(discSel)
        turma = Turma(codTurma, disc, self.listaAlunosTurma)
        self.listaTurmas.append(turma)
        self.limiteIns.mostraJanela('Sucesso', 'Turma criada com sucesso')
        self.limiteIns.janela.destroy()


    def insereAluno(self, event):
        alunoSel = self.limiteIns.listbox.get(tk.ACTIVE)
        aluno = self.ctrlPrincipal.ctrlEstudante.getEstudante(alunoSel)
        self.listaAlunosTurma.append(aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Aluno matriculado')
        self.limiteIns.listbox.delete(tk.ACTIVE)
        
    def mostraTurmas(self):
        str = ''
        for turma in self.listaTurmas:
            str += 'Código: ' + turma.getCodigo() + '\n'
            str += 'Disciplina: ' + turma.getDisciplina().getCodigo() + '\n'
            str += 'Estudantes:\n'
            for estud in turma.getEstudantes():
                str += estud.getNroMatric() + ' - ' + estud.getNome() + '\n'
            str += '------\n'

        self.limiteLista = LimiteMostraTurmas(str)
    
    def consultaTurmas(self, root):
        self.limiteConsulta = LimiteConsultaTurmas(self, root)
    
    def consultaHandler(self, event):
        codigo = self.limiteConsulta.inputTextCodigo.get()
        try:
            contador=0
            for i in self.listaTurmas:
                if i.getDisciplina().getCodigo() == codigo:
                    contador += 1
            if contador==0:
               raise DisciplinaNaoCadastrada()
    
        except DisciplinaNaoCadastrada:
            self.limiteConsulta.mostraMessagebox('Alerta', 'Disciplina não cadastrada em nenhuma turma')
        
        else:
            if contador>=2 :
                self.mostraTurmas()
            else:
                self.limiteConsulta.mostraMessagebox('Alerta', 'Disciplina {} já cadastrada em apenas uma turma'.format(codigo))
        
        finally:
            self.clearTurma(event)
    
    def clearTurma(self, event):
        self.limiteConsulta.inputTextCodigo.delete(0, len(self.limiteConsulta.inputTextCodigo.get()))

    def fechaTurma(self, event):
        self.limiteConsulta.janela.destroy()