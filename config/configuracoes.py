import customtkinter as ctk

#================
#Visual Da Janela
#================

def configuracoes_janela (janela):
    ctk.set_appearance_mode ('dark')
    janela.resizable(False, False)
    janela.configure (fg_color = "#11132E")
