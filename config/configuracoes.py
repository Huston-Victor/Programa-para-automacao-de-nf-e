import customtkinter as ctk


def configuracoes_janela (janela):
    ctk.set_appearance_mode ('dark')
    janela.resizable(False, False)
    janela.configure (fg_color = "#0F172A")
    janela.iconbitmap("assets/icones/icone_leitor.ico")
    janela.title("Leitor De NF-e")
