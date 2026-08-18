import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def _to_gray(image):
    """Converte uma imagem RGB/RGBA para escala de cinza."""
    if image.ndim == 2:
        return image
    if image.ndim == 3 and image.shape[-1] in (3, 4):
        return rgb2gray(image[..., :3])
    raise ValueError("Formato de imagem não suportado.")


def encontrar_diferenca(image1, image2):
    """Compara duas imagens usando similaridade estrutural (SSIM).

    As imagens precisam ter o mesmo formato. O resultado é uma matriz
    normalizada entre 0 e 1, na qual valores menores indicam maior diferença.
    """
    if not isinstance(image1, np.ndarray) or not isinstance(image2, np.ndarray):
        raise TypeError("image1 e image2 devem ser numpy.ndarray.")

    if image1.shape != image2.shape:
        raise ValueError("Informe duas imagens com o mesmo formato.")

    gray_image1 = _to_gray(image1)
    gray_image2 = _to_gray(image2)

    data_range = max(
        float(np.max(gray_image1)), float(np.max(gray_image2))
    ) - min(float(np.min(gray_image1)), float(np.min(gray_image2)))
    if data_range == 0:
        data_range = 1.0

    score, dif_image = structural_similarity(
        gray_image1,
        gray_image2,
        full=True,
        data_range=data_range,
    )

    print(f"Similaridade das imagens: {score:.4f}")

    min_value = float(np.min(dif_image))
    max_value = float(np.max(dif_image))
    if max_value == min_value:
        return np.zeros_like(dif_image, dtype=float)

    return (dif_image - min_value) / (max_value - min_value)


def transferir_histograma(image1, image2):
    """Transfere o histograma de ``image2`` para ``image1``."""
    if not isinstance(image1, np.ndarray) or not isinstance(image2, np.ndarray):
        raise TypeError("image1 e image2 devem ser numpy.ndarray.")

    if image1.ndim != image2.ndim:
        raise ValueError("As imagens precisam ter o mesmo número de dimensões.")

    if image1.ndim == 3:
        if image1.shape[-1] not in (3, 4) or image2.shape[-1] not in (3, 4):
            raise ValueError("Imagens coloridas devem ter 3 ou 4 canais.")
        if image1.shape[-1] != image2.shape[-1]:
            raise ValueError("As imagens coloridas precisam ter o mesmo número de canais.")
        channel_axis = -1
    elif image1.ndim == 2:
        channel_axis = None
    else:
        raise ValueError("Formato de imagem não suportado.")

    return match_histograms(image1, image2, channel_axis=channel_axis)
