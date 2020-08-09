import tkinter as tk
from tkinter import messagebox

class DisciplinaNaoCadastrada(Exception):
    pass

class Disciplina:

    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome

    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome

class LimiteInsereDisciplinas():
    def __init__(self, controle, root):
        self.janela = tk.Toplevel()
        self.janela.geometry('250x100')
        self.janela.title('Insere Disciplina')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameNome = tk.Frame(self.janela)
        self.frameCodigo = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
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

class LimiteMostraDisciplinas():
    def __init__(self, str):
        messagebox.showinfo('Lista de disciplinas', str)

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
        self.listaDisciplinas = [
            Disciplina('COM220', 'Programação OO'),
            Disciplina('COM222', 'Programação Web'),
            Disciplina('COM111', 'Estruturas de Dados')
        ]

    def getListaDisciplinas(self):
        return self.listaDisciplinas

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

    def insereDisciplinas(self, root):
        self.limiteIns = LimiteInsereDisciplinas(self, root) 

    def mostraDisciplinas(self):
        str = 'Código -- Nome\n'
        for disc in self.listaDisciplinas:
            str += disc.getCodigo() + ' -- ' + disc.getNome() + '\n'
        self.limiteLista = LimiteMostraDisciplinas(str)
    
    def consultaDisciplinas(self, root):
        self.limiteConsulta = LimiteConsultaDisciplina(self, root)

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        disciplina = Disciplina(codigo, nome)
        self.listaDisciplinas.append(disciplina)
        self.limiteIns.mostraJanela('Sucesso', 'Disciplina cadastrada com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.janela.destroy()
    
    def consultaHandler(self, event):
        codigo = self.limiteConsulta.inputTextCodigo.get()
        try:
            encontrou=False
            for i in self.listaDisciplinas:
                if i.getCodigo() == codigo:
                    nomeDisc = i.getNome()
                    codigoDisc = i.getCodigo()
                    encontrou=True
            if encontrou==False:
               raise DisciplinaNaoCadastrada() 

        except DisciplinaNaoCadastrada:
            self.limiteConsulta.mostraMessagebox('Alerta', 'Disciplina não cadastrada')
        
        else:
            str = 'Disciplina cadastrada \nCódigo -- Nome \n'+codigoDisc+' -- '+nomeDisc
            LimiteMostraDisciplinas(str)
        finally:
            self.clearConsulta(event)
    
    def clearConsulta(self, event):
        self.limiteConsulta.inputTextCodigo.delete(0, len(self.limiteConsulta.inputTextCodigo.get()))
    
    def fechaConsulta(self, event):
        self.limiteConsulta.janela.destroy()