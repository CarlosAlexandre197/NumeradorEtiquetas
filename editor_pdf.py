import pymupdf as fitz

def adicionar_lote(pdf_entrada, pdf_saida, numero_lote):

    doc = fitz.open(pdf_entrada)

    for pagina in doc:

        largura = pagina.rect.width
        altura = pagina.rect.height

        print(f"Largura: {largura}")
        print(f"Altura: {altura}")

        # TESTE DE RÉGUA
        for x in range(0, int(largura), 50):
            pagina.insert_text(
                (x, 50),
                f"X{x}",
                fontsize=12,
                color=(1, 0, 0)
            )

        for y in range(0, int(altura), 50):
            pagina.insert_text(
                (20, y),
                f"Y{y}",
                fontsize=12,
                color=(0, 0, 1)
            )

    doc.save(pdf_saida)
    doc.close()

    print("PDF criado com sucesso!")