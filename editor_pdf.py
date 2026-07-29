import pymupdf as fitz


def adicionar_lote(pdf_entrada, pdf_saida, numero_lote):

    doc = fitz.open(pdf_entrada)

    for pagina in doc:

        largura = pagina.rect.width
        altura = pagina.rect.height

        print(f"Largura: {largura}")
        print(f"Altura : {altura}")
        

        # Marca os quatro cantos
        pagina.insert_text((10, 20), "A", fontsize=20, color=(1, 0, 0))
        pagina.insert_text((largura - 20, 20), "B", fontsize=20, color=(0, 1, 0))
        pagina.insert_text((10, altura - 20), "C", fontsize=20, color=(0, 0, 1))
        pagina.insert_text((largura - 20, altura - 20), "D", fontsize=20, color=(1, 0, 1))

    doc.save(pdf_saida)
    doc.close()
