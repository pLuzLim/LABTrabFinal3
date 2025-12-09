
------
# Projeto: Processamento de Imagens — Trab_Final

Este projeto reúne scripts para baixar imagens, aplicar filtros e manipular arquivos de imagem por meio de uma interface simples. Foi desenvolvido como trabalho final da disciplina de Laboratório de Programação (P3).

## Estrutura
- `download.py`: Classe para fazer downloads no programa principal.
- `Filtros.py`: Classes para aplicar os filtros na imagem no programa principal. (ex.: escala de cinza, negativo, brilho/contraste, blur, etc.).
- `imagem.py`: Classe imagem para ser utilizada no resto do programa.
- `inteface.py`: Interface principal (GUI) que integra download, filtros e imagem para uso pelo usuário.
- `download_temp.png`: Arquivo temporário/resultado gerado pelos testes iniciais.

## Pré-requisitos
- Python 3.8+
- Bibliotecas utilizadas:
  - `Pillow` (PIL) para manipulação de imagens
  - `requests` para download de arquivos
  - `tkinter` para a GUI

Instale as dependências:

```zsh
pip install pillow requests tkinter
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
