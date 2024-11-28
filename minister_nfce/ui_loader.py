from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
import os

def load_ui(filename):
    ui_file_name = os.path.join(os.path.dirname(__file__), filename)
    print(ui_file_name)
    ui_file = QFile(ui_file_name)
    print(ui_file)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    return window

