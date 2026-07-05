from gui.frame_esquerdo import frame_e
from gui.base_troca_janela import base_troca
from gui.tela_importar import frame_importar
from utils.trocar_janelas import trocar_tela


def criar_tela_inicial(janela):

    frame_principal = base_troca(janela)
    frame_e(
        janela,
        lambda tela: trocar_tela(frame_principal, tela)
    )

    frame_importar(frame_principal)


