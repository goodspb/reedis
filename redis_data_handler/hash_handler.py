from abc import ABC

from PySide6.QtCore import QModelIndex

from redis_data_handler.redis_data_handler import RedisDataHandler


class HashHandler(RedisDataHandler, ABC):

    def update_content(self, key: str, *args, **kw):
        count = kw.get("count", 100)
        scan_search_keyword = kw.get("scan_search_keyword")
        model = self.window.ui.contentTable.model()

        self.window.ui.scanSearchLineEdit.show()
        self.window.ui.stackedContents.setCurrentIndex(1)
        if self.window.current_cursor == -1:
            return
        cursor, lst = self.r.hscan(key, self.window.current_cursor, scan_search_keyword, count)
        print(f"key_click hash value: {lst}, cursor: {cursor}")
        if cursor == 0:
            self.window.current_cursor = -1
            self.window.ui.loadMoreContentButton.setDisabled(True)
        else:
            self.window.current_cursor = cursor
        model.setHorizontalHeaderLabels(['Key', 'Value'])
        index = model.rowCount()
        for k, v in lst.items():
            model.insertRow(index)
            model.setData(model.index(index, 0), k.decode('utf-8', errors='ignore'))
            model.setData(model.index(index, 1), v.decode('utf-8', errors='ignore'))
            index += 1

    def delete_content(self, key: str, current_index, current_data, *args, **kw):
        field_index = self.window.ui.contentTable.model().index(current_index.row(), 0)
        field = self.window.ui.contentTable.model().data(field_index)
        print(f"field: {field}")
        self.r.hdel(key, field)

    def edit_content(self, key: str, index: QModelIndex, *args, **kw):
        model = self.window.ui.contentTable.model()
        field_index = model.index(index.row(), 0)
        field = model.data(field_index)
        value_index = model.index(index.row(), 1)
        value = model.data(value_index)
        print(f"field: {field}, value: {value}")
        # change field
        if index.column() == 0:
            # add new field
            self.r.hset(key, field, self.window.table_content_editing_old[1])
            # delete old field
            self.r.hdel(key, self.window.table_content_editing_old[0])
        # change value
        else:
            self.r.hset(key, field, value)
