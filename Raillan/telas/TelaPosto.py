from ..controladores.controladorPosto import ControladorPosto
import customtkinter as ctk

class TelaPosto(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciamento de Postos de Gasolina")
        self.geometry("900x900")
        self.controlador = ControladorPosto()
        # Botões do Menu Principal
        self.menu_principal()

    def menu_principal(self):
        self.clear_frame()
        ctk.CTkLabel(self, text="Dados do Posto", font=("Arial", 16)).pack(pady=20)
        ctk.CTkButton(self, text="Criar Posto", command=self.tela_criar_posto).pack(pady=10)
        ctk.CTkButton(self, text="Listar Postos", command=self.tela_listar_postos).pack(pady=10)
        ctk.CTkButton(self, text="Alterar Posto", command=self.tela_alterar_posto).pack(pady=10)
        ctk.CTkButton(self, text="Excluir Posto", command=self.tela_excluir_posto).pack(pady=10)

    def clear_frame(self):
        # Destruir todos os widgets que são filhos do frame principal da janela
        for widget in self.winfo_children():
            widget.destroy()

    def tela_criar_posto(self):
        self.clear_frame()
        ctk.CTkLabel(self, text="Criar Novo Posto", font=("Arial", 16)).pack(pady=20)
        self.nome_posto = ctk.CTkEntry(self,width=300, placeholder_text="Nome do Posto")
        self.nome_posto.pack(pady=5)
        self.cnpj = ctk.CTkEntry(self, width=300, placeholder_text="CNPJ")
        self.cnpj.pack(pady=5)
        self.chave_pix = ctk.CTkEntry(self, width=300, placeholder_text="Chave PIX")
        self.chave_pix.pack(pady=5)
        ctk.CTkButton(self, text="Salvar Posto", command=self.salvar_posto).pack(pady=20)

    def salvar_posto(self):
        cnpj = self.cnpj.get().strip()
        chavePix = self.chave_pix.get().strip()
        nomePosto = self.nome_posto.get().strip()

        if not cnpj or not chavePix or not nomePosto:
            ctk.CTkLabel(self, text="Todos os campos devem ser preenchidos!", text_color="red").pack(pady=20)
            self.after(3000, self.menu_principal)
            return

        novo_posto = self.controlador.posto(cnpj, chavePix, nomePosto)
        try:
            self.controlador.adicionar_posto(novo_posto)
            ctk.CTkLabel(self, text="Posto salvo com sucesso!", text_color="green").pack(pady=20)
        except Exception as e:
            ctk.CTkLabel(self, text=str(e), text_color="red").pack(pady=20)

        self.after(3000, self.menu_principal)


    def tela_listar_postos(self):
        self.clear_frame()
        postos = self.controlador.listar_postos()
        ctk.CTkLabel(self, text="Lista de Postos", font=("Arial", 16)).pack(pady=20)
        if postos:
            for posto in postos:
                ctk.CTkLabel(self, text=f"{posto[2]} - {posto[0]}").pack(pady=2)
        else:
            ctk.CTkLabel(self, text="Nenhum posto cadastrado.").pack(pady=20)
        ctk.CTkButton(self, text="Voltar", command=self.menu_principal).pack(pady=10)

    def salvar_alteracoes_posto(self):
        # Capturar os dados dos campos de entrada
        cnpj = self.cnpj_alterar.get()
        novo_nome = self.novo_nome_posto.get()
        nova_chave_pix = self.nova_chave_pix.get()

        alteracoes_posto = self.controlador.posto(cnpj, nova_chave_pix, novo_nome)
        # Lógica para atualizar o posto no banco de dados
        try:
            sucesso = self.controlador.atualizar_posto(alteracoes_posto)
            if sucesso:
                mensagem = "Posto atualizado com sucesso!"
                cor = "green"
            else:
                mensagem = "Falha ao atualizar posto. Verifique o CNPJ."
                cor = "red"
        except Exception as e:
            mensagem = str(e)
            cor = "red"

        # Exibir mensagem de sucesso ou erro
        ctk.CTkLabel(self, text=mensagem, text_color=cor).pack(pady=20)
        self.after(3000, self.menu_principal)

    
    def tela_alterar_posto(self):
        self.clear_frame()
        ctk.CTkLabel(self, text="Alterar Posto", font=("Arial", 16)).pack(pady=20)

        # Campos para inserir o CNPJ do posto a ser alterado e os novos dados
        self.cnpj_alterar = ctk.CTkEntry(self, width=300, placeholder_text="CNPJ do Posto")
        self.cnpj_alterar.pack(pady=5)
        
        self.novo_nome_posto = ctk.CTkEntry(self,width=300, placeholder_text="Novo Nome do Posto")
        self.novo_nome_posto.pack(pady=5)
        
        self.nova_chave_pix = ctk.CTkEntry(self, width=300, placeholder_text="Nova Chave PIX")
        self.nova_chave_pix.pack(pady=5)
        
        # Botão para salvar as alterações
        ctk.CTkButton(self, text="Salvar Alterações", command=self.salvar_alteracoes_posto).pack(pady=10)
        
        # Botão para cancelar a ação e voltar ao menu principal
        ctk.CTkButton(self, text="Cancelar", command=self.menu_principal).pack(pady=10)

    
    
    def tela_excluir_posto(self):
        self.clear_frame()
        ctk.CTkLabel(self, text="Excluir Posto", font=("Arial", 16)).pack(pady=20)
        self.cnpj_excluir = ctk.CTkEntry(self, placeholder_text="CNPJ do Posto a Excluir")
        self.cnpj_excluir.pack(pady=5)
        ctk.CTkButton(self, text="Excluir Posto", command=self.excluir_posto).pack(pady=20)

    def excluir_posto(self):
        if self.controlador.remover_posto(self.cnpj_excluir.get()):
            ctk.CTkLabel(self, text="Posto excluído com sucesso!", text_color="green").pack(pady=20)
        else:
            ctk.CTkLabel(self, text="Falha ao excluir posto!", text_color="red").pack(pady=20)
        self.after(3000, self.menu_principal)

if __name__ == '__main__':
    app = TelaPosto()
    app.mainloop()