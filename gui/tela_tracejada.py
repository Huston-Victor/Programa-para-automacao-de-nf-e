import customtkinter as ctk
from PIL import Image

def tela_tracejada(frame):
    imagem_importar = ctk.CTkImage(
        light_image=Image.open("assets/imagens/importar_arquivos.png"),
        dark_image=Image.open("assets/imagens/importar_arquivos.png"),
        size=(100, 100),
        
    )
    label_imagem = ctk.CTkLabel(
    frame,
    image=imagem_importar,
    text="",
    fg_color=frame.cget("fg_color")
)
    label_imagem.place(x=296, y=50)
    texto_arrastar(frame)
    sub_texto_arrastar(frame)
    botao_selecionar(frame)
    


def texto_arrastar (frame):
    texto_principal = ctk.CTkLabel (
        master=frame,
        text="Arraste e Solte Os Arquivos da NF-e Aqui",
        text_color="white",
        font=("Arial", 26, "bold"),
    )

    texto_principal.place(x=110, y= 150)

def sub_texto_arrastar(frame):
    sub_texto_arrastar = ctk.CTkLabel(
        frame,
        text="Ou Clique No Botão Abaixo Para Selecionar.",
        text_color="grey",
        font=("Arial", 14),

    )
    sub_texto_arrastar.place(x=215, y=180)

def botao_selecionar(frame):
    imagem_pasta = ctk.CTkImage(
        light_image=Image.open("assets/imagens/imagem_pasta.png"),
        dark_image=Image.open("assets/imagens/imagem_pasta.png"),
        size=(30 , 30),
    )

    botao_pasta = ctk.CTkButton(
        frame,
        text= "Selecionar Arquivos",
        image=imagem_pasta,
        compound="left",
        width=130,
        height=50,
        fg_color="#1357C5",
        hover_color="#1B58DD",
        text_color="white",
        font=("Arial", 15, "bold")
    )
    botao_pasta.place(x=250, y=220)