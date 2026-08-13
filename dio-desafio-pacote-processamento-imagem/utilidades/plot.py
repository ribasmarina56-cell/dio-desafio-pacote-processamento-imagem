
    import matplotlib.pyplot as plt


def plot_image(image):
    """
    Exibe uma imagem.

    Args:
        image (numpy.ndarray): Imagem que será exibida.
    """
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def plot_result(*images):
    """
    Exibe uma ou mais imagens para comparação.

    Args:
        *images (numpy.ndarray): Imagens que serão exibidas.
    """
    if not images:
        raise ValueError("É necessário fornecer pelo menos uma imagem.")

    number_images = len(images)

    fig, axes = plt.subplots(
        nrows=1,
        ncols=number_images,
        figsize=(4 * number_images, 4)
    )

    if number_images == 1:
        axes = [axes]

    names = [f"Image{i}" for i in range(1, number_images)]
    names.append("Result")

    for axis, name, image in zip(axes, names, images):
        axis.set_title(name)
        axis.imshow(image, cmap="gray")
        axis.axis("off")

    fig.tight_layout()
    plt.show()


def plot_histogram(image):
    """
    Exibe o histograma de uma imagem.

    Para imagens coloridas RGB, exibe os histogramas dos canais
    vermelho, verde e azul. Para imagens em escala de cinza,
    exibe um único histograma.

    Args:
        image (numpy.ndarray): Imagem cujo histograma será exibido.
    """
    if image.ndim == 2:
        plt.figure(figsize=(8, 4))
        plt.hist(image.ravel(), bins=256, color="gray", alpha=0.8)
        plt.title("Histograma")
        plt.xlabel("Intensidade")
        plt.ylabel("Frequência")
        plt.tight_layout()
        plt.show()
        return

    if image.ndim == 3 and image.shape[2] >= 3:
        fig, axes = plt.subplots(
            nrows=1,
            ncols=3,
            figsize=(12, 4)
        )

        colors = ["red", "green", "blue"]

        for index, (axis, color) in enumerate(zip(axes, colors)):
            axis.set_title(f"Histograma {color}")
            axis.hist(
                image[:, :, index].ravel(),
                bins=256,
                color=color,
                alpha=0.8
            )
            axis.set_xlabel("Intensidade")
            axis.set_ylabel("Frequência")

        fig.tight_layout()
        plt.show()
        return

    raise ValueError("Formato de imagem não suportado.")