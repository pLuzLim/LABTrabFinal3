from PIL import Image, ImageChops, ImageFilter, ImageOps


class PretoBranco:
    def aplicar_pb(imagem):
        limiar = 128
        escalaCinza = imagem.convert("L")
        imagemPretoBranco = escalaCinza.point(
            lambda x: 0 if x < limiar else 255, '1')
        return imagemPretoBranco


class EscalaCinza:
    def aplicar_cinza(imagem):
        imagemCinza = imagem.convert("L")
        return imagemCinza


class Contorno:
    def aplicar_contorno(imagem):
        escalaCinza = imagem.convert("L")
        contornoImagem = escalaCinza.filter(ImageFilter.FIND_EDGES)
        return contornoImagem


class Cartoon:
    def aplicar_cartoon(imagem):
        escalaCinza = imagem.convert("L")
        bordasImagem = escalaCinza.filter(ImageFilter.FIND_EDGES)
        bordasImagem = bordasImagem.point(lambda x: 0 if x < 40 else 255)
        bordasImagem = ImageOps.invert(bordasImagem)

        suavizacao = imagem.filter(ImageFilter.MedianFilter(size=7))
        pintura = suavizacao.quantize(colors=32).convert("RGB")

        bordasRgb = bordasImagem.convert("RGB")
        imagemCartoon = ImageChops.multiply(pintura, bordasRgb)

        return imagemCartoon


class Negativo:
    def aplicar_negativo(imagem):
        if imagem.mode == "RGBA":
            imagemBranca = Image.new("RGB", imagem.size, (255, 255, 255))
            imagemBranca.paste(imagem, mask=imagem.split()[3])
            imagem = imagemBranca
        else:
            imagem = imagem.convert("RGB")

        imagemNegativa = ImageOps.invert(imagem)
        return imagemNegativa


class Blurred:
    def aplicar_blurred(imagem, intensidade):
        imagemBorrada = imagem.filter(
            ImageFilter.GaussianBlur(radius=intensidade))
        return imagemBorrada
