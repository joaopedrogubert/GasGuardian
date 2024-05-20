import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

from ..controladores.controladorTanqueCombustivel import ControladorTanqueCombustivel

class TelaTanqueCombustivel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controladorTanqueCombustivel = ControladorTanqueCombustivel()
        self.selected_row = None

    def tela_listar_tanques(self):
        cabecalhos = None
        tanques = None
        self.clear_frame()

        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=20, pady=10)

        # Título alinhado à esquerda com fonte maior
        ctk.CTkLabel(top_frame, text="Lista de Usuários", font=("Arial", 25,"bold")).pack(side="left")

        # Botões alinhados à direita
        btn_frame = ctk.CTkFrame(top_frame)
        btn_frame.pack(side="right")

        btn_add = ctk.CTkButton(btn_frame, text="+", command=self.cadastrar_tanque)
        btn_add.pack(side="left", padx=5)

        self.btn_alterar = ctk.CTkButton(btn_frame, text="Alterar", command=self.alterar_tanque, state=tk.DISABLED)
        self.btn_alterar.pack(side="left", padx=5)

        self.btn_excluir = ctk.CTkButton(btn_frame, text="Excluir", command=self.excluir_tanque, state=tk.DISABLED)
        self.btn_excluir.pack(side="left", padx=5)


        # Criando a tabela responsiva com barra de rolagem horizontal
        self.criar_tabela(cabecalhos, tanques )

        # Adicionando botão de pesquisa na parte inferior direita
        btn_pesquisar = ctk.CTkButton(self, text="Pesquisar", command=self.pesquisar)
        btn_pesquisar.pack(side="bottom", anchor="se", padx=10, pady=10)

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
        self.tree.tag_configure('evenrow', background='#E6E6E6')
        self.tree.tag_configure('oddrow', background='#FFFFFF')

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

    def alterar_tanque(self):
        if self.selected_row:
            # Lógica para alterar as informações do usuário
            print(f"Alterar usuário: {self.selected_row}")

    def excluir_tanque(self):
        if self.selected_row:
            # Lógica para excluir o usuário
            print(f"Excluir usuário: {self.selected_row}")

    def pesquisar(self):
        # Lógica para pesquisar e carregar os dados na grid
        self.clear_frame()
        return self.controladorTanqueCombustivel.listar_tanques()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def menu_principal(self):
        # Implemente a lógica para voltar ao menu principal
        pass

    def cadastrar_tanque(self):
        # Lógica para abrir a tela de cadastro de novo tanque
        print("Abrir tela de cadastro de novo tanque")


if __name__ == '__main__':
    ctk.set_appearance_mode("light")  # Define o modo de aparência para claro
    app = TelaTanqueCombustivel()
    app.mainloop()
