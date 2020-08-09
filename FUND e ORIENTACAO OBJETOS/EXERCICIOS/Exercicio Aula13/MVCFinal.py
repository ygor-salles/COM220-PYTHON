import tkinter as tk
from tkinter import messagebox

class ModelCliente():
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.viewPanel = ViewPanel(master, controller)

class ViewPanel():
    def __init__(self, root, controller):
        self.controller = controller
        self.janela = tk.Frame(root)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
      
        self.labelInfo1 = tk.Label(self.frame1,text="Nome:")
        self.labelInfo2 = tk.Label(self.frame2,text="E-mail:")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")  

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.janela,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.enterHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)         

        self.buttonClientes = tk.Button(self.janela, text='Mostra Clientes')
        self.buttonClientes.pack(side="left")
        self.buttonClientes.bind("<Button>", controller.clientesHandler)

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.listaClientes = []       

        # Cria a view passando referencia da janela principal e
        #de si próprio (controlador)
        self.view = View(self.root, self)

        self.root.title('Exemplo MVC')
        #Inicia o MainLoop
        self.root.mainloop()

    def enterHandler(self, event):
        nomeCli = self.view.viewPanel.inputText1.get()
        emailCli = self.view.viewPanel.inputText2.get()
        cliente = ModelCliente(nomeCli, emailCli)
        self.listaClientes.append(cliente)
        self.view.viewPanel.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.viewPanel.inputText1.delete(0, len(self.view.viewPanel.inputText1.get()))
        self.view.viewPanel.inputText2.delete(0, len(self.view.viewPanel.inputText2.get()))

    def clientesHandler(self, event):
        self.message = 'Clientes cadastrados: \n'
        for cliente in self.listaClientes:
            self.message += cliente.getNome()+' - '+cliente.getEmail()+'\n'
        self.view.viewPanel.mostraJanela('Lista de Clientes', self.message)

if __name__ == '__main__':
    c = Controller()

