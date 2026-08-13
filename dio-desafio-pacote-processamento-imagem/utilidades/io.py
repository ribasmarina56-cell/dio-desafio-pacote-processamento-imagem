from skimage.io import imread, imsave


def ler_imagem(path, is_gray=False):
    """
    Carrega uma imagem a partir de um arquivo.

    Args:
        path (str): Caminho do arquivo da imagem.
        is_gray (bool): Se True, carrega a imagem em escala de cinza.

    Returns:
        numpy.ndarray: Imagem carregada.
    """
    return imread(path, as_gray=is_gray)


def salvar_imagem(image, path):
    """
    Salva uma imagem em um arquivo.

    Args:
        image (numpy.ndarray): Imagem que será salva.
        path (str): Caminho onde a imagem será salva.
    """
    imsave(path, image)