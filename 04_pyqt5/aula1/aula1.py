"""
PyQT é um toolkit desenvolvido em C++ utilizado por vários programas para criação de aplicações GUI (Interface Gráfica).
Também inclui diversas funcionalidades, como: acesso a base de dados, threads, comunicação de rede, etc...

Comando de instalação do pacote:
pip install PyQt5
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do Botão')
        self.btn.setStyleSheet('font-size: 40px;')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(self.acaoBotao)

        self.setCentralWidget(self.cw)

    def acaoBotao(self):
        print('Olá, mundo!')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec()