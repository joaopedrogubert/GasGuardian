from ..controladores.controladorUsuario import ControladorUsuario
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class TelaUsuario(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciamento de Usuários")
        self.geometry("900x900")
        self.controlador = ControladorUsuario()
        # Botões do Menu Principal
        self.menu_principal()

    def menu_principal(self):
        self.clear_frame()
        ctk.CTkLabel(self, text="Dados do Usuário", font=("Arial", 16)).pack(pady=20)
        ctk.CTkButton(self, text="Criar Usuário", command=self.tela_criar_usuario).pack(pady=10)
        ctk.CTkButton(self, text="Listar Usuários", command=self.tela_listar_usuarios).pack(pady=10)
        ctk.CTkButton(self, text="Alterar Usuário", command=self.tela_alterar_usuario).pack(pady=10)
        ctk.CTkButton(self, text="Excluir Usuário", command=self.tela_excluir_usuario).pack(pady=10)

    def clear_frame(self):
        # Destruir todos os widgets que são filhos do frame principal da janela
        for widget in self.winfo_children():
            widget.destroy()

    def tela_criar_usuario(self):
        self.clear_frame()
        ctk.CTkLabel(self, text="Criar Novo Usuário", font=("Arial", 16)).pack(pady=20)
        self.cpf = ctk.CTkEntry(self,width=300, placeholder_text="CPF")
        self.cpf.pack(pady=5)
        self.email = ctk.CTkEntry(self, width=300, placeholder_text="Email")
        self.email.pack(pady=5)
        self.nome = ctk.CTkEntry(self, width=300, placeholder_text="Nome")
        self.nome.pack(pady=5)
        self.telefone = ctk.CTkEntry(self, width=300, placeholder_text="Telefone")
        self.telefone.pack(pady=5)
        self.senha = ctk.CTkEntry(self, width=300, placeholder_text="Senha")
        self.senha.pack(pady=5)
        self.confirmar_senha = ctk.CTkEntry(self, width=300, placeholder_text="Confirmar Senha")
        self.confirmar_senha.pack(pady=5)
        self.isGestor = ctk.CTkCheckbutton(self, text="É Gestor?")
        self.isGestor.pack(pady=5)
        ctk.CTkButton(self, text="Salvar Usuário", command=self.salvar_usuario).pack(pady=20)
        ctk.CTkButton(self, text="Voltar", command=self.menu_principal).pack(pady=20)

    def salvar_usuario(self):
        cpf = self.cpf.get().strip()
        email = self.email.get().strip()
        nome = self.nome.get().strip()
        telefone = self.telefone.get().strip()
        senha = self.senha.get().strip()
        confirmar_senha = self.confirmar_senha.get().strip()
        isGestor = self.isGestor.get()

        if not cpf or not email or not nome or not telefone or not senha or not confirmar_senha:
            ctk.CTkLabel(self, text="Todos os campos devem ser preenchidos!", text_color="red").pack(pady=20)
            return

        if senha != confirmar_senha:
            ctk.CTkLabel(self, text="Senhas não conferem!", text_color="red").pack(pady=20)
            return

        novo_usuario = self.controlador.usuario(cpf, email, nome, telefone, senha, isGestor)
        try:
            self.controlador.adicionar_usuario(novo_usuario)
            ctk.CTkLabel(self, text="Usuário salvo com sucesso!", text_color="green").pack(pady=20)
            self.after(1000, self.menu_principal)
        except Exception as e:
            ctk.CTkLabel(self, text=str(e), text_color="red").pack(pady=20)

        
    def tela_listar_usuarios(self):
        self.clear_frame()
        usuarios = self.controlador.listar_usuarios()
        ctk.CTkLabel(self, text="Lista de Usuários", font=("Arial", 16)).pack(pady=20)
        if usuarios:
            for usuario in usuarios:
                ctk.CTkLabel(self, text=f"{usuario[2]} - {usuario[0]}").pack(pady=2)
        else:
            ctk.CTkLabel(self, text="Nenhum usuário cadastrado.").pack(pady=20)
        ctk.CTkButton(self, text="Voltar", command=self.menu_principal).pack(pady=10)
    