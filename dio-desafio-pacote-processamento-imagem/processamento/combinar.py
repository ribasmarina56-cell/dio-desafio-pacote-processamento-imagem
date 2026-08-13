
import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def encontrar_diferenca(image1, image2):
    """
    Compara duas imagens utilizando similaridade estrutural (SSIM).

    As imagens precisam possuir o mesmo formato.

    Args:
        image1 (numpy.ndarray): Primeira imagem.
        image2 (numpy.ndarray): Segunda imagem.

    Returns:
        numpy.ndarray: Imagem normalizada com as diferenças estruturais.

    Raises:
        ValueError: Se as imagens tiverem formatos diferentes.
    """
    if image1.shape != image2.shape:
        raise ValueError(
            "Informe duas imagens com o mesmo formato."
        )

    # Converte imagens RGB para escala de cinza.
    if image1.ndim == 3:
        gray_image1 = rgb2gray(image1)
        gray_image2 = rgb2gray(image2)
    else:
        gray_image1 = image1
        gray_image2 = image2

    score, dif_image = structural_similarity(
        gray_image1,
        gray_image2,
        full=True,
        data_range=gray_image1.max() - gray_image1.min()
    )

    print(f"Similaridade das imagens: {score:.4f}")

    min_value = np.min(dif_image)
    max_value = np.max(dif_image)

    if max_value == min_value:
        return np.zeros_like(dif_image)

    dif_image_normalizado = (
        (dif_image - min_value) /
        (max_value - min_value)
    )

    return dif_image_normalizado


def transferir_histograma(image1, image2):
    """
    Transfere o histograma da segunda imagem para a primeira.

    Args:
        image1 (numpy.ndarray): Imagem que receberá o histograma.
        image2 (numpy.ndarray): Imagem de referência.

    Returns:
        numpy.ndarray: Imagem com o histograma ajustado.
    """
    imagem_correspondente = match_histograms(
        image1,
        image2,
        channel_axis=-1 if image1.ndim == 3 else None
    )

    return imagem_correspondente