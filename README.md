# processamento_imagem

Pacote Python para processamento e manipulação de imagens.

## Funcionalidades

### Processamento
- Comparação de histogramas.
- Similaridade estrutural com SSIM.
- Redimensionamento de imagens.

### Utilidades
- Carregar imagens.
- Salvar imagens.
- Exibir imagens.
- Exibir resultados para comparação.
- Exibir histogramas.

## Instalação

```bash
pip install dio-desafio-pacote-processamento-imagem
```

## Uso

```python
from processamento_imagem import (
    encontrar_diferenca,
    transferir_histograma,
    redimensionar_imagem,
    ler_imagem,
    salvar_imagem,
)

imagem1 = ler_imagem("imagem1.jpg")
imagem2 = ler_imagem("imagem2.jpg")

resultado = encontrar_diferenca(imagem1, imagem2)
imagem_ajustada = transferir_histograma(imagem1, imagem2)
imagem_menor = redimensionar_imagem(imagem1, 0.5)

salvar_imagem(imagem_ajustada, "resultado.jpg")
```

## Desenvolvimento

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute os testes:

```bash
python -m pytest
```

Para gerar os arquivos de distribuição:

```bash
python -m build
```

## Autor

Marina Ribas

## Licença

MIT
