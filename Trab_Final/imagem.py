import os
from PIL import Image


class Imagem:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.imagem = Image.open(endereco)

    def dimensoes(self):
        return self.imagem.size

    def tamanho(self):
        return os.path.getsize(self.endereco)

    def formato(self):
        return self.imagem.format

    def conteudo(self):
        return self.imagem

    def __str__(self):
        return f'Nome: {self.nome}\nDimensões: {self.dimensoes()}\nFormato: {self.formato()}\nTamanho: {self.tamanho()} Bytes'
