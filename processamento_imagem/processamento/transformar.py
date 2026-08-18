from skimage.transform import resize


def redimensionar_imagem(image, proporcao):
    """Redimensiona uma imagem mantendo sua proporção espacial.

    Args:
        image: Imagem representada por ``numpy.ndarray``.
        proporcao: Fator maior que 0 e menor ou igual a 1.

    Returns:
        numpy.ndarray: Imagem redimensionada.
    """
    if not 0 < proporcao <= 1:
        raise ValueError(
            "Informe uma proporção maior que 0 e menor ou igual a 1."
        )

    if getattr(image, "ndim", 0) < 2:
        raise ValueError("A imagem deve possuir pelo menos duas dimensões.")

    height = max(1, round(image.shape[0] * proporcao))
    width = max(1, round(image.shape[1] * proporcao))

    return resize(
        image,
        (height, width),
        anti_aliasing=True,
        preserve_range=True,
    )
