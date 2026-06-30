import customtkinter as ctk

#================================================
#Função Responsável Por Centralizar O App Na Tela
#================================================

def centralizar(janela, largura, altura):

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2

    janela.geometry(f"{largura}x{altura}+{x}+{y}")