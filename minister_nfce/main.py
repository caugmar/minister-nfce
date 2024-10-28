# File: main.py
import sys, os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

def obter_app():
    return QApplication(sys.argv)

def saindo():
    print("Saindo.")

def obter_janela():
    ui_file_name = os.path.join(os.path.dirname(__file__), "main.ui")
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.actionSair.triggered.connect(saindo)
    window.buttonMensagem.clicked.connect(saindo)
    return window

if __name__ == "__main__":
    app = obter_app()
    window = obter_janela()
    window.show()
    sys.exit(app.exec())

