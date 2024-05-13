import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class MinhaAplicacao(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Listar Usuários")
        self.attributes('-fullscreen', True)
        self.controlador = Controlador()

        self.tela_listar_usuarios()

    def tela_listar_usuarios(self):
        self.clear_frame()

        ctk.CTkLabel(self, text="Lista de Usuários", font=("Arial", 16)).pack(pady=20)

        # Obtendo dados e cabeçalhos do backend
        usuarios, cabecalhos = self.controlador.listar_usuarios()

        # Criando a tabela com barra de rolagem horizontal
        self.criar_tabela(usuarios, cabecalhos)

        ctk.CTkButton(self, text="Voltar", command=self.menu_principal).pack(pady=10)

    def criar_tabela(self, dados, cabecalhos):
        # Frame container para Treeview e Scrollbar com espaçamento
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True, padx=10)

        # Criando o Treeview dentro do container
        tree = ttk.Treeview(container, columns=cabecalhos, show="headings", height=8)
        tree.pack(side="left", fill="both", expand=True)
        
        # Configurando as colunas
        for col in cabecalhos:
            tree.heading(col, text=col)
            tree.column(col, width=150, minwidth=50, stretch=tk.NO)

        # Configurando as tags para cores alternadas
        tree.tag_configure('evenrow', background='#544F59')
        tree.tag_configure('oddrow', background='#262526')

        # Inserindo dados na tabela
        for index, row in enumerate(dados):
            tree.insert('', 'end', values=row, tags=('evenrow' if index % 2 == 0 else 'oddrow'))

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def menu_principal(self):
        # Implemente a lógica para voltar ao menu principal
        pass

class Controlador:
    def listar_usuarios(self):
        # Dados fictícios e cabeçalhos dinâmicos de exemplo
        dados = [
            ("Maria Oliveira", "987.654.321-00", "maria.oliveira@email.com", "21 98765-4321", "Sim", "Editar", "Excluir", "Adape", "Corno", "Absurdamente Grande"),
            ("Carlos Andrade", "222.333.444-55", "carlos.andrade@email.com", "31 91234-5678")
        ]
        cabecalhos = ["Nome", "CPF", "Email", "Telefone", "Gestor", "Ações", "Adape", "Corno", "Absurdamente Grande"]
        return dados, cabecalhos

if __name__ == '__main__':
    app = MinhaAplicacao()
    app.mainloop()
