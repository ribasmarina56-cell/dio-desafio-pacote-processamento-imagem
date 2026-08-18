from skimage.io import imread, imsave


def ler_imagem(path, is_gray=False):
    """Carrega uma imagem a partir de um arquivo."""
    return imread(path, as_gray=is_gray)


def salvar_imagem(image, path):
    """Salva uma imagem em um arquivo."""
    imsave(path, image)
