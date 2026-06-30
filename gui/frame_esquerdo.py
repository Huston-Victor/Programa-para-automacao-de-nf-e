import customtkinter as ctk

#==============
#Frame Esquerdo
#==============
def frame_esquerdo (janela):
    frame_esquerdo = ctk.CTkFrame(
    master = janela,
    width = 200,
    height= 580,
    fg_color ="#171B4D",
    corner_radius = 20
    )
    frame_esquerdo.place (x=10, y=10)