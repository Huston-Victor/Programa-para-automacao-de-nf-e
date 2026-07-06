import fitz
from tkinter import filedialog as fd


def selecionar_arquivo():
    arquivo = fd.askopenfilename(
        title="Selecione um PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    return arquivo

def extrair_texto_pdf(arquivo):
    doc = fitz.open(arquivo)

    texto = ""

    for pagina in doc:
        texto += pagina.get_text()

    doc.close()

    return texto

arquivo = selecionar_arquivo()

if arquivo:
    texto = extrair_texto_pdf(arquivo)
    print(texto)
else:
    print("Nenhum arquivo selecionado.")

linhas = texto.split("\n")

for numero, linha in enumerate(linhas):
    print(f"{numero}: {linha}")

