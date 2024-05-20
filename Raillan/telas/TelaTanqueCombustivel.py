import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class TelaTanqueCombustivel(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Listar Usuários")
        self.attributes('-fullscreen', True)
        self.controlador = Controlador()

        self.selected_row = None

        self.tela_listar_usuarios()

    def tela_listar_usuarios(self):
        self.clear_frame()

        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=20, pady=10)

        # Título alinhado à esquerda com fonte maior
        ctk.CTkLabel(top_frame, text="Lista de Usuários", font=("Arial", 20)).pack(side="left")

        # Botões alinhados à direita
        btn_frame = ctk.CTkFrame(top_frame)
        btn_frame.pack(side="right")

        btn_add = ctk.CTkButton(btn_frame, text="+", command=self.cadastrar_tanque)
        btn_add.pack(side="left", padx=5)

        self.btn_alterar = ctk.CTkButton(btn_frame, text="Alterar", command=self.alterar_usuario, state=tk.DISABLED)
        self.btn_alterar.pack(side="left", padx=5)

        self.btn_excluir = ctk.CTkButton(btn_frame, text="Excluir", command=self.excluir_usuario, state=tk.DISABLED)
        self.btn_excluir.pack(side="left", padx=5)

        # Obtendo dados e cabeçalhos do backend
        usuarios, cabecalhos = self.controlador.listar_usuarios()

        # Criando a tabela responsiva com barra de rolagem horizontal
        self.criar_tabela(usuarios, cabecalhos)

        ctk.CTkButton(self, text="Voltar", command=self.menu_principal).pack(pady=10)

    def criar_tabela(self, dados, cabecalhos):
        # Frame container para Treeview e Scrollbar com espaçamento
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True, padx=10, pady=20)

        # Adicionando Scrollbars
        scrollbar_x = ttk.Scrollbar(container, orient="horizontal")
        scrollbar_y = ttk.Scrollbar(container, orient="vertical")

        self.tree = ttk.Treeview(container, columns=cabecalhos, show="headings", height=8,
                                 xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
        
        scrollbar_x.pack(side="bottom", fill="x")
        scrollbar_y.pack(side="right", fill="y")

        scrollbar_x.config(command=self.tree.xview)
        scrollbar_y.config(command=self.tree.yview)

        self.tree.pack(side="left", fill="both", expand=True)

        # Adicionando evento de seleção de linha
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)
        
        # Configurando as colunas
        for col in cabecalhos:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        # Configurando as tags para cores alternadas
        self.tree.tag_configure('evenrow', background='#544F59')
        self.tree.tag_configure('oddrow', background='#262526')

        # Inserindo dados na tabela
        for index, row in enumerate(dados):
            self.tree.insert('', 'end', values=row, tags=('evenrow' if index % 2 == 0 else 'oddrow'))

    def on_row_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            self.selected_row = self.tree.item(selected_item[0], "values")
            self.btn_alterar.configure(state=tk.NORMAL)
            self.btn_excluir.configure(state=tk.NORMAL)
        else:
            self.selected_row = None
            self.btn_alterar.configure(state=tk.DISABLED)
            self.btn_excluir.configure(state=tk.DISABLED)

    def alterar_usuario(self):
        if self.selected_row:
            # Lógica para alterar as informações do usuário
            print(f"Alterar usuário: {self.selected_row}")

    def excluir_usuario(self):
        if self.selected_row:
            # Lógica para excluir o usuário
            print(f"Excluir usuário: {self.selected_row}")

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def menu_principal(self):
        # Implemente a lógica para voltar ao menu principal
        pass

    def cadastrar_tanque(self):
        # Lógica para abrir a tela de cadastro de novo tanque
        print("Abrir tela de cadastro de novo tanque")

class Controlador:
    def listar_usuarios(self):
        # Dados fictícios e cabeçalhos dinâmicos de exemplo
        dados = [
            ("Maria Oliveira", "987.654.321-00", "maria.oliveira@email.com", "21 98765-4321"),
            ("Carlos Andrade", "222.333.444-55", "carlos.andrade@email.com", "31 91234-5678")
        ]
        cabecalhos = ["Nome", "CPF", "Email", "Telefone"]
        return dados, cabecalhos

if __name__ == '__main__':
    app = TelaTanqueCombustivel()
    app.mainloop()
