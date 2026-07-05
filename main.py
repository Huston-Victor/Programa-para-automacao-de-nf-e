import customtkinter as ctk

from config.configuracoes import configuracoes_janela
from utils.centralizar import centralizar
from gui.tela_inicial import criar_tela_inicial

janela = ctk.CTk()

configuracoes_janela(janela)
centralizar(janela, 1000, 600)

criar_tela_inicial(janela)

janela.mainloop() 