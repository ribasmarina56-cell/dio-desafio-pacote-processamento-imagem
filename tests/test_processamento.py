import numpy as np

from processamento_imagem.processamento.combinar import (
    encontrar_diferenca,
    transferir_histograma,
)
from processamento_imagem.processamento.transformar import redimensionar_imagem


def test_redimensionar_imagem():
    image = np.zeros((100, 80, 3), dtype=float)
    result = redimensionar_imagem(image, 0.5)
    assert result.shape == (50, 40, 3)


def test_encontrar_diferenca_imagens_iguais():
    image = np.ones((32, 32), dtype=float)
    result = encontrar_diferenca(image, image)
    assert result.shape == image.shape
    assert np.all(result == 0)


def test_transferir_histograma_rgb():
    image1 = np.zeros((16, 16, 3), dtype=float)
    image2 = np.ones((16, 16, 3), dtype=float)
    result = transferir_histograma(image1, image2)
    assert result.shape == image1.shape
