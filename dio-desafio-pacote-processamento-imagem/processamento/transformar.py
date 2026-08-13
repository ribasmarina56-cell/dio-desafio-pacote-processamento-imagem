from skimage.transform import resize


def redimensionar_imagem(image, proporcao):
    """
    Redimensiona uma imagem de acordo com uma proporção.

    Args:
        image (numpy.ndarray): Imagem que será redimensionada.
        proporcao (float): Proporção do novo tamanho da imagem.
            Deve estar entre 0 e 1.

    Returns:
        numpy.ndarray: Imagem redimensionada.

    Raises:
        ValueError: Se a proporção não estiver entre 0 e 1.
    """
    if not 0 < proporcao <= 1:
        raise ValueError(
            "Informe uma proporção maior que 0 e menor ou igual a 1."
        )

    height = round(image.shape[0] * proporcao)
    width = round(image.shape[1] * proporcao)

    imagem_redimensionada = resize(
        image,
        (height, width),
        anti_aliasing=True
    )

    return imagem_redimensionada