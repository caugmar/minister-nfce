# File: main.py
import sys, os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QFile, QIODevice

class Aplicativo(QApplication):

    def __init__(self, arg):
        super().__init__(arg)
        ui_file_name = os.path.join(os.path.dirname(__file__), "main.ui")
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        if not self.window:
            print(loader.errorString())
            sys.exit(-1)
        self.window.actionSair.triggered.connect(self.saindo)
        self.window.buttonMensagem.clicked.connect(self.exibir_mensagem)
        self.window.show()

    def saindo(self):
        sys.exit(self.exec())

    def exibir_mensagem(self, s):
        dlg = QMessageBox(self.window)
        dlg.setWindowTitle("Olá!")
        dlg.setText("Olá para todo mundo!")
        button = dlg.exec()

if __name__ == "__main__":
    app = Aplicativo(sys.argv)
    app.exec()

