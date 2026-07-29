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


class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.caminho_pdf = ""

        self.setWindowTitle("Numerador de Etiquetas PDF")
        self.setGeometry(300, 200, 600, 300)

        self.criar_interface()

    def criar_interface(self):

        layout_principal = QVBoxLayout()

        # Título
        titulo = QLabel("NUMERADOR DE ETIQUETAS")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

        layout_principal.addWidget(titulo)

        # Campo PDF
        layout_pdf = QHBoxLayout()

        self.edit_pdf = QLineEdit()
        self.edit_pdf.setReadOnly(True)

        botao_pdf = QPushButton("Selecionar PDF")
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

        # Botão gerar

        self.botao_gerar = QPushButton("GERAR PDF")
        self.botao_gerar.setFixedHeight(40)

        layout_principal.addWidget(self.botao_gerar)

        # Status

        self.label_status = QLabel("Aguardando...")

        layout_principal.addWidget(self.label_status)

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