from PySide6.QtWidgets import QDialog, QMessageBox
from redis.client import Redis

from ui.ui_add_key import Ui_AddKeyDialog


class AddKeyDialog(QDialog):
    def __init__(self, r: Redis, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddKeyDialog()
        self.ui.setupUi(self)
        self.r = r
        self.parent = parent
        self.ui.buttonBox.accepted.connect(self.save_key_clicked)

    def save_key_clicked(self):
        if not self.r:
            QMessageBox.warning(self, 'Error', 'Can\'t find redis connection.', QMessageBox.StandardButton.Ok)
            return
        key_name = self.ui.keyNameInput.text()
        key_type = self.ui.keyTypeList.currentText()
        print(f"key_name:{key_name}, key_type:{key_type}")
        if key_type == 'string':
            self.r.set(key_name, "New String")
        elif key_type == 'list':
            self.r.rpush(key_name, "New List")
        elif key_type == 'hash':
            self.r.hset(key_name, "New Hash", "NewValue")
        elif key_type == 'set':
            self.r.sadd(key_name, "New Set")
        elif key_type == 'zset':
            self.r.zadd(key_name, {"New ZSet": 1.0})
        # refresh key list
        self.parent._search_input_key()
