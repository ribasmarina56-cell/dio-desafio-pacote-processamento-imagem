from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="dio-desafio-pacote-processamento-imagem",
    version="0.0.11",
    author="Marina Ribas",
    description="Pacote Python para processamento e manipulação de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ribasmarina56-cell/dio-desafio-pacote-processamento-imagem",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)


