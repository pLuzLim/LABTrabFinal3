import requests

class Download:
    def __init__(self, link, endereco):
        self.link = link
        self.endereco = endereco

    def baixarArquivo(self):
        try:
            res = requests.get(self.link)
            res.raise_for_status()
            with open(self.endereco, "wb") as arquivo:
                arquivo.write(res.content)
            print("Download realizado com sucesso!")
        except requests.exceptions.MissingSchema:
            print("URL inválida.")
        except requests.exceptions.RequestException as e:
            print(f"Erro: {e}")
