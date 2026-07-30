import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from janela_principal import JanelaPrincipal


def main():
    app = QApplication(sys.argv)

    # Ícone da aplicação
    app.setWindowIcon(QIcon("icone.ico.ico"))

    janela = JanelaPrincipal()
    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()