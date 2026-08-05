import os

from editor_pdf import adicionar_lote

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QProgressBar
)
from PyQt6.QtCore import Qt

from style import ESTILO_JANELA, BOTAO_VERDE, BOTAO_AZUL


class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.caminho_pdf = ""

        self.setWindowTitle("Numerador de Etiquetas PDF")
        self.setGeometry(300, 200, 600, 300)

        self.setStyleSheet(ESTILO_JANELA)

        self.criar_interface()

    def criar_interface(self):

        layout_principal = QVBoxLayout()

        # Título
        titulo = QLabel("NUMERADOR DE ETIQUETAS PDF")
        titulo.setFixedHeight(60)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("""
            QLabel{
                background-color:#1565C0;
                color:white;
                font-size:22px;
                font-weight:bold;
                border-radius:8px;
            }
        """)

        layout_principal.addWidget(titulo)

        # Campo PDF
        layout_pdf = QHBoxLayout()

        self.edit_pdf = QLineEdit()
        self.edit_pdf.setReadOnly(True)

        botao_pdf = QPushButton("Selecionar PDF")
        botao_pdf.setStyleSheet(BOTAO_VERDE)
        botao_pdf.setFixedHeight(40)
        botao_pdf.clicked.connect(self.selecionar_pdf)

        layout_pdf.addWidget(self.edit_pdf)
        layout_pdf.addWidget(botao_pdf)

        layout_principal.addLayout(layout_pdf)

        # Campo lote
        label_lote = QLabel("Número do Lote")

        self.edit_lote = QLineEdit()
        self.edit_lote.setPlaceholderText("Ex: 15")

        layout_principal.addWidget(label_lote)
        layout_principal.addWidget(self.edit_lote)

        # Barra de progresso
        self.barra = QProgressBar()
        self.barra.setValue(0)

        layout_principal.addWidget(self.barra)

        # Status
        self.label_status = QLabel("Aguardando...")
        layout_principal.addWidget(self.label_status)

        # Mensagem de sucesso
        self.label_mensagem = QLabel("")
        self.label_mensagem.setWordWrap(True)
        self.label_mensagem.hide()

        self.label_mensagem.setStyleSheet("""
        QLabel{
            background-color:#E8F5E9;
            color:#2E7D32;
            border:1px solid #A5D6A7;
            border-radius:6px;
            padding:8px;
            font-size:10pt;
        }
        """)

        layout_principal.addWidget(self.label_mensagem)

        # Botão gerar
        self.botao_gerar = QPushButton("GERAR PDF")
        self.botao_gerar.setStyleSheet(BOTAO_AZUL)
        self.botao_gerar.setFixedHeight(45)
        self.botao_gerar.clicked.connect(self.gerar_pdf)

        layout_principal.addWidget(self.botao_gerar)

        self.setLayout(layout_principal)

    def selecionar_pdf(self):

        arquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar PDF",
            "",
            "Arquivos PDF (*.pdf)"
        )

        if arquivo:
            self.caminho_pdf = arquivo
            self.edit_pdf.setText(arquivo)

    def gerar_pdf(self):

        if not self.caminho_pdf:
            QMessageBox.warning(
                self,
                "Aviso",
                "Selecione um arquivo PDF."
            )
            return

        lote = self.edit_lote.text().strip()

        if not lote:
            QMessageBox.warning(
                self,
                "Aviso",
                "Digite o número do lote."
            )
            return

        try:

            self.label_status.setText("Gerando PDF...")
            self.barra.setValue(30)

            pasta = os.path.dirname(self.caminho_pdf)

            nome = os.path.basename(self.caminho_pdf)
            nome_sem_extensao = os.path.splitext(nome)[0]

            pdf_saida = os.path.join(
                pasta,
                f"{nome_sem_extensao}_LOTE_{lote}.pdf"
            )

            adicionar_lote(
                self.caminho_pdf,
                pdf_saida,
                lote
            )

            self.barra.setValue(100)

            self.label_status.setText("PDF gerado com sucesso!")

            self.label_mensagem.setText(
                f"✅ PDF gerado com sucesso!\n\n"
                f"📄 Arquivo salvo em:\n{pdf_saida}"
            )

            self.label_mensagem.show()

            # Limpar os campos
            self.edit_pdf.clear()
            self.edit_lote.clear()
            self.caminho_pdf = ""

            self.edit_pdf.setFocus()

        except Exception as erro:

            QMessageBox.critical(
                self,
                "Erro",
                str(erro)
            )

            self.label_status.setText("Erro.")
            self.barra.setValue(0)