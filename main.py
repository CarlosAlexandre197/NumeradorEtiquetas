import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon, QFont
from janela_principal import JanelaPrincipal


def main():
    app = QApplication(sys.argv)

    # Ícone da aplicação
    app.setWindowIcon(QIcon("icone.ico"))

    # Fonte padrão em negrito
    fonte = QFont("Segoe UI", 10)
    fonte.setBold(True)
    app.setFont(fonte)

    janela = JanelaPrincipal()
    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()