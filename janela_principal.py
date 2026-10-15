
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
    QProgressBar,
    QGroupBox
)

from PyQt6.QtCore import Qt, QTimer

from style import ESTILO_JANELA, BOTAO_VERDE, BOTAO_AZUL


class JanelaPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        self.caminho_pdf = ""

        self.setWindowTitle("Numerador de Etiquetas PDF")
        self.resize(950, 650)
        self.setMinimumSize(750, 550)

        self.setStyleSheet(ESTILO_JANELA)

        self.criar_interface()

    def criar_interface(self):

        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(25, 20, 25, 20)
        layout_principal.setSpacing(18)

        # =====================================
        # CABEÇALHO
        # =====================================

        titulo = QLabel("NUMERADOR DE ETIQUETAS PDF")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setFixedHeight(75)

        titulo.setStyleSheet("""
            QLabel {
                background-color: #1565C0;
                color: white;
                font-size: 23px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        layout_principal.addWidget(titulo)

        subtitulo = QLabel(
            "Selecione seu arquivo PDF e informe o número do lote."
        )
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitulo.setStyleSheet("""
            QLabel {
                color: #64748B;
                font-size: 11pt;
                background: transparent;
            }
        """)

        layout_principal.addWidget(subtitulo)

        # =====================================
        # SELEÇÃO DO PDF
        # =====================================

        grupo_pdf = QGroupBox("  1. ARQUIVO PDF  ")
        layout_pdf_grupo = QVBoxLayout()
        layout_pdf_grupo.setSpacing(12)

        descricao_pdf = QLabel(
            "Escolha o arquivo PDF que deseja numerar:"
        )
        layout_pdf_grupo.addWidget(descricao_pdf)

        linha_pdf = QHBoxLayout()

        self.edit_pdf = QLineEdit()
        self.edit_pdf.setReadOnly(True)
        self.edit_pdf.setPlaceholderText(
            "Nenhum arquivo PDF selecionado..."
        )
        self.edit_pdf.setMinimumHeight(45)

        botao_pdf = QPushButton("SELECIONAR PDF")
        botao_pdf.setStyleSheet(BOTAO_VERDE)
        botao_pdf.setMinimumHeight(45)
        botao_pdf.setMinimumWidth(170)
        botao_pdf.clicked.connect(self.selecionar_pdf)

        linha_pdf.addWidget(self.edit_pdf, 1)
        linha_pdf.addWidget(botao_pdf)

        layout_pdf_grupo.addLayout(linha_pdf)
        grupo_pdf.setLayout(layout_pdf_grupo)

        layout_principal.addWidget(grupo_pdf)

        # =====================================
        # NÚMERO DO LOTE
        # =====================================

        grupo_lote = QGroupBox("  2. NUMERAÇÃO DO LOTE  ")
        layout_lote = QVBoxLayout()
        layout_lote.setSpacing(12)

        descricao_lote = QLabel(
            "Informe o número que será aplicado nas etiquetas:"
        )

        layout_lote.addWidget(descricao_lote)

        self.edit_lote = QLineEdit()
        self.edit_lote.setPlaceholderText("Exemplo: 15")
        self.edit_lote.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.edit_lote.setMinimumHeight(55)

        self.edit_lote.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: #1565C0;
                border: 2px solid #CBD5E1;
                border-radius: 8px;
                padding: 8px;
                font-size: 20px;
                font-weight: bold;
            }

            QLineEdit:focus {
                border: 2px solid #1565C0;
            }
        """)

        layout_lote.addWidget(self.edit_lote)

        grupo_lote.setLayout(layout_lote)

        layout_principal.addWidget(grupo_lote)

        # =====================================
        # PROCESSAMENTO
        # =====================================

        grupo_progresso = QGroupBox("  3. PROCESSAMENTO  ")
        layout_progresso = QVBoxLayout()
        layout_progresso.setSpacing(12)

        self.label_status = QLabel(
            "Aguardando seleção do arquivo..."
        )

        self.label_status.setStyleSheet("""
            QLabel {
                color: #64748B;
                font-weight: bold;
                background: transparent;
            }
        """)

        layout_progresso.addWidget(self.label_status)

        self.barra = QProgressBar()
        self.barra.setValue(0)
        self.barra.setMinimumHeight(24)
        self.barra.setTextVisible(True)

        layout_progresso.addWidget(self.barra)

        grupo_progresso.setLayout(layout_progresso)

        layout_principal.addWidget(grupo_progresso)

        # =====================================
        # MENSAGEM DE SUCESSO
        # =====================================

        self.label_mensagem = QLabel("")
        self.label_mensagem.setWordWrap(True)
        self.label_mensagem.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.label_mensagem.setStyleSheet("""
            QLabel {
                background-color: #E8F5E9;
                color: #2E7D32;
                border: 1px solid #A5D6A7;
                border-radius: 8px;
                padding: 12px;
                font-size: 10pt;
                font-weight: bold;
            }
        """)

        self.label_mensagem.hide()

        layout_principal.addWidget(self.label_mensagem)

        # =====================================
        # ESPAÇO FLEXÍVEL
        # =====================================

        layout_principal.addStretch()

        # =====================================
        # BOTÃO GERAR PDF
        # =====================================

        self.botao_gerar = QPushButton(
            "GERAR PDF NUMERADO"
        )

        self.botao_gerar.setStyleSheet("""
            QPushButton {
                background-color: #1565C0;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 15px;
                font-size: 13pt;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1976D2;
            }

            QPushButton:pressed {
                background-color: #0D47A1;
            }

            QPushButton:disabled {
                background-color: #94A3B8;
            }
        """)

        self.botao_gerar.setMinimumHeight(60)
        self.botao_gerar.clicked.connect(self.gerar_pdf)

        layout_principal.addWidget(self.botao_gerar)

        self.setLayout(layout_principal)

    # =====================================
    # SELECIONAR PDF
    # =====================================

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

            self.label_mensagem.hide()
            self.label_status.setText(
                "Arquivo PDF selecionado. Informe o número do lote."
            )

            self.barra.setValue(0)

    # =====================================
    # GERAR PDF
    # =====================================

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
            self.edit_lote.setFocus()
            return

        try:

            self.botao_gerar.setEnabled(False)

            self.label_mensagem.hide()

            self.label_status.setText(
                "Processando arquivo PDF..."
            )

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

            self.label_status.setText(
                "PDF gerado com sucesso!"
            )

            self.label_mensagem.setText(
                f"PDF GERADO COM SUCESSO!\n\n"
                f"Arquivo salvo em:\n{pdf_saida}"
            )

            self.label_mensagem.show()

            QTimer.singleShot(
                5000,
                self.limpar_mensagem
            )

            # Limpar campos

            self.edit_pdf.clear()
            self.edit_lote.clear()

            self.caminho_pdf = ""

            self.edit_pdf.setFocus()

        except Exception as erro:

            QMessageBox.critical(
                self,
                "Erro ao gerar PDF",
                str(erro)
            )

            self.label_status.setText(
                "Não foi possível gerar o PDF."
            )

            self.barra.setValue(0)

        finally:

            self.botao_gerar.setEnabled(True)

    # =====================================
    # LIMPAR MENSAGEM
    # =====================================

    def limpar_mensagem(self):

        self.label_mensagem.hide()

        self.label_status.setText(
            "Aguardando novo PDF..."
        )

        self.barra.setValue(0)
