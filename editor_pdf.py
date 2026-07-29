import pymupdf as fitz


def adicionar_lote(pdf_entrada, pdf_saida, numero_lote):

    documento = fitz.open(pdf_entrada)

    for pagina in documento:

        # Caixa preta
        caixa = fitz.Rect(10, 10, 140, 35)

        pagina.draw_rect(
            caixa,
            color=(0, 0, 0),
            fill=(0, 0, 0)
        )

        # Texto branco
        pagina.insert_text(
            (20, 28),
            f"LOTE {numero_lote}",
            fontsize=14,
            fontname="helv",
            color=(1, 1, 1)
        )

    documento.save(pdf_saida)
    documento.close()