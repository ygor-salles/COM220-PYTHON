import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
import Produto as prod

class NotaFiscalDuplicada(Exception):
    pass

class CampoPreenchimentoVazio(Exception):
    pass

class NotaFiscalInexistente(Exception):
    pass

class NotaFiscal:
    def __init__(self, numeroNF, nomeCliente, itensNota):
        self.__numeroNF = numeroNF
        self.__nomeCliente = nomeCliente
        self.__itensNota = itensNota
    
    def getNumeroNF(self):
        return self.__numeroNF
    
    def getnomeCliente(self):
        return self.__nomeCliente
    
    def getItensNota(self):
        return self.__itensNota

class LimiteInsereNF:
    def __init__(self, controle, root, listaCodProdutos):
        self.janela = tk.Toplevel()
        self.janela.geometry('400x300')
        self.janela.title('Cadastramento de Nota Fiscal')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameNumeroNF = tk.Frame(self.janela)
        self.frameNomeCliente = tk.Frame(self.janela)
        self.frameItensNota = tk.Frame(self.janela)    
        self.frameNumeroNF.pack()
        self.frameNomeCliente.pack()
        self.frameItensNota.pack()

        self.labelNumeroNF = tk.Label(self.frameNumeroNF, text='Numero NF: ')
        self.labelNomeCliente = tk.Label(self.frameNomeCliente, text='Cliente: ')
        self.labelItensNota = tk.Label(self.frameItensNota, text='Itens Nota: ')
        self.labelNumeroNF.pack(side='left')
        self.labelNomeCliente.pack(side='left')
        self.labelItensNota.pack(side='left')

        self.inputNumeroNF = tk.Entry(self.frameNumeroNF, width=20)
        self.inputNomeCliente = tk.Entry(self.frameNomeCliente, width=50)
        self.inputNumeroNF.pack(side='left')
        self.inputNomeCliente.pack(side='left')

        self.listboxItem = tk.Listbox(self.frameItensNota)
        self.listboxItem.pack(side='left')
        for produto in listaCodProdutos:
            self.listboxItem.insert(tk.END, produto.getCodigo())

        self.buttonConcluir = tk.Button(self.janela, text='Concluir')
        self.buttonConcluir.pack(side='right')
        self.buttonConcluir.bind('<Button>', controle.concluirCompra)

        self.buttonCadastro = tk.Button(self.janela, text='Cadastrar')
        self.buttonCadastro.pack(side='right')
        self.buttonCadastro.bind('<Button>', controle.inserirProduto)

    def mostraMessagebox(self, titulo, mensagem, identificador):
        if identificador == True:
            messagebox.showinfo(titulo, mensagem)
        else:
            messagebox.showerror(titulo, mensagem)

class LimiteConsultaNF:
    def __init__(self, controle, root):
        self.janela = tk.Toplevel()
        self.janela.geometry('300x100')
        self.janela.title('Consulta de Nota Fiscal')
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameNumeroNF = tk.Frame(self.janela)
        self.frameNumeroNF.pack()

        self.labelNumeroNF = tk.Label(self.frameNumeroNF, text='Codigo')
        self.labelNumeroNF.pack(side='left')

        self.inputNumeroNF = tk.Entry(self.frameNumeroNF, width=20)
        self.inputNumeroNF.pack(side='left')

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

class CtrlNotaFiscal:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaProdutosNF = []

        if not os.path.isfile("NotaFiscal.pickle"):
            self.listaNotasFiscais =  []
        else:
            with open("NotaFiscal.pickle", "rb") as f:
                self.listaNotasFiscais = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaNotaFiscals(self):
        if len(self.listaNotasFiscais) != 0:
            with open("NotaFiscal.pickle","wb") as f:
                pickle.dump(self.listaNotasFiscais, f)

    #Funções auxiliares -----------------------------------------------------------

    def getNotaFiscal(self, numeroNF):
        for nf in self.listaNotasFiscais:
            if nf.getNumeroNF() == numeroNF:
                return nf
        return None

    #Funções instaciadoras ---------------------------------------------------------

    def insereNotasFiscais(self, root):
        listaProdutos = self.ctrlPrincipal.ctrlProduto.listaProdutos
        self.limiteInsere = LimiteInsereNF(self, root, listaProdutos)

    def consultaNotasFiscais(self, root):
        self.limiteConsulta = LimiteConsultaNF(self, root)
    
    #Funções dos Buttons Insere -----------------------------------------------------

    def inserirProduto(self, event):
        produtoSelecionado = self.limiteInsere.listboxItem.get(tk.ACTIVE)
        produto = self.ctrlPrincipal.ctrlProduto.getProduto(produtoSelecionado)
        self.listaProdutosNF.append(produto)
        self.limiteInsere.mostraMessagebox('Sucesso', 'Compra realizada com sucesso', True)
        self.limiteInsere.listboxItem.delete(tk.ACTIVE)
    
    def concluirCompra(self, event):
        numeroNF = self.limiteInsere.inputNumeroNF.get()
        nomeCliente = self.limiteInsere.inputNomeCliente.get()
        try:
            if len(numeroNF)==0 or len(nomeCliente)==0:
                raise CampoPreenchimentoVazio()
            if self.getNotaFiscal(numeroNF) != None:
                raise NotaFiscalDuplicada()
        except CampoPreenchimentoVazio:
            self.limiteInsere.mostraMessagebox('Error', 'Todos os campos devem ser preenchidos', False)
        except NotaFiscalDuplicada:
            self.limiteInsere.mostraMessagebox('Error', 'Numero {} de Nota Fiscal já existe!'.format(numeroNF), False)
        else:
            nf = NotaFiscal(numeroNF, nomeCliente, self.listaProdutosNF)
            self.listaNotasFiscais.append(nf)
            self.limiteInsere.mostraMessagebox('Sucesso', 'Nota Fiscal Gerada com sucesso', True)
            self.limiteInsere.janela.destroy()

    #Funções dos Buttons Consulta -------------------------------------------------------

    def consultar(self, event):
        numeroNF = self.limiteConsulta.inputNumeroNF.get()
        nf = self.getNotaFiscal(numeroNF)
        try:
            if len(numeroNF)==0:
                raise CampoPreenchimentoVazio()
            if nf == None:
                raise NotaFiscalInexistente()
        except CampoPreenchimentoVazio:
            self.limiteConsulta.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', False)
        except NotaFiscalInexistente:
            self.limiteConsulta.mostraMessagebox('Atenção', 'Nota Fiscal {} não existe!'.format(numeroNF), False)
        else:
            soma=0
            string = 'NOTA FISCAL ENCONTRADA \n\nNumeroNF: {} \nCliente: {}'.format(nf.getNumeroNF(), nf.getnomeCliente())
            string += '\n\nLista de Produtos: \n'
            for produto in self.listaProdutosNF:
                string += produto.getCodigo()+' -- '+produto.getDescricao()+' -- R$ '+produto.getValorUnitario()+'\n'
                soma += float(produto.getValorUnitario())
            string += '\n\nTotal de compra: R$ {}'.format(soma)
            self.limiteConsulta.mostraMessagebox('Consulta', string, True)
            self.clearConsulta(event)

    def clearConsulta(self, event):
        self.limiteConsulta.inputNumeroNF.delete(0, len(self.limiteConsulta.inputNumeroNF.get()))

    def finalizarConsulta(self, event):
        self.limiteConsulta.janela.destroy()
    

