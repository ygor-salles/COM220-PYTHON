import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import Aluno as al
import Disciplina as dic
import Grade as gr
import os.path
import pickle

class MatriculaNaoEncontrada(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass

class Historico:
    def __init__(self, listaDisc, aluno):
        self.__listaDisc = listaDisc
        self.__aluno = aluno
        self.__semestre = None
        self.__ano = None
        self.__notaDisc = []
        
    def getListaDisc(self):
        return self.__listaDisc

    def getAluno(self):
        return self.__aluno
    
    def getSemestre(self):
        return self.__semestre
    
    def setSemestre(self, semestre):
        self.__semestre = semestre
    
    def getAno(self):
        return self.__ano
    
    def setAno(self, ano):
        self.__ano = ano
    
    def getNotaDisc(self):
        return self.__notaDisc

    def setNotaDisc(self, notaDisc):
        self.__notaDisc = notaDisc

class LimiteInsereHistorico():
    def __init__(self, controle, root, listaDisc, listaMatricAluno):
        self.janela = tk.Toplevel()
        self.janela.geometry('400x350')
        self.janela.title('Insere Histórico')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameAluno = tk.Frame(self.janela)
        self.frameSemestre = tk.Frame(self.janela)
        self.frameAno = tk.Frame(self.janela)
        self.frameListaDisc = tk.Frame(self.janela)
        self.frameNota = tk.Frame(self.janela)
        self.frameAluno.pack()
        self.frameSemestre.pack()
        self.frameAno.pack()
        self.frameListaDisc.pack()
        self.frameNota.pack()
        
        self.labelAluno = tk.Label(self.frameAluno, text='Nro Matricula do Aluno: ')
        self.labelAluno.pack(side='left')
        self.labelSemestre = tk.Label(self.frameSemestre, text='Informe Semestre: ')
        self.labelSemestre.pack(side='left')
        self.labelAno = tk.Label(self.frameAno, text='Informe o ano: ')
        self.labelAno.pack(side='left')
        self.labelListaDisc = tk.Label(self.frameListaDisc, text='Selecione as disciplinas \nque o aluno cursou no semestre: ')
        self.labelListaDisc.pack(side='left')
        self.labelNota = tk.Label(self.frameNota, text='Nota do Aluno na Disciplina: ')
        self.labelNota.pack(side='left')

        self.comboAluno = tk.StringVar()
        self.comboboxAluno = ttk.Combobox(self.frameAluno, width=15, textvariable=self.comboAluno)
        self.comboboxAluno.pack(side='left')
        self.comboboxAluno['values'] = listaMatricAluno

        self.comboSemestre = ttk.Combobox(self.frameSemestre, values=['1', '2'])
        self.comboSemestre.pack(side='left')

        self.inputAno = tk.Entry(self.frameAno, width=4)
        self.inputAno.pack(side='left')
        
        self.listboxDisciplina = tk.Listbox(self.frameListaDisc)
        self.listboxDisciplina.pack(side='left')
        for disc in listaDisc:
            self.listboxDisciplina.insert(tk.END, disc)

        self.inputNota = tk.Entry(self.frameNota, width=4)
        self.inputNota.pack(side='left')

        self.buttonCria = tk.Button(self.janela, text='Criar Semestre')
        self.buttonCria.pack(side='right')
        self.buttonCria.bind('<Button>', controle.criaSemestre)

        self.buttonInsere = tk.Button(self.janela, text='Insere Disciplina no Histórico')
        self.buttonInsere.pack(side='right')
        self.buttonInsere.bind('<Button>', controle.insereDisciplina)

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteMostraHistorico():
    def __init__(self, string):
        messagebox.showinfo('Lista de Historicos', string)

class LimiteConsultaHistorico():
    def __init__(self, controle, root):
        self.janela = tk.Toplevel()
        self.janela.geometry('250x100')
        self.janela.title('Insere Histórico')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameAluno = tk.Frame(self.janela)
        self.frameButton = tk.Frame(self.janela)
        self.frameAluno.pack()
        self.frameButton.pack()

        self.labelMatricAluno = tk.Label(self.frameAluno, text='Matricula do Aluno: ')
        self.labelMatricAluno.pack(side='left')

        self.inputMatricAluno = tk.Entry(self.frameAluno, width=15)
        self.inputMatricAluno.pack(side='left')

        self.buttonConsulta = tk.Button(self.frameButton, text='Enter')
        self.buttonConsulta.pack(side='left')
        self.buttonConsulta.bind('<Button>', controle.enterConsulta)

        self.buttonClear = tk.Button(self.frameButton, text='Clear')
        self.buttonClear.pack(side='left')
        self.buttonClear.bind('<Button>', controle.clearConsulta)

        self.buttonFinaliza = tk.Button(self.frameButton, text='Finalizar')
        self.buttonFinaliza.pack(side='left')
        self.buttonFinaliza.bind('<Button>', controle.finalizaConsulta)


class CtrlHistorico():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDisc = []
        self.listaCodDisc = []
        self.notaDisc = []

        if not os.path.isfile("Historico.pickle"):
            self.listaHistoricos =  []
        else:
            with open("Historico.pickle", "rb") as f:
                self.listaHistoricos = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaHistoricos(self):
        if len(self.listaHistoricos) != 0:
            with open("Historico.pickle","wb") as f:
                pickle.dump(self.listaHistoricos, f)

    # Funções instanciadoras, recebe da main ---------------------------------------
    
    def insereHistoricos(self, root):
        self.listaDisc = []
        self.notaDisc = []
        self.listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        listaMatricAluno = self.ctrlPrincipal.ctrlAluno.getListaNroMatric()
        self.limiteIns = LimiteInsereHistorico(self, root, self.listaCodDisc, listaMatricAluno)

    def mostraHistoricos(self):
        string = '..................RELATÓRIO DE HISTÓRICOS DOS ALUNOS..................'
        for his in self.listaHistoricos:
            string = self.emitirHistorico(his, string)
        self.limiteMostra = LimiteMostraHistorico(string)

    def consultaHistoricos(self, root):
        self.limiteConsulta = LimiteConsultaHistorico(self, root)

    #Funções auxiliares ------------------------------------------------------------

    def emitirHistorico(self, his, string):
        eletiva=0
        obrigatoria=0
        total=0
        string += '\nMatrícula: '+str(his.getAluno().getNroMatric())
        string += '\nNome: '+his.getAluno().getNome()
        string += '\n\n|Ano|Semestre|Cod. Disciplina|Nome Disciplina|CH|Nota|Status|\n'
        encontrou=False
        grade=''
        for hisDisc, nota in his.getNotaDisc():
            if nota >= 6:
                string += '{} - {} - {} - {} - {} - {} - Aprovado\n'.format(his.getAno(), his.getSemestre(), hisDisc.getCodigo(), \
                    hisDisc.getNome(), hisDisc.getCargaHoraria(), nota)
            else:
                string += '{} - {} - {} - {} - {} - {} - Reprovado\n'.format(his.getAno(), his.getSemestre(), hisDisc.getCodigo(), \
                    hisDisc.getNome(), hisDisc.getCargaHoraria(), nota)
            total += int(hisDisc.getCargaHoraria())
            
            for curso in self.ctrlPrincipal.ctrlCurso.listaCursos:
                for aluno in curso.getListaAlunos():
                    if aluno.getNroMatric() == his.getAluno().getNroMatric():
                        grade=curso.getGrade().getAnoCurso()
                        nroMatric = aluno.getNroMatric()
                        for disc in curso.getGrade().getListaDisc():
                            if disc.getCodigo() == hisDisc.getCodigo() and his.getAluno().getNroMatric() == nroMatric:
                                obrigatoria += int(hisDisc.getCargaHoraria())
                        
        eletiva = int(total-obrigatoria)    
        string += '\nGrade: '+str(grade)
        string += '\nTotal Carga Horária obrigatória: {} \nTotal Carga Horária eletiva: {}\n'.format(obrigatoria, eletiva)
        string += '----------------------------------------------------------------------\n'
        return string
    
    #Função dos Buttons de Inserção de Histórico ----------------------------------------

    def insereDisciplina(self, event):
        nroMatric = self.limiteIns.comboAluno.get()
        semestre = self.limiteIns.comboSemestre.get()
        ano = self.limiteIns.inputAno.get()
        nota = self.limiteIns.inputNota.get()
        disciplinaSelecionada = self.limiteIns.listboxDisciplina.get(tk.ACTIVE)
        try:
            if len(nroMatric)==0 or len(semestre)==0 or len(ano)==0 or len(nota)==0 or len(disciplinaSelecionada)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        else:
            nota=float(nota)
            disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaSelecionada)
            self.listaDisc.append(disciplina)
            self.notaDisc.append((disciplina, nota))
            self.limiteIns.mostraMessagebox('Sucesso', 'Disciplina e nota inserida no histórico com sucesso!')
            self.limiteIns.listboxDisciplina.delete(tk.ACTIVE)
            self.limiteIns.inputNota.delete(0, len(self.limiteIns.inputNota.get()))
    
    def criaSemestre(self, event):
        alunoSelecionado = self.limiteIns.comboAluno.get()
        aluno = self.ctrlPrincipal.ctrlAluno.getAluno(alunoSelecionado)
        semestre = self.limiteIns.comboSemestre.get()
        ano = self.limiteIns.inputAno.get()
        historico = Historico(self.listaDisc, aluno)
        historico.setSemestre(semestre)
        historico.setAno(ano)
        historico.setNotaDisc(self.notaDisc)
        self.listaHistoricos.append(historico)
        self.limiteIns.mostraMessagebox('Sucesso', 'Semestre criado no histórico do Aluno com sucesso!')
        self.limiteIns.janela.destroy()

    # Funções dos Buttons de Consulta ------------------------------------------------------------------------

    def enterConsulta(self, event):
        matricAluno = self.limiteConsulta.inputMatricAluno.get()
        encontrou=False
        try:
            if len(matricAluno)==0:
                raise CamposNaoPreenchidos()
            string= '..................RELATÓRIO DE HISTÓRICO DO ALUNO..................'
            for hist in self.listaHistoricos:
                if matricAluno == hist.getAluno().getNroMatric():
                    encontrou=True
                    string = self.emitirHistorico(hist, string)
            if encontrou==False:
                raise MatriculaNaoEncontrada()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except MatriculaNaoEncontrada:
            messagebox.showerror('Error', 'Nenhum histórico foi cadastrado para essa matrícula!')
        else:
            LimiteMostraHistorico(string)
        finally:
            self.clearConsulta(event)
    
    def clearConsulta(self, event):
        self.limiteConsulta.inputMatricAluno.delete(0, len(self.limiteConsulta.inputMatricAluno.get()))
    
    def finalizaConsulta(self, event):
        self.limiteConsulta.janela.destroy()