from pathlib import Path
from setuptools import find_packages, setup

ROOT_DIR = Path(__file__).parent

with open(ROOT_DIR / "README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open(ROOT_DIR / "requirements.txt", encoding="utf-8") as f:
    requirements = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="dio-processamento-imagem-marina",
    version="0.0.12",
    author="Marina Ribas",
    description="Pacote Python para processamento e manipulação de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ribasmarina56-cell/dio-desafio-pacote-processamento-imagem",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
