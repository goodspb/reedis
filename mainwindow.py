# This Python file uses the following encoding: utf-8
import json
import pickle
import sys

from PySide6.QtCore import QStringListModel, QModelIndex, Qt, QPoint
from PySide6.QtGui import QStandardItemModel, QAction, QCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QMenu, QHeaderView

from database import get_connections, get_connection, delete_connection
from dialog.add_member_dialog import AddMemberDialog
from dialog.add_or_edit_connection_dialog import AddOrEditConnectionDialog
from dialog.add_key_dialog import AddKeyDialog
from redis_handler import get_redis_connection, get_dbs, get_keys
from ui.ui_main import Ui_MainWindow


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic main.ui -o ui_form.py, or
#     pyside2-uic main.ui -o ui_form.py


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.connectButton.clicked.connect(self.connect_button_clicked)
        self.ui.addButton.clicked.connect(self.add_or_edit_button_clicked)
        self.ui.editButton.clicked.connect(self.add_or_edit_button_clicked)
        self.ui.deleteButton.clicked.connect(self.delete_button_clicked)
        self.ui.saveContentButton.clicked.connect(self.save_content_clicked)
        self.ui.refreshContentButton.clicked.connect(self.refresh_content_clicked)
        self.ui.loadMoreKeyButton.clicked.connect(self.load_more_key_clicked)
        self.ui.loadMoreContentButton.clicked.connect(self.load_more_content_clicked)
        self.ui.addKeyButton.clicked.connect(self.add_or_edit_key_clicked)
        self.ui.refreshKeysButton.clicked.connect(self.refresh_key_clicked)
        self.refresh_connections()
        self.ui.dbList.activated.connect(self.db_list_selected)
        self.ui.searchInput.returnPressed.connect(self._search_input_key)

        self.ui.keyList.clicked.connect(self.key_click)
        self.ui.keyList.doubleClicked.connect(self.key_double_clicked)
        self.ui.keyList.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.keyList.customContextMenuRequested[QPoint].connect(self.key_list_menu)
        key_list_model = QStringListModel()
        key_list_model.dataChanged.connect(self.key_edited)
        self.ui.keyList.setModel(key_list_model)
        self.key_list_cursor = 0

        self.ui.contentTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.contentTable.customContextMenuRequested[QPoint].connect(self.table_content_list_menu)
        self.ui.contentTable.doubleClicked.connect(self.table_content_double_clicked)
        content_table_model = QStandardItemModel()
        content_table_header = self.ui.contentTable.horizontalHeader()
        content_table_header.setSectionResizeMode(QHeaderView.Stretch)
        content_table_model.dataChanged.connect(self.table_content_edit)
        self.ui.contentTable.setModel(content_table_model)
        self.current_cursor=0

        self.ui.addMemberButton.clicked.connect(self.add_member_clicked)
        self.ui.contentTypeList.activated.connect(self.content_type_list_selected)
        self.ui.maxLabel.hide()
        self.ui.maxLineEdit.hide()
        self.ui.minLabel.hide()
        self.ui.minLineEdit.hide()
        self.ui.maxLineEdit.returnPressed.connect(self.stream_min_or_max_press)
        self.ui.minLineEdit.returnPressed.connect(self.stream_min_or_max_press)
        self.ui.scanSearchLineEdit.hide()
        self.ui.scanSearchLineEdit.returnPressed.connect(self.refresh_content_clicked)

        self.key_editing_old = None
        self.table_content_editing_old = None
        self.connected_redis = None
        self.shown_redis_key = None

    def refresh_connections(self):
        self.ui.connectionList.clear()
        connections = get_connections()
        if not connections:
            return
        for connection in connections:
            self.ui.connectionList.addItem(f"{connection.host}@{connection.port}", connection.id)

    def connect_button_clicked(self, s):
        print("connect_button_clicked", s)
        current_index = self.ui.connectionList.currentIndex()
        current_data = self.ui.connectionList.itemData(current_index)
        print(f"current_index: {current_index}, current_data: {current_data}")
        current_connection = get_connection(current_data)
        if not current_connection:
            QMessageBox.warning(self, 'Error', 'Can not connect to redis.', QMessageBox.StandardButton.Ok)
            return

        res, r = get_redis_connection(current_connection)
        if not res:
            QMessageBox.warning(self, 'Error', 'Can not connect to redis.', QMessageBox.StandardButton.Ok)
            return
        self.connected_redis = r

        db_count = get_dbs(r)
        print(f"db count:{db_count}")
        for db_idx in range(int(db_count)):
            self.ui.dbList.addItem(f"DB{db_idx}", db_idx)

        self._search_input_key()

    def add_or_edit_button_clicked(self):
        button = self.sender()
        print(button.text() + ' was clicked')
        connection_id = None
        if str(button.text()).lower() == 'edit':
            current_index = self.ui.connectionList.currentIndex()
            connection_id = self.ui.connectionList.itemData(current_index)
            print(f"add_or_edit_button_clicked, connection_id:{connection_id}")
        add_connection_dialog = AddOrEditConnectionDialog(connection_id=connection_id, parent=self)
        add_connection_dialog.exec()

    def delete_button_clicked(self, s):
        print("add_button_clicked", s)
        current_index = self.ui.connectionList.currentIndex()
        current_data = self.ui.connectionList.itemData(current_index)
        res = delete_connection(current_data)
        if not res:
            QMessageBox.warning(self, 'Error', 'Can not delete connection.', QMessageBox.StandardButton.Ok)
            return
        self.refresh_connections()
        QMessageBox.information(self, 'Success', 'delete connection successfully.', QMessageBox.StandardButton.Ok)

    def db_list_selected(self, index):
        if not self.connected_redis:
            return
        r = self.connected_redis
        dbs = get_dbs(r)
        print(f"db_list_selected index: {index}, dbs: {dbs}")
        if index >= int(dbs):
            return
        r.select(index)
        self._search_input_key()

    def _search_input_key(self, from_start=True):
        if not self.connected_redis:
            return
        model = self.ui.keyList.model()
        if from_start:
            # remove all rows
            model.removeRows(0, model.rowCount())
            self.key_list_cursor = 0
            self.ui.loadMoreKeyButton.setDisabled(False)
        r = self.connected_redis
        search_input = self.ui.searchInput.text()
        print(f"_search_input_key, key_list_cursor:{self.key_list_cursor} search_input: {search_input}")
        if self.key_list_cursor == -1:
            return
        new_cursor, keys = get_keys(r, self.key_list_cursor, f"*{search_input}*" if search_input else "*", 100)
        if new_cursor == 0:
            print(f"_search_input_key, end of the list")
            self.key_list_cursor = -1
            self.ui.loadMoreKeyButton.setDisabled(True)
        else:
            self.key_list_cursor = new_cursor
        index = model.rowCount()
        for key in keys:
            model.insertRow(index)
            model.setData(model.index(index), key)
            index += 1

    def key_click(self, index):
        if not self.connected_redis:
            return
        k = index.data()
        print(f"key_click key: {k}")
        r = self.connected_redis
        key_type = r.type(k)
        print(f"key_click type: {key_type}")
        key_type_str = key_type.decode('utf-8', errors='ignore')
        self.ui.typeShowInput.setText(key_type_str)
        self.shown_redis_key = {
            "key": k,
            "type": key_type_str
        }
        self._update_content(r, k, key_type_str)

    def key_double_clicked(self, index: QModelIndex):
        print(f"key_double_clicked: {index}")
        self.key_editing_old = index.data()

    def key_edited(self, index: QModelIndex):
        print(f"key_edited: {index}")
        if self.key_editing_old is None:
            return
        r = self.connected_redis
        if not r:
            return
        # rename
        r.rename(self.key_editing_old, index.data())
        # reset
        self.key_editing_old = None

    def key_list_menu(self, point):
        print(f"key_list_menu: {point}")
        popMenu = QMenu()
        popMenu.addAction(QAction(u'delete', self, triggered=self.key_delete))
        popMenu.exec(QCursor.pos())

    def key_delete(self):
        current_index = self.ui.keyList.currentIndex()
        current_data = self.ui.keyList.model().data(current_index)
        print(f"key_delete: {current_index}, {current_data}")
        r = self.connected_redis
        if not r:
            return
        r.delete(current_data)
        self._search_input_key()

    def _update_content(self, r, key, key_type, from_start=True):
        self.ui.maxLabel.hide()
        self.ui.maxLineEdit.hide()
        self.ui.minLabel.hide()
        self.ui.minLineEdit.hide()
        self.ui.scanSearchLineEdit.hide()

        ttl = r.ttl(key)
        print(f"key_click ttl: {ttl}")
        self.ui.ttlShowEditInput.setText(str(ttl))

        count = 100
        model = self.ui.contentTable.model()
        scan_search_keyword = self.ui.scanSearchLineEdit.text()
        scan_search_keyword = f"*{scan_search_keyword}*" if scan_search_keyword else "*"
        if from_start:
            # remove all rows
            model.removeRows(0, model.rowCount())
            model.removeColumns(0, model.columnCount())
            self.ui.loadMoreContentButton.setDisabled(False)
            self.current_cursor = 0
        if key_type == 'string':
            self.ui.stackedContents.setCurrentIndex(0)
            content = r.get(key)
            content_str = content.decode('utf-8', errors='ignore')
            print(f"key_click string value {content_str}, size: {len(content_str)}")
            self.ui.sizeLabel.setText(f"Size: {len(content_str)}")
            content_type = self.ui.contentTypeList.currentText()
            print(f"content type: {content_type}")
            try:
                if content_type == 'Json':
                    content_str = json.dumps(json.loads(content_str), indent=4)
                elif content_type == 'Django':
                    content_str = pickle.loads(content)
            except Exception as err:
                print("content type convert error", err)
            self.ui.contentStrEdit.setText(content_str)
        elif key_type == 'list':
            self.ui.stackedContents.setCurrentIndex(1)
            if self.current_cursor != -1:
                lst = r.lrange(key, self.current_cursor, self.current_cursor + count - 1)
                if len(lst) == count:
                    self.current_cursor += count
                else:
                    self.ui.loadMoreContentButton.setDisabled(True)
                    self.current_cursor = -1
                print(f"key_click, redis_list_index: {self.current_cursor}, list value: {lst}")
                model.setHorizontalHeaderLabels(['Value'])
                index = model.rowCount()
                for item in lst:
                    model.insertRow(index)
                    model.setData(model.index(index, 0), item.decode('utf-8', errors='ignore'))
                    index += 1
        elif key_type == 'hash':
            self.ui.scanSearchLineEdit.show()
            self.ui.stackedContents.setCurrentIndex(1)
            if self.current_cursor != -1:
                cursor, lst = r.hscan(key, self.current_cursor, scan_search_keyword, count)
                print(f"key_click hash value: {lst}, cursor: {cursor}")
                if cursor == 0:
                    self.current_cursor = -1
                    self.ui.loadMoreContentButton.setDisabled(True)
                else:
                    self.current_cursor = cursor
                model.setHorizontalHeaderLabels(['Key', 'Value'])
                index = model.rowCount()
                for k, v in lst.items():
                    model.insertRow(index)
                    model.setData(model.index(index, 0), k.decode('utf-8', errors='ignore'))
                    model.setData(model.index(index, 1), v.decode('utf-8', errors='ignore'))
                    index += 1
        elif key_type == 'set':
            self.ui.scanSearchLineEdit.show()
            self.ui.stackedContents.setCurrentIndex(1)
            if self.current_cursor != -1:
                cursor, lst = r.sscan(key, self.current_cursor, scan_search_keyword, count)
                print(f"key_click set value: {lst}, cursor: {cursor}")
                if cursor == 0:
                    self.current_cursor = -1
                    self.ui.loadMoreContentButton.setDisabled(True)
                else:
                    self.current_cursor = cursor
                model.setHorizontalHeaderLabels(['Value'])
                index = model.rowCount()
                for item in lst:
                    model.insertRow(index)
                    model.setData(model.index(index, 0), item.decode('utf-8', errors='ignore'))
                    index += 1
        elif key_type == 'zset':
            self.ui.scanSearchLineEdit.show()
            self.ui.stackedContents.setCurrentIndex(1)
            print(f"current_cursor: {self.current_cursor}, count:{count}")
            if self.current_cursor != -1:
                cursor, lst = r.zscan(key, self.current_cursor, scan_search_keyword, count)
                print(f"key_click zset value: {lst}, cursor: {cursor}")
                if cursor == 0:
                    self.current_cursor = -1
                    self.ui.loadMoreContentButton.setDisabled(True)
                else:
                    self.current_cursor = cursor
                model.setHorizontalHeaderLabels(['Score', 'Member'])
                index = model.rowCount()
                for item in lst:
                    member, score = item
                    model.insertRow(index)
                    model.setData(model.index(index, 0), member.decode('utf-8', errors='ignore'))
                    model.setData(model.index(index, 1), score)
                    index += 1
        elif key_type == 'stream':
            self.ui.maxLabel.show()
            self.ui.maxLineEdit.show()
            self.ui.minLabel.show()
            self.ui.minLineEdit.show()
            self.ui.stackedContents.setCurrentIndex(1)
            # stream does not support pagination
            self.ui.loadMoreContentButton.setDisabled(True)
            lst = r.xrange(key, self.ui.minLineEdit.text(), self.ui.maxLineEdit.text())
            print(f"key_click stream value: {lst}")
            model.setHorizontalHeaderLabels(['ID', 'Value'])
            index = 0
            for item in lst:
                stream_id, stream_value = item
                print(f"stream_id: {stream_id}, stream_value: {stream_value}")
                stream_value_dict_str = {k.decode('utf-8', errors='ignore'): v.decode('utf-8', errors='ignore')
                                         for k, v in stream_value.items()}
                model.insertRow(index)
                model.setData(model.index(index, 0), stream_id.decode('utf-8', errors='ignore'))
                model_item = model.item(index, 0)
                model_item.setFlags(model_item.flags() & ~Qt.ItemIsEditable)
                model.setData(model.index(index, 1), json.dumps(stream_value_dict_str))
                model_item2 = model.item(index, 1)
                model_item2.setFlags(model_item2.flags() & ~Qt.ItemIsEditable)
                index += 1

    def load_more_content_clicked(self):
        r = self.connected_redis
        redis_key = self.shown_redis_key
        if not r or not redis_key:
            return
        self._update_content(r, redis_key['key'], redis_key['type'], False)

    def save_content_clicked(self):
        r = self.connected_redis
        redis_key = self.shown_redis_key
        if not r or not redis_key:
            return
        print(f"save_content_clicked redis_key: {redis_key}")
        # set ttl
        ttl_text = self.ui.ttlShowEditInput.text()
        print(f"text ttl:{ttl_text}")
        if ttl_text != '-1' and not ttl_text.isdigit():
            QMessageBox.warning(self, 'Error', 'TTL must be digit.', QMessageBox.StandardButton.Ok)
            return
        ttl = int(ttl_text)
        # set Content if is String
        if redis_key["type"] == 'string':
            key_value = self.ui.contentStrEdit.toPlainText()
            print(f"key_value:{key_value}")
            if ttl != -1:
                r.set(redis_key["key"], key_value, ttl)
            else:
                r.set(redis_key["key"], key_value)
        else:  # set other keys
            if ttl != -1:
                r.expire(redis_key["key"], ttl)
            else:
                r.persist(redis_key["key"])

    def refresh_content_clicked(self):
        r = self.connected_redis
        redis_key = self.shown_redis_key
        if not r or not redis_key:
            return
        self._update_content(r, redis_key['key'], redis_key['type'])

    def load_more_key_clicked(self):
        self._search_input_key(from_start=False)

    def add_or_edit_key_clicked(self):
        if not self.connected_redis:
            return
        r = self.connected_redis
        add_key_dialog = AddKeyDialog(r, parent=self)
        add_key_dialog.exec()

    def refresh_key_clicked(self):
        self._search_input_key()

    def add_member_clicked(self):
        r = self.connected_redis
        redis_key = self.shown_redis_key
        if not r or not redis_key:
            return
        add_member_dialog = AddMemberDialog(r, redis_key, parent=self)
        add_member_dialog.exec()

    def content_type_list_selected(self):
        self.refresh_content_clicked()

    def table_content_list_menu(self, point):
        print(f"table_content_list_menu: {point}")
        popMenu = QMenu()
        popMenu.addAction(QAction(u'copy', self, triggered=self.table_content_copy))
        popMenu.addAction(QAction(u'delete', self, triggered=self.table_content_delete))
        popMenu.exec(QCursor.pos())

    def table_content_copy(self):
        current_index = self.ui.contentTable.currentIndex()
        current_data = self.ui.contentTable.model().data(current_index)
        print(f"table_content_copy current index: {current_index}, current data: {current_data}")
        cb = app.clipboard()
        cb.setText(current_data)

    def table_content_delete(self):
        current_index: QModelIndex = self.ui.contentTable.currentIndex()
        current_data = self.ui.contentTable.model().data(current_index)
        print(f"table_content_delete current index: {current_index.row()}, current data: {current_data}")
        r = self.connected_redis
        redis_key = self.shown_redis_key
        if not r or not redis_key:
            return
        key = redis_key['key']
        key_type = redis_key['type']
        if key_type == 'list':
            r.lrem(key, current_index.row(), r.lindex(key, current_index.row()))
        elif key_type == 'hash':
            field_index = self.ui.contentTable.model().index(current_index.row(), 0)
            field = self.ui.contentTable.model().data(field_index)
            print(f"field: {field}")
            r.hdel(key, field)
        elif key_type == 'set':
            r.srem(key, current_data)
        elif key_type == 'zset':
            member_index = self.ui.contentTable.model().index(current_index.row(), 0)
            member = self.ui.contentTable.model().data(member_index)
            print(f"member: {member}")
            r.zrem(key, member)
        elif key_type == 'stream':
            stream_id_index = self.ui.contentTable.model().index(current_index.row(), 0)
            stream_id = self.ui.contentTable.model().data(stream_id_index)
            print(f"stream_id: {stream_id}")
            r.xdel(key, stream_id)
        self._update_content(r, key, key_type)

    def stream_min_or_max_press(self):
        self.refresh_content_clicked()

    def table_content_double_clicked(self, index: QModelIndex):
        print(f"table_content_double_clicked, row:{index.row()}, column: {index.column()}, data:{index.data()}")
        model = self.ui.contentTable.model()
        column_list = []
        for column in range(self.ui.contentTable.model().columnCount()):
            column_index = model.index(index.row(), column)
            column_list.append(model.data(column_index))
        self.table_content_editing_old = column_list
        print(f"table_content_editing_old: {self.table_content_editing_old}")

    def table_content_edit(self, index: QModelIndex):
        print(f"key_edited, row:{index.row()}, column: {index.column()}, data:{index.data()}")
        if self.table_content_editing_old is None:
            return
        r = self.connected_redis
        redis_key = self.shown_redis_key
        if not r or not redis_key:
            return
        key = redis_key['key']
        key_type = redis_key['type']
        model = self.ui.contentTable.model()
        if key_type == 'list':
            r.lset(key, index.row(), index.data())
        elif key_type == 'hash':
            field_index = model.index(index.row(), 0)
            field = model.data(field_index)
            value_index = model.index(index.row(), 1)
            value = model.data(value_index)
            print(f"field: {field}, value: {value}")
            # change field
            if index.column() == 0:
                # add new field
                r.hset(key, field, self.table_content_editing_old[1])
                # delete old field
                r.hdel(key, self.table_content_editing_old[0])
            # change value
            else:
                r.hset(key, field, value)
        elif key_type == 'set':
            # add new set
            r.sadd(key, index.data())
            # delete old set
            r.srem(key, self.table_content_editing_old[0])
        elif key_type == 'zset':
            member_index = model.index(index.row(), 0)
            member = model.data(member_index)
            score_index = model.index(index.row(), 1)
            score = model.data(score_index)
            print(f"member: {member}, score: {score}")
            # change member
            if index.column() == 0:
                # add new member
                r.zadd(key, {member: self.table_content_editing_old[1]})
                # delete old member
                r.zrem(key, self.table_content_editing_old[0])
            # change score
            else:
                r.zadd(key, {member: score})
        self.table_content_editing_old = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
