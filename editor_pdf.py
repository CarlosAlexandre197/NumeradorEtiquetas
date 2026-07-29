import fitz  # PyMuPDF
import os


def adicionar_lote(pdf_entrada, pdf_saida, numero_lote):
    """
    Adiciona o texto 'LOTE X' em todas as páginas do PDF.
    """

    documento = fitz.open(pdf_entrada)

    for pagina in documento:

        # Desenha um retângulo preto
        retangulo = fitz.Rect(360, 10, 510, 40)

        pagina.draw_rect(
            retangulo,
            color=(0, 0, 0),
            fill=(0, 0, 0)
        )

        # Escreve o texto em branco
        pagina.insert_text(
            (380, 30),
            f"LOTE {numero_lote}",
            fontsize=16,
            color=(1, 1, 1),
            fontname="helv"
        )

    documento.save(pdf_saida)
    documento.close()