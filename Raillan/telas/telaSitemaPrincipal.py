import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class MenuPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gerenciamento")
        self.geometry("1200x800")

        # Inicializar a lista de imagens
        self.images = []

        # Configurando a estrutura do menu lateral e o container principal
        self.configure_grid()
        self.configure_style()
        self.create_menu()

        # Inicializando os frames
        self.frames = {}

    def configure_grid(self):
        self.grid_columnconfigure(0, weight=0, minsize=300)  # Largura fixa do menu
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)

    def configure_style(self):
        # Estilo do Treeview
        style = ttk.Style()
        style.configure("Treeview", 
                        font=("Arial", 25, "bold"),   # Fonte das opções do menu
                        rowheight=50,                # Altura das linhas
                        background="lightgrey",      # Fundo das linhas
                        fieldbackground="lightgrey", # Fundo do campo de entrada
                        foreground="black")          # Cor do texto
        style.configure("Treeview.Heading", font=("Arial", 30, "bold"))
        
        # Configuração do ícone do botão para expandir/contrair
        style.layout("Treeview.Item", [('Treeitem.padding', {'sticky': 'nswe', 'children': [('Treeitem.indicator', {'side': 'left', 'sticky': ''}), ('Treeitem.image', {'side': 'left', 'sticky': ''}), ('Treeitem.text', {'side': 'left', 'sticky': ''})]})])
        style.configure("Treeitem.indicator", indicatorcolor="black")

        # Definindo a cor de fundo do aplicativo
        self.configure(bg="lightgrey")

    def create_menu(self):
        # Menu lateral
        self.menu_frame = ctk.CTkFrame(self, fg_color="lightgrey", width=200)
        self.menu_frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

        # Label do Menu
        ctk.CTkLabel(self.menu_frame, text="Menu", font=("Arial", 30, "bold"), fg_color="lightgrey").pack(pady=20)

        self.tree_menu = ttk.Treeview(self.menu_frame, show="tree", selectmode="browse", style="Treeview")
        self.tree_menu.pack(fill="both", expand=True)

        # Adicionando itens ao menu
        icon_path_base = "/Users/railanabreu/Documents/Projects/GasGuardian/Raillan/telas/Icones/"
        self.add_menu_item("", "abastecimento", "Abastecimento", icon_path_base + "afundando.png", True)
        self.add_separator(self.menu_frame)
        
        # Adicionando item "Cadastro" com ícone
        cadastro_id = self.add_menu_item("", "cadastro", "Cadastro", icon_path_base + "cadastro.png", True)
        self.add_menu_item(cadastro_id, "funcionarios", "Funcionários", icon_path_base + "Funcionarios.png")
        self.add_menu_item(cadastro_id, "tanques", "Tanques", icon_path_base + "tanquesCombustivel.png")
        self.add_menu_item(cadastro_id, "combustiveis", "Combustíveis", icon_path_base + "oil.png")
        self.add_menu_item(cadastro_id, "bombas", "Bombas", icon_path_base + "bomba-de-gasolina.png")
        self.add_separator(self.menu_frame)

        self.add_menu_item("", "relatorios", "Relatórios", icon_path_base + "relatorios.png", True)

        # Configuração das tags
        self.tree_menu.tag_configure("main", font=("Arial", 30, "bold"), foreground="black")
        self.tree_menu.tag_configure("sub", font=("Arial", 25, "bold"), foreground="black")

        self.tree_menu.bind("<<TreeviewSelect>>", self.on_menu_select)

    def add_menu_item(self, parent, id, text, icon_path, is_main=False):
        icon = self.get_icon(icon_path)
        if icon:
            # Adiciona o texto com um espaçamento à esquerda para o ícone
            return self.tree_menu.insert(parent, "end", id, text=" " + text, image=icon, tags=("main" if is_main else "sub",))
        else:
            return self.tree_menu.insert(parent, "end", id, text=text, tags=("main" if is_main else "sub",))

    def add_separator(self, parent):
        separator = ctk.CTkFrame(parent, height=2, fg_color="black")
        separator.pack(fill="x", padx=5, pady=2)

    def get_icon(self, path):
        if os.path.exists(path):
            image = Image.open(path)
            image = image.resize((25, 25), Image.LANCZOS)

            photo = ImageTk.PhotoImage(image)
            self.images.append(photo)  # Adiciona a imagem à lista para evitar coleta de lixo
            return photo
        else:
            print(f"Ícone não encontrado: {path}")
            return None

    def on_menu_select(self, event):
        selected_item = self.tree_menu.selection()[0]
        print(f"Selecionado: {selected_item}")
        # Aqui você pode adicionar a lógica para mostrar o frame correspondente
        # Exemplo: self.show_frame(selected_item)

    def show_frame(self, frame_name):
        # Implementar a lógica para mostrar o frame correspondente
        # frame = self.frames.get(frame_name)
        # if frame:
        #     frame.tkraise()
        pass

if __name__ == '__main__':
    ctk.set_appearance_mode("light")  # Define o modo de aparência para claro
    app = MenuPrincipal()
    app.mainloop()
