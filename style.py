
# ==========================================
# ESTILOS - NUMERADOR DE ETIQUETAS PDF
# ==========================================

COR_AZUL = "#1565C0"
COR_AZUL_HOVER = "#1976D2"
COR_AZUL_CLICK = "#0D47A1"

COR_VERDE = "#2E7D32"
COR_VERDE_HOVER = "#388E3C"

COR_FUNDO = "#F1F5F9"
COR_BRANCA = "#FFFFFF"

COR_TEXTO = "#263238"
COR_CINZA = "#64748B"
COR_BORDA = "#DCE3EB"

FONTE = "Segoe UI"

ESTILO_JANELA = """
QWidget {
    background-color: #F1F5F9;
    color: #263238;
    font-family: 'Segoe UI';
    font-size: 10pt;
}

QLabel {
    color: #263238;
    background: transparent;
}

QGroupBox {
    background-color: #FFFFFF;
    border: 1px solid #DCE3EB;
    border-radius: 10px;
    margin-top: 18px;
    padding: 15px;
    font-weight: bold;
    color: #1565C0;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 8px;
    background-color: #FFFFFF;
}

QLineEdit {
    background-color: #FFFFFF;
    color: #263238;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    padding: 10px;
    selection-background-color: #1565C0;
}

QLineEdit:focus {
    border: 2px solid #1565C0;
}

QProgressBar {
    background-color: #E2E8F0;
    border: none;
    border-radius: 8px;
    height: 20px;
    text-align: center;
    color: #263238;
    font-weight: bold;
}

QProgressBar::chunk {
    background-color: #1565C0;
    border-radius: 8px;
}
"""

BOTAO_AZUL = """
QPushButton {
    background-color: #1565C0;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 11px 18px;
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
    color: #E2E8F0;
}
"""

BOTAO_VERDE = """
QPushButton {
    background-color: #2E7D32;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 11px 18px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #388E3C;
}

QPushButton:pressed {
    background-color: #1B5E20;
}

QPushButton:disabled {
    background-color: #94A3B8;
    color: #E2E8F0;
}
"""
