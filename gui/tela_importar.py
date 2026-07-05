import customtkinter as ctk
from PIL import Image
from gui.tela_tracejada import tela_tracejada

def frame_importar(frame):

    texto_importarNFe(frame)
    sub_importar(frame)
    imagem_tracejada(frame)
    frame_tracejado(frame) 
    

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





