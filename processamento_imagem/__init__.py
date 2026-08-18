"""Pacote para processamento e manipulação de imagens."""

__version__ = "0.0.12"

from .processamento.combinar import encontrar_diferenca, transferir_histograma
from .processamento.transformar import redimensionar_imagem
from .utilidades.io import ler_imagem, salvar_imagem

__all__ = [
    "__version__",
    "encontrar_diferenca",
    "transferir_histograma",
    "redimensionar_imagem",
    "ler_imagem",
    "salvar_imagem",
]
