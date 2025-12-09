
------
# Projeto: Processamento de Imagens — Trab_Final

Este projeto reúne scripts para baixar imagens, aplicar filtros e manipular arquivos de imagem por meio de uma interface simples. Foi desenvolvido como trabalho final da disciplina de Laboratório de Programação (P3).

## Estrutura
- `download.py`: Faz o download de uma imagem a partir de uma URL e salva localmente.
- `Filtros.py`: Implementa filtros e transformações na imagem carregada. (ex.: escala de cinza, negativo, brilho/contraste, blur, etc.).
- `imagem.py`: Classe imagem para ser utilizada no resto do programa.
- `inteface.py`: Interface principal (GUI) que integra download e filtros para uso pelo usuário.
- `download_temp.png`: Arquivo temporário/resultado gerado por `download.py` (pode variar).

## Pré-requisitos
- Python 3.8+
- Bibliotecas utilizadas:
  - `Pillow` (PIL) para manipulação de imagens
  - `requests` para download de arquivos
  - `tkinter` para a GUI

Instale as dependências:

```zsh
pip install pillow requests
```

## Uso
### 1) Interface principal
Execute a interface integrada.
```zsh
python3 inteface.py
```
### 2) Carregando imagens
Para carregar as imagens para aplicar o filtro, ou selecione uma dentro do seu dispositivo com o botão de "Selecionar Arquivo" ou copie o URL da imagem na caixa.
Selecione "Carregar Imagem" para carregar ela.

### 3) Adicionando Filtros
Selecione o filtro que quer aplicar e aperte o botão de aplicar.
Para o blur, pode escolher a intensidade.
Imagem resultante é salva na pasta do programa.

## Licença
Projeto acadêmico destinado ao aprendizado. Verifique o repositório principal para políticas específicas.
