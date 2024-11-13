# File: main.py
import sys, os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QFile, QIODevice
import webbrowser
from minister_nfce.relatorio import gerar

class Aplicativo:  # Mover de subclasse para composição

    def __init__(self):
        self.app = QApplication(sys.argv)
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
        self.window.actionDemonstracao.triggered.connect(self.exibir_relatorio_demonstracao)
        self.window.buttonMensagem.clicked.connect(self.exibir_mensagem)
        self.window.show()

    def saindo(self):
        sys.exit(self.app.exec())

    def exibir_mensagem(self, s):
        self.window.buttonMensagem.setText("Você me clicou!")
        dlg = QMessageBox(self.window)
        dlg.setWindowTitle("Olá!")
        nome = self.window.editNome.text().strip()
        dlg.setText("Olá para todo mundo!\nE olá para você, " + nome +
                    "!")
        resposta = dlg.exec()

    def exibir_relatorio_demonstracao(self, s):
        nome = gerar()
        webbrowser.open(nome)

if __name__ == "__main__":
    apl = Aplicativo()
    apl.app.exec()

