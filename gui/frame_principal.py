import customtkinter as ctk
from PIL import Image
from gui.tela_tracejada import tela_tracejada

from utils.centralizar import centralizar_widget

def frame_p(janela):

    frame_principal = ctk.CTkFrame(
        master=janela,
        width=770,
        height=580,
        fg_color="#1E293B",
        corner_radius=20
    )

    frame_principal.place(x=220, y=10)
    texto_importarNFe(frame_principal)
    sub_importar(frame_principal)
    imagem_tracejada(frame_principal)
    frame_tracejado(frame_principal) 
    

def texto_importarNFe(frame):
    texto_importar = ctk.CTkLabel(
        frame,
        text="Importar NF-e",
        text_color="white",
        font=("Arial", 26, "bold")
    )
    texto_importar.place(x=20, y=20)

def sub_importar(frame):
    sub_texto_importar = ctk.CTkLabel(
        frame,
        text="Selecione ou Arraste os Arquivos da Nota Fiscal Para Iniciar o Processamento",
        text_color="grey",
        font=("Arial", 14)
    )
    sub_texto_importar.place(x=20, y=60)

def imagem_tracejada(frame):
    broda_tracejada = ctk.CTkImage(
        light_image=Image.open("assets/imagens/borda_tracejada.png"),
        dark_image=Image.open("assets/imagens/borda_tracejada.png"),
        size=(730, 400)
    )

    label_borda = ctk.CTkLabel(frame, image=broda_tracejada, text="")
    label_borda.place(x=20, y=100)

def frame_tracejado (frame):
    frame_interno_tracejado = ctk.CTkFrame(
        master=frame,
        width=693,
        height=342,
        fg_color="#273449",
        
    )
    frame_interno_tracejado.place(x=40, y=125)

    tela_tracejada(frame_interno_tracejado)





