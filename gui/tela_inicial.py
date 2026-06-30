import customtkinter as ctk
from gui.frame_esquerdo import frame_esquerdo
from gui.frame_principal import frame_principal

def criar_tela_inicial(janela):
    frame_esquerdo(janela)
    frame_principal(janela)
