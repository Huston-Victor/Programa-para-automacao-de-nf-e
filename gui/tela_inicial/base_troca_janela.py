import customtkinter as ctk

def base_troca(janela):

    frame_principal = ctk.CTkFrame(
        master=janela,
        width=770,
        height=580,
        fg_color="#1E293B",
        corner_radius=20
    )

    frame_principal.place(x=220, y=10)
    return frame_principal