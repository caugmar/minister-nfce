from PySide6.QtWidgets import QApplication
from ui_loader import load_ui
from database import create_tables
import os, sys

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = load_ui("main_window.ui")
        self.window.show()
        self.setup_connections()

    def setup_connections(self):
        self.window.btnCadastrarProduto.clicked.connect(self.cadastrar_produto)
        self.window.btnEmitirNFCe.clicked.connect(self.emitir_nfce)

    def cadastrar_produto(self):
        # Lógica para cadastrar produtos
        pass

    def emitir_nfce(self):
        # Lógica para emitir NFCe
        pass

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    create_tables()
    app = MainApp()
    app.run()
