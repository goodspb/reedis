import sys
from PySide6.QtWidgets import QDialog, QMessageBox, QLayout, QWidget, QSpacerItem, QFileDialog

from database import get_connection, add_or_edit_connections, Connection
from ui.ui_add_or_edit_connection import Ui_AddOrEditConnectionDialog


class AddOrEditConnectionDialog(QDialog):
    def __init__(self, connection_id=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddOrEditConnectionDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.save_connection_clicked)
        self.show_widget_number = 0
        self._show_line()
        self._show_or_hide_layout(self.ui.sshWidget)
        self._show_or_hide_layout(self.ui.sslWidget)
        self._show_or_hide_layout(self.ui.sentinelWidget)
        self.ui.sshCheckBox.stateChanged.connect(self.ssh_checked)
        self.ui.sslCheckBox.stateChanged.connect(self.ssl_checked)
        self.ui.sentinelCheckBox.stateChanged.connect(self.sentinel_checked)
        self.ui.sshPrivateKeyToolButton.clicked.connect(self.ssh_private_key_clicked)
        self.ui.sslPublicKeylToolButton.clicked.connect(self.ssl_public_key_clicked)
        self.ui.sslPrivateKeyToolButton.clicked.connect(self.ssl_private_key_clicked)
        self.ui.sslAuthorityToolButton.clicked.connect(self.ssl_authority_clicked)
        print(f"connection_id: {connection_id}")
        self.current_connection = get_connection(connection_id)
        print(f"current_connection: {self.current_connection}")
        self._init_data()

    def _init_data(self):
        if not self.current_connection:
            return
        current_connection = self.current_connection
        self.ui.hostEdit.setText(current_connection.host)
        self.ui.portEdit.setText(str(current_connection.port))
        self.ui.usernameEdit.setText(current_connection.username)
        self.ui.passwordEdit.setText(current_connection.password)
        self.ui.sshCheckBox.setChecked(current_connection.ssh)
        self.ui.sslCheckBox.setChecked(current_connection.ssl)
        self.ui.sentinelCheckBox.setChecked(current_connection.sentinel)
        self.ui.clusterCheckBox.setChecked(current_connection.cluster)
        self.ui.readonlyCheckBox.setChecked(current_connection.readonly)

        self.ui.sshHostEdit.setText(current_connection.ssh_host)
        self.ui.sshPortEdit.setText(current_connection.ssh_port)
        self.ui.sshUsernameEdit.setText(current_connection.ssh_username)
        self.ui.sshPasswordEdit.setText(current_connection.ssh_password)
        self.ui.sshPrivateKeyLineEdit.setText(current_connection.ssh_private_key)
        self.ui.sshPassphraseEdit.setText(current_connection.ssh_passphrase)
        self.ui.sshTimeoutEdit.setText(str(current_connection.ssh_timeout))

        self.ui.sslPrivateKeylineEdit.setText(current_connection.ssl_public_key)
        self.ui.sslPrivateKeylineEdit.setText(current_connection.ssl_private_key)
        self.ui.sslAuthorityLineEdit.setText(current_connection.ssl_authority)

        self.ui.sentinelMasterGroupNameEdit.setText(current_connection.sentinel_master_group_name)
        self.ui.sentinelRedisNodePasswordEdit.setText(current_connection.sentinel_redis_node_password)

    def _show_or_hide_layout(self, w: QWidget, hide=True):
        if hide:
            w.hide()
            self.show_widget_number = max(self.show_widget_number - 1, 0)
            return
        w.show()
        self.show_widget_number = self.show_widget_number + 1

    def _show_line(self):
        self.ui.line.show() if self.show_widget_number > 0 else self.ui.line.hide()

    def ssh_checked(self, v):
        # v == 2 means: checked
        self._show_or_hide_layout(self.ui.sshWidget, v != 2)
        self._show_line()

    def ssl_checked(self, v):
        self._show_or_hide_layout(self.ui.sslWidget, v != 2)
        self._show_line()

    def sentinel_checked(self, v):
        self._show_or_hide_layout(self.ui.sentinelWidget, v != 2)
        self._show_line()

    def save_connection_clicked(self):
        current_connection = self.current_connection
        is_create = not current_connection
        if not current_connection:
            current_connection = Connection()

        current_connection.host = self.ui.hostEdit.text()
        current_connection.port = self.ui.portEdit.text()
        current_connection.username = self.ui.usernameEdit.text()
        current_connection.password = self.ui.passwordEdit.text()
        current_connection.ssh = self.ui.sshCheckBox.isChecked()
        current_connection.ssl = self.ui.sslCheckBox.isChecked()
        current_connection.sentinel = self.ui.sentinelCheckBox.isChecked()
        current_connection.cluster = self.ui.clusterCheckBox.isChecked()
        current_connection.readonly = self.ui.readonlyCheckBox.isChecked()

        current_connection.ssh_host = self.ui.sshHostEdit.text()
        current_connection.ssh_port = self.ui.sshPortEdit.text()
        current_connection.ssh_username = self.ui.sshUsernameEdit.text()
        current_connection.ssh_password = self.ui.sshPasswordEdit.text()
        current_connection.ssh_private_key = self.ui.sshPrivateKeyLineEdit.text()
        current_connection.ssh_passphrase = self.ui.sshPassphraseEdit.text()
        current_connection.ssh_timeout = int(self.ui.sshTimeoutEdit.text())

        current_connection.ssl_public_key = self.ui.sslPrivateKeylineEdit.text()
        current_connection.ssl_private_key = self.ui.sslPrivateKeylineEdit.text()
        current_connection.ssl_authority = self.ui.sslAuthorityLineEdit.text()

        current_connection.sentinel_master_group_name = self.ui.sentinelMasterGroupNameEdit.text()
        current_connection.sentinel_redis_node_password = self.ui.sentinelRedisNodePasswordEdit.text()

        res, error = add_or_edit_connections(current_connection, is_create)
        if res:
            self.close()
            self.parent().refresh_connections()
            QMessageBox.information(self, 'Alert', 'Success', QMessageBox.StandardButton.Ok)
            return
        print(error)
        QMessageBox.information(self, 'Alert', 'Failed', QMessageBox.StandardButton.Ok)

    def ssh_private_key_clicked(self):
        file_name = self._open_file_dialog("please select the private key")
        self.ui.sshPrivateKeyLineEdit.setText(file_name)

    def ssl_public_key_clicked(self):
        file_name = self._open_file_dialog("please select the public key")
        self.ui.sslPublicKeylLineEdit.setText(file_name)

    def ssl_private_key_clicked(self):
        file_name = self._open_file_dialog("please select the private key")
        self.ui.sslPrivateKeylineEdit.setText(file_name)

    def ssl_authority_clicked(self):
        file_name = self._open_file_dialog("please select the authority key")
        self.ui.sslAuthorityLineEdit.setText(file_name)

    def _open_file_dialog(self, title):
        platform = sys.platform
        print(f"platform: {platform}")
        path = './'
        if platform.startswith('linux'):
            path = '~/Downloads'
        elif platform.startswith('win'):
            path = 'C:/'
        elif platform.startswith('darwin'):
            path = '~/Downloads'
        file_path, _ = QFileDialog.getOpenFileName(self, title, path, "")
        return file_path
