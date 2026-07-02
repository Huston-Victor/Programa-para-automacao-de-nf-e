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
    botao_abastesimento(frame_esquerdo)
    linha_ajuda(frame_esquerdo)
    botao_ajuda(frame_esquerdo)
    
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
        size=(35, 35),
    )

    
    botao_importar = ctk.CTkButton(
        frame,
        text="Importar NF-e",
        image=imagem_importar,
        compound="left",
        width=150,
        height=40,
        fg_color="#0E3E8B",
        hover_color="#1B58DD",
        corner_radius=20,
        text_color="white",
        font=("Arial", 15, "bold")
    )

    centralizar_widget(botao_importar, frame, y=220)

def botao_abastesimento (frame):
    imagem_abastecimento = ctk.CTkImage(
        light_image=Image.open("assets/imagens/abastecimento.png"),
        dark_image=Image.open("assets/imagens/abastecimento.png"),
        size=(28, 28),
    )

    botao_abastecimento = ctk.CTkButton(
        frame,
        text="Abastecimento",
        image=imagem_abastecimento,
        compound="left",
        width=150,
        height=40,
        fg_color="#0E3E8B",
        hover_color="#1B58DD",
        corner_radius=20,
        text_color="white",
        font=("Arial", 15, "bold")
    )

    centralizar_widget(botao_abastecimento, frame, y=270)

def linha_ajuda (frame):
    linha = ctk.CTkFrame(
        master=frame,
        width=180,
        height=2,
        fg_color="darkgrey"
    )

    centralizar_widget(linha, frame, y=530)

def botao_ajuda (frame):
    imagem_ajuda = ctk.CTkImage(
        light_image=Image.open("assets/imagens/botao_ajuda.png"),
        dark_image=Image.open("assets/imagens/botao_ajuda.png"),
        size=(28, 28),
    )

    botao_ajuda = ctk.CTkButton(
        frame,
        text="Ajuda",
        image=imagem_ajuda,
        compound="left",
        width=150,
        height=40,
        fg_color="#172554",
        hover_color="#1B58DD",
        corner_radius=20,
        text_color="grey",
        font=("Arial", 15, "bold")
    )

    centralizar_widget(botao_ajuda, frame, y=555)