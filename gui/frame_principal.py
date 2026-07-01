import customtkinter as ctk

def frame_p(janela):

    frame_principal = ctk.CTkFrame(
        master=janela,
        width=770,
        height=580,
        fg_color="#171B4D",
        corner_radius=20
    )

    frame_principal.place(x=220, y=10)