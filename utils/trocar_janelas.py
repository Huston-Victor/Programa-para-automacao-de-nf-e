import customtkinter as ctk

def trocar_tela(frame_principal, tela):
    for widget in frame_principal.winfo_children():
        widget.destroy()
    tela(frame_principal)