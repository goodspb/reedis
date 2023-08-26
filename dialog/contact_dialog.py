from PySide6.QtWidgets import QDialog

from ui.ui_contact import Ui_ContactDialog


class ContactDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ContactDialog()
        self.ui.setupUi(self)
