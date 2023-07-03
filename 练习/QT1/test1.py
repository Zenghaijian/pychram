from PySide6.QtWidgets import (QApplication, QDialog)
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QDialog()
    window.show()

    sys.exit(app.exec())
