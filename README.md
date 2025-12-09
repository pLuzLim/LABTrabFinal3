## Para executar:
### Abra e execute o arquivo "inteface.py"
### Siga a interface para o resto.

- "Carregar Imagem" após inserir o link/escolher o arquivo.

### O resultado é salvo na mesma pasta.
------
# Projeto: Processamento de Imagens — Trab_Final

Este projeto reúne scripts para baixar imagens, aplicar filtros e manipular arquivos de imagem por meio de uma interface simples. Foi desenvolvido como trabalho final da disciplina de Laboratório de Programação (P3).

## Estrutura
- `download.py`: Faz o download de uma imagem a partir de uma URL e salva localmente.
- `Filtros.py`: Implementa filtros e transformações (ex.: escala de cinza, negativo, brilho/contraste, blur, etc.).
- `imagem.py`: Funções utilitárias para abrir, salvar e converter imagens; pode encapsular operações comuns.
- `inteface.py`: Interface principal (CLI/GUI) que integra download e filtros para uso pelo usuário.
- `download_temp.png`: Arquivo temporário/resultado gerado por `download.py` (pode variar).

## Pré-requisitos
- Python 3.8+
- Bibliotecas sugeridas:
  - `Pillow` (PIL) para manipulação de imagens
  - `requests` para download de arquivos

Instale as dependências (ajuste conforme necessário):

```zsh
python3 -m venv .venv
source .venv/bin/activate
pip install pillow requests
```

## Uso
### 1) Baixar uma imagem
Baixe uma imagem pela URL e salve em `download_temp.png`:
```zsh
python3 download.py --url "https://exemplo.com/arquivo.png" --out download_temp.png
```
Parâmetros comuns:
- `--url`: URL da imagem a ser baixada.
- `--out`: caminho do arquivo de saída (opcional; padrão pode ser `download_temp.png`).

### 2) Aplicar filtros
Aplique um filtro sobre uma imagem de entrada e salve a saída:
```zsh
python3 Filtros.py --input download_temp.png --filtro "grayscale" --out resultado.png
```
Exemplos de filtros (podem variar conforme implementação):
- `grayscale`
- `negative`
- `brightness --valor 20`
- `contrast --valor 15`
- `blur --raio 2`

### 3) Operações gerais de imagem
Utilize utilitários (caso disponíveis) para conversão ou ajustes:
```zsh
python3 imagem.py --input download_temp.png --op "resize" --largura 800 --altura 600 --out redimensionada.png
```

### 4) Interface principal
Execute a interface integrada para fluxo completo:
```zsh
python3 inteface.py
```
Dependendo da implementação, você poderá escolher baixar uma imagem, aplicar filtros e salvar resultados em sequência.

## Organização e boas práticas
- Mantenha as imagens de entrada/saída na pasta `Trab_Final` ou especifique caminhos completos.
- Evite sobrescrever arquivos sem necessidade; utilize `--out` para nomear resultados.
- Versione apenas código e exemplos mínimos; arquivos gerados podem ser grandes.

## Desenvolvimento
- Formatação sugerida: `black` e `flake8` (opcional).
- Testes rápidos podem ser feitos com imagens pequenas para acelerar a execução.

## Próximos passos
- Documentar todos os filtros disponíveis com parâmetros.
- Adicionar exemplos com imagens de exemplo e resultados.
- Opcional: criar interface gráfica com `tkinter` ou `PySimpleGUI`.

## Licença
Projeto acadêmico destinado ao aprendizado. Verifique o repositório principal para políticas específicas.
