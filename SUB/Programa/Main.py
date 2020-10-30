import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
import Produto as prod
import NotaFiscal as nf

class LimitePrincipal:
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry("500x400")
        self.menubar = tk.Menu(self.root)
        self.produto = tk.Menu(self.menubar)
        self.notaFiscal = tk.Menu(self.menubar)
        self.salva = tk.Menu(self.menubar)
        self.sair = tk.Menu(self.menubar)

        self.produto.add_command(label="Insere", command=self.controle.insereProdutos)
        self.produto.add_command(label="Consulta", command=self.controle.consultaProdutos)
        self.menubar.add_cascade(label="Produto", menu=self.produto)

        self.notaFiscal.add_command(label="Insere", command=self.controle.insereNotasFiscais)
        self.notaFiscal.add_command(label="Consulta", command=self.controle.consultaNotasFiscais)
        self.menubar.add_cascade(label="Nota Fiscal", menu=self.notaFiscal)

        self.salva.add_command(label="Salvar os Dados", command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Salvar", menu=self.salva)

        self.sair.add_command(label="Sair do Programa", command=self.controle.sair)
        self.menubar.add_cascade(label="Sair", menu=self.sair)

        self.root.config(menu=self.menubar)
    
    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = prod.CtrlProduto()
        self.ctrlNotaFiscal = nf.CtrlNotaFiscal(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.title('Sistema de Nota Fiscal')
        self.root.mainloop()

    ##########################################################
    def insereProdutos(self):
        self.ctrlProduto.insereProdutos(self.root)
    
    def consultaProdutos(self):
        self.ctrlProduto.consultaProdutos(self.root)

    ##########################################################
    def insereNotasFiscais(self):
        self.ctrlNotaFiscal.insereNotasFiscais(self.root)
    
    def consultaNotasFiscais(self):
        self.ctrlNotaFiscal.consultaNotasFiscais(self.root)
    
    ##########################################################
    def salvaDados(self):
        self.ctrlProduto.salvaProdutos()
        self.ctrlNotaFiscal.salvaNotaFiscals()
        self.limite.mostraMessagebox('Backup', 'Dados salvos com sucesso')
        
    def sair(self):
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()