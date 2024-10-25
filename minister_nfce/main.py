from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt, Slot
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minister NFC-e")

        # Menu Bar
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # Menus
        menu_file = QMenu("Cadastros", self)
        menu_file.addAction("Produtos e Serviços")
        menu_file.addAction("Clientes [Opcional]")
        
        menu_edit = QMenu("Emissão", self)

        # Adding Menus to the MenuBar
        menu_bar.addMenu(menu_file)
        menu_bar.addMenu(menu_edit)

        # Main widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)

        # Input and output fields
        self.feet_entry = QLineEdit()
        self.feet_entry.setPlaceholderText("Enter feet")
        self.meters_label = QLabel("")

        # Calculate button
        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)

        # Labels
        layout.addWidget(QLabel("feet"))
        layout.addWidget(self.feet_entry)
        layout.addWidget(QLabel("is equivalent to"))
        layout.addWidget(self.meters_label)
        layout.addWidget(QLabel("meters"))
        layout.addWidget(calculate_button)

        # Add padding and alignment
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setAlignment(Qt.AlignTop)

    @Slot()
    def calculate(self):
        try:
            value = float(self.feet_entry.text())
            meters = round(0.3048 * value, 4)
            self.meters_label.setText(str(meters))
        except ValueError:
            self.meters_label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
