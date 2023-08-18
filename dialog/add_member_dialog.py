from PySide6.QtWidgets import QDialog, QMessageBox
from redis.client import Redis

from ui.ui_add_member import Ui_AddMemberDialog


class AddMemberDialog(QDialog):
    def __init__(self, r: Redis, shown_redis_key: dict, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddMemberDialog()
        self.ui.setupUi(self)
        self.r = r
        self.shown_redis_key = shown_redis_key
        self.parent = parent
        self.ui.buttonBox.accepted.connect(self.save_member_clicked)
        if not self.r or not self.shown_redis_key:
            QMessageBox.warning(self, 'Error', 'Can\'t find current redis key', QMessageBox.StandardButton.Ok)
            return
        self.key = self.shown_redis_key["key"]
        self.key_type = self.shown_redis_key["type"]
        if self.key_type == 'list':
            self._hide_field_layout()
            self._hide_score_layout()
        elif self.key_type == 'hash':
            self._hide_score_layout()
        elif self.key_type == 'set':
            self._hide_field_layout()
            self._hide_score_layout()
        elif self.key_type == 'zset':
            self._hide_field_layout()

    def _hide_field_layout(self):
        for i in range(self.ui.FieldLayout.count()):
            self.ui.FieldLayout.itemAt(i).widget().hide()

    def _hide_score_layout(self):
        for i in range(self.ui.ScoreLayout.count()):
            self.ui.ScoreLayout.itemAt(i).widget().hide()

    def save_member_clicked(self):
        field = self.ui.FieldInput.text()
        score = self.ui.ScoreInput.text()
        value = self.ui.ValueTextEdit.toPlainText()
        if self.key_type == 'list':
            self.r.rpush(self.key, value)
        elif self.key_type == 'hash':
            self.r.hset(self.key, field, value)
        elif self.key_type == 'set':
            self.r.sadd(self.key, value)
        elif self.key_type == 'zset':
            self.r.zadd(self.key, {value: score})
        self.parent._update_content(self.r, self.key, self.key_type)