import matplotlib.pyplot as plt


def plot_image(image):
    """Exibe uma imagem."""
    plt.figure(figsize=(8, 5))
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def plot_result(*images):
    """Exibe uma ou mais imagens lado a lado para comparação."""
    if not images:
        raise ValueError("É necessário fornecer pelo menos uma imagem.")

    number_images = len(images)
    fig, axes = plt.subplots(
        nrows=1,
        ncols=number_images,
        figsize=(4 * number_images, 4),
        squeeze=False,
    )
    axes = axes[0]

    names = [f"Image{i}" for i in range(1, number_images)] + ["Result"]
    for axis, name, image in zip(axes, names, images):
        axis.set_title(name)
        axis.imshow(image, cmap="gray")
        axis.axis("off")

    fig.tight_layout()
    plt.show()


def plot_histogram(image):
    """Exibe o histograma de uma imagem em tons de cinza ou RGB."""
    if image.ndim == 2:
        plt.figure(figsize=(8, 4))
        plt.hist(image.ravel(), bins=256, alpha=0.8)
        plt.title("Histograma")
        plt.xlabel("Intensidade")
        plt.ylabel("Frequência")
        plt.tight_layout()
        plt.show()
        return

    if image.ndim == 3 and image.shape[-1] >= 3:
        fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
        for index, axis in enumerate(axes):
            axis.set_title(f"Histograma canal {index + 1}")
            axis.hist(image[..., index].ravel(), bins=256, alpha=0.8)
            axis.set_xlabel("Intensidade")
            axis.set_ylabel("Frequência")
        fig.tight_layout()
        plt.show()
        return

    raise ValueError("Formato de imagem não suportado.")
