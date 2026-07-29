import pymupdf as fitz

# Posição da caixa
X = 395
Y = 8
LARGURA = 120
ALTURA = 28


def adicionar_lote(pdf_entrada, pdf_saida, numero_lote):

    documento = fitz.open(pdf_entrada)

    for pagina in documento:

        caixa = fitz.Rect(
            X,
            Y,
            X + LARGURA,
            Y + ALTURA
        )

        pagina.draw_rect(
            caixa,
            color=(0, 0, 0),
            fill=(0, 0, 0)
        )

        pagina.insert_text(
            (X + 12, Y + 20),
            f"LOTE {numero_lote}",
            fontsize=14,
            color=(1, 1, 1),
            fontname="helv"
        )

    documento.save(pdf_saida)
    documento.close()