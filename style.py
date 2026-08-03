# style.py

COR_AZUL = "#1565C0"
COR_AZUL_HOVER = "#1976D2"
COR_AZUL_CLICK = "#0D47A1"

COR_VERDE = "#2E7D32"
COR_VERDE_HOVER = "#388E3C"

COR_FUNDO = "#F5F5F5"
COR_BRANCA = "#FFFFFF"

FONTE = "Segoe UI"

ESTILO_JANELA = """
QWidget {
    background-color: #F5F5F5;
    color: #212121;
    font-family: Segoe UI;
    font-size: 10pt;
}

QLabel {
    color: #212121;
}

QGroupBox {
    background: white;
    border: 1px solid #D0D0D0;
    border-radius: 8px;
    margin-top: 12px;
    font-weight: bold;
    color: #1565C0;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
}

QLineEdit {
    background: white;
    color: black;
    border: 1px solid #C5C5C5;
    border-radius: 6px;
    padding: 6px;
}

QProgressBar {
    border: 1px solid #C5C5C5;
    border-radius: 6px;
    text-align: center;
    color: black;
}

QProgressBar::chunk {
    background-color: #1565C0;
}
"""

BOTAO_AZUL = """
QPushButton{
    background:#1565C0;
    color:white;
    border:none;
    border-radius:6px;
    padding:8px;
    font-weight:bold;
}

QPushButton:hover{
    background:#1976D2;
}

QPushButton:pressed{
    background:#0D47A1;
}
"""

BOTAO_VERDE = """
QPushButton{
    background:#2E7D32;
    color:white;
    border:none;
    border-radius:6px;
    padding:8px;
    font-weight:bold;
}

QPushButton:hover{
    background:#388E3C;
}
"""