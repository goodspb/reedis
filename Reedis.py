import sys

from PySide6.QtWidgets import QApplication

from window.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow(app=app)
    widget.show()
    sys.exit(app.exec())
