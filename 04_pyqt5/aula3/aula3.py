"""
Comando para converter o arquivo do QtDesigner para o formato .py
pyuic5 design.ui -o design.py

Nenhuma modificação feita no arquivo gerado será salvo.
"""

import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class RedimensionarImagem(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_escolher_arquivo.clicked.connect(self.abrir_imagem)
        self.btn_redimensionar.clicked.connect(self.redimensionar)
        self.btn_salvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem',
            r'C:\Users\rober\Pictures'
        )
        self.input_abrir_arquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.label_img.setPixmap(self.original_img)
        self.input_largura.setText(str(self.original_img.width()))
        self.input_altura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.input_largura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.label_img.setPixmap(self.nova_imagem)
        self.input_largura.setText(str(self.nova_imagem.width()))
        self.input_altura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar imagem',
            r'C:\Users\rober\Pictures\imagem_redimensionada.png',
            filter="Images"
        )
        self.nova_imagem.save(imagem, 'PNG')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    redimensionar_imagem = RedimensionarImagem()
    redimensionar_imagem.show()
    qt.exec()
