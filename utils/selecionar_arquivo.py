from tkinter import filedialog as fd

def selecionar_arquivo():
    arquivo = fd.askopenfilename(
        title="Selecione um arquivo",
        filetypes=[("Arquivos PDF", "*.pdf")],
    )
    return arquivo
