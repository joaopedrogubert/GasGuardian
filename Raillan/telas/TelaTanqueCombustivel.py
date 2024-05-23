from controladores.controladorTanqueCombustivel import ControladorTanqueCombustivel
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class TelaTanqueCombustivel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controladorTanqueCombustivel = ControladorTanqueCombustivel()
        self.selected_row = None
        self.cabecalhos = [ "Nome", "Capacidade", "Porcentagem Alerta", "Combustível", "Volume Atual"]
        self.tanques = self.controladorTanqueCombustivel.listar_tanques()
        self.tela_listar_tanques()

    def tela_listar_tanques(self):
        self.clear_frame()

        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=20, pady=10)

        # Título alinhado à esquerda com fonte maior
        ctk.CTkLabel(top_frame, text="Lista de Tanques", font=("Arial", 25, "bold")).pack(side="left")

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
        self.criar_tabela(self.tanques, self.cabecalhos)

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
        self.tree.tag_configure('evenrow', background='#242424')
        self.tree.tag_configure('oddrow', background='#2D2E30')

        # Inserindo dados na tabela
        self.update_table(dados)

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
            self.modal_alterar_tanque(self.selected_row)

    def modal_alterar_tanque(self, dados_tanque):
        self.modal = tk.Toplevel(self)
        self.modal.title("Alterar Tanque")
        self.modal.geometry("500x500")
        
        self.labels = ["Nome", "Capacidade", "Porcentagem Alerta", "Combustível", "Volume Atual"]
        self.entries = {}
        
        for i, label in enumerate(self.labels):
            lbl = ctk.CTkLabel(self.modal, text=label)
            lbl.grid(row=i, column=0, padx=10, pady=5)
            entry = ctk.CTkEntry(self.modal)
            entry.grid(row=i, column=1, padx=10, pady=5)
            if i == 0:
                entry.insert(0, dados_tanque[i])
                entry.configure(state='disabled')  # Desabilitar edição do identificador
            else:
                entry.insert(0, dados_tanque[i])
            self.entries[label] = entry
        
        update_button = ctk.CTkButton(self.modal, text="Atualizar", command=self.atualizar_tanque)
        update_button.grid(row=len(self.labels), columnspan=2, pady=20)

    def atualizar_tanque(self):
        nome = self.entries["Nome"].get()
        capacidade = self.entries["Capacidade"].get()
        porcentagem_alerta = self.entries["Porcentagem Alerta"].get()
        combustivel = self.entries["Combustível"].get()
        volume_atual = self.entries["Volume Atual"].get()
        identificadorTanque = self.selected_row[5]
        print(f"ID: {id}")

        resultado = self.controladorTanqueCombustivel.atualizar_tanque(capacidade, porcentagem_alerta, combustivel, volume_atual, identificadorTanque)
        if resultado:
            print("Tanque atualizado com sucesso!")
        else:
            print("Erro ao atualizar o tanque.")
        
        self.modal.destroy()

    def excluir_tanque(self):
        if self.selected_row:
            self.controladorTanqueCombustivel.remover_tanque(self.selected_row[5])
            self.pesquisar()
            self.btn_alterar.configure(state=tk.DISABLED)
            self.btn_excluir.configure(state=tk.DISABLED)

    def pesquisar(self):
        # Lógica para pesquisar e carregar os dados na grid
        tanques = self.controladorTanqueCombustivel.listar_tanques()
        self.update_table(tanques)

    def update_table(self, dados):
        # Limpar a tabela atual
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Inserir novos dados na tabela
        for index, row in enumerate(dados):
            self.tree.insert('', 'end', values=row, tags=('evenrow' if index % 2 == 0 else 'oddrow'))

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
    root = tk.Tk()
    root.geometry("1200x800")
    app = TelaTanqueCombustivel(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
