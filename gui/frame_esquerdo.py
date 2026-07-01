import customtkinter as ctk
from PIL import Image
from utils.centralizar import centralizar_widget

def frame_e(janela):
    frame_esquerdo = ctk.CTkFrame(
        master=janela,
        width=200,
        height=580,
        fg_color="#172554",
        corner_radius=20
    )

    frame_esquerdo.place(x=10, y=10)

    imagem_principal(frame_esquerdo)
    nome_app(frame_esquerdo)
    texto_app(frame_esquerdo)
    botao_importar(frame_esquerdo)


def imagem_principal(frame):
    imagem = ctk.CTkImage(
        light_image=Image.open("assets/imagens/imagem_leitor.png"),
        dark_image=Image.open("assets/imagens/imagem_leitor.png"),
        size=(120, 120)
    )

    label_imagem = ctk.CTkLabel(frame, image=imagem, text="")
    label_imagem.place(x=40, y=10)


def nome_app(frame):
    nome_aplicativo = ctk.CTkLabel(
        frame,
        text="Leitor De NF-e",
        text_color="white",
        font=("Arial", 26, "bold")
    )

    centralizar_widget(nome_aplicativo, frame, y=140)

def texto_app(frame):
    texto_aplicativo = ctk.CTkLabel(
        frame,
        text="Automação de Lançamentos",
        text_color="grey",
        font=("Arial", 14)
    )

    centralizar_widget(texto_aplicativo, frame, y=165)

def botao_importar(frame):
    imagem_importar = ctk.CTkImage(
        light_image=Image.open("assets/imagens/importar_arquivos.png"),
        dark_image=Image.open("assets/imagens/importar_arquivos.png"),
        size=(40, 40),
    )

    
    botao_importar = ctk.CTkButton(
        frame,
        text="Importar NF-e",
        image=imagem_importar,
        compound="left",
        width=150,
        height=40,
        fg_color="#1E52A7",
        hover_color="#2563EB",
        corner_radius=20,
        text_color="white",
        font=("Arial", 15, "bold")
    )

    centralizar_widget(botao_importar, frame, y=220)