#==========================
# Bibliotecas e Importações
#-=========================

import customtkinter as ctk
from config.configuracoes import configuracoes_janela

from utils.centralizar import centralizar

from gui.tela_inicial import criar_tela_inicial

# ===========================
# Criação Da Janela Principal
# ===========================

janela = ctk.CTk()

configuracoes_janela(janela)
centralizar(janela, 1000, 600)

criar_tela_inicial(janela)

# ===========================
# Looping Da Janela Principal
# ===========================

janela.mainloop()