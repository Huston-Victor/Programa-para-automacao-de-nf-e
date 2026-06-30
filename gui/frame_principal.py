import customtkinter as ctk

def frame_principal (janela):
    frame_principal = ctk.CTk.frame (
    master = janela,
    width = 600,
    higth = 580,
    fg_color ="#171B4D",
    corner_radius = 20
    )
    frame_principal.place (x=100, y=10)