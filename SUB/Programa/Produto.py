import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class ProdutoDuplicado(Exception):
    pass

class CampoPreenchimentoVazio(Exception):
    pass

class ProdutoInexistente(Exception):
    pass

class Produto:
    def __init__(self, codigo, descricao, valorUnitario):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUnitario = valorUnitario
    
    def getCodigo(self):
        return self.__codigo
    
    def getDescricao(self):
        return self.__descricao
    
    def getValorUnitario(self):
        return self.__valorUnitario
    
class LimiteInsereProduto:
    def __init__(self, controle, root):
        self.janela = tk.Toplevel()
        self.janela.geometry('350x200')
        self.janela.title('Cadastramento de Produto')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameCodigo = tk.Frame(self.janela)
        self.frameDescricao = tk.Frame(self.janela)
        self.frameValor = tk.Frame(self.janela)    
        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.frameValor.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text='Codigo: ')
        self.labelDescricao = tk.Label(self.frameDescricao, text='Descrição: ')
        self.labelValor = tk.Label(self.frameValor, text='Valor: ')
        self.labelCodigo.pack(side='left')
        self.labelDescricao.pack(side='left')
        self.labelValor.pack(side='left')

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputDescricao = tk.Entry(self.frameDescricao, width=50)
        self.inputValor = tk.Entry(self.frameValor, width=10)
        self.inputCodigo.pack(side='left')
        self.inputDescricao.pack(side='left')
        self.inputValor.pack(side='left')

        self.buttonCadastro = tk.Button(self.janela, text='Cadastrar')
        self.buttonCadastro.pack(side='left')
        self.buttonCadastro.bind('<Button>', controle.cadastrarHandler)

        self.buttonClear = tk.Button(self.janela, text='Clear')
        self.buttonClear.pack(side='left')
        self.buttonClear.bind('<Button>', controle.clearHandler)

        self.buttonFinaliza = tk.Button(self.janela, text='Finalizar')
        self.buttonFinaliza.pack(side='left')
        self.buttonFinaliza.bind('<Button>', controle.finalizarHandler)

    def mostraMessagebox(self, titulo, mensagem, identificador):
        if identificador == True:
            messagebox.showinfo(titulo, mensagem)
        else:
            messagebox.showerror(titulo, mensagem)

class LimiteConsultaProduto:
    def __init__(self, controle, root):
        self.janela = tk.Toplevel()
        self.janela.geometry('250x100')
        self.janela.title('Consulta de Produto')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameCodigo = tk.Frame(self.janela)
        self.frameCodigo.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text='Codigo')
        self.labelCodigo.pack(side='left')

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side='left')

        self.buttonConsulta = tk.Button(self.janela, text='Consultar')
        self.buttonConsulta.pack(side='left')
        self.buttonConsulta.bind('<Button>', controle.consultar)

        self.buttonClear = tk.Button(self.janela, text='Clear')
        self.buttonClear.pack(side='left')
        self.buttonClear.bind('<Button>', controle.clearConsulta)

        self.buttonFinaliza = tk.Button(self.janela, text='Finalizar')
        self.buttonFinaliza.pack(side='left')
        self.buttonFinaliza.bind('<Button>', controle.finalizarConsulta)

    def mostraMessagebox(self, titulo, mensagem, identificador):
        if identificador == True:
            messagebox.showinfo(titulo, mensagem)
        else:
            messagebox.showerror(titulo, mensagem)

class CtrlProduto:
    def __init__(self):
        if not os.path.isfile("Produto.pickle"):
            self.listaProdutos =  []
        else:
            with open("Produto.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaProdutos(self):
        if len(self.listaProdutos) != 0:
            with open("Produto.pickle","wb") as f:
                pickle.dump(self.listaProdutos, f)
    
    #Funções de instanciação --------------------------------------------------------

    def insereProdutos(self, root):
        self.limiteInsere = LimiteInsereProduto(self, root)

    def consultaProdutos(self, root):
        self.limiteConsulta = LimiteConsultaProduto(self, root)

    #Funções auxiliares --------------------------------------------------------------

    def getProduto(self, codigo):
        for produto in self.listaProdutos:
            if produto.getCodigo() == codigo:
                return produto
        return None

    #Funções dos Buttons da janela Insere --------------------------------------------

    def cadastrarHandler(self, event):
        codigo = self.limiteInsere.inputCodigo.get()
        descricao = self.limiteInsere.inputDescricao.get()
        valorUnitario = self.limiteInsere.inputValor.get()
        try:
            if len(codigo)==0 or len(descricao)==0 or len(valorUnitario)==0:
                raise CampoPreenchimentoVazio()
            if self.getProduto(codigo) != None:
                raise ProdutoDuplicado()
        except ProdutoDuplicado:
            self.limiteInsere.mostraMessagebox('Error', 'Produto {} já existe!'.format(codigo), False)
            self.clearHandler(event)
        except CampoPreenchimentoVazio:
            self.limiteInsere.mostraMessagebox('Error', 'Todos os campos devem ser preenchidos', False)
        else:
            produto = Produto(codigo, descricao, valorUnitario)
            self.listaProdutos.append(produto)
            self.limiteInsere.mostraMessagebox('Sucesso', 'Produto {} cadastrado com sucesso'.format(codigo), True)
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteInsere.inputCodigo.delete(0, len(self.limiteInsere.inputCodigo.get()))
        self.limiteInsere.inputDescricao.delete(0, len(self.limiteInsere.inputDescricao.get()))
        self.limiteInsere.inputValor.delete(0, len(self.limiteInsere.inputValor.get()))
    
    def finalizarHandler(self, event):
        self.limiteInsere.janela.destroy()

    #Funções dos Buttons da janela Consulta ---------------------------------------------------------

    def consultar(self, event):
        codigo = self.limiteConsulta.inputCodigo.get()
        produto = self.getProduto(codigo)
        try:
            if len(codigo)==0:
                raise CampoPreenchimentoVazio()
            if produto == None:
                raise ProdutoInexistente()
        except CampoPreenchimentoVazio:
            self.limiteConsulta.mostraMessagebox('Consulta', 'Todos os campos devem ser preenchidos', False)
        except ProdutoInexistente:
            self.limiteConsulta.mostraMessagebox('Consulta', 'Produto {} não existe!'.format(codigo), False)
        else:
            self.limiteConsulta.mostraMessagebox('Consulta', 'PRODUTO ENCONTRADO\n\nCodigo: {} \nDescrição: {} \
                \nValor Unitário: R$ {}\n'.format(produto.getCodigo(), produto.getDescricao(), produto.getValorUnitario()), True)
        finally:
            self.clearConsulta(event)
        
    def clearConsulta(self, event):
        self.limiteConsulta.inputCodigo.delete(0, len(self.limiteConsulta.inputCodigo.get()))

    def finalizarConsulta(self, event):
        self.limiteConsulta.janela.destroy()
