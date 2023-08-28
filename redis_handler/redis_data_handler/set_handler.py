from abc import ABC

from PySide6.QtCore import QModelIndex

from redis_handler.redis_data_handler.redis_data_handler import RedisDataHandler


class SetHandler(RedisDataHandler, ABC):

    def update_content(self, key: str, *args, **kw):
        count = kw.get("count", 100)
        scan_search_keyword = kw.get("scan_search_keyword")
        model = self.window.ui.contentTable.model()

        self.window.ui.scanSearchLineEdit.show()
        self.window.ui.stackedContents.setCurrentIndex(2)
        if self.window.current_cursor == -1:
            return
        cursor, lst = self.r.sscan(key, self.window.current_cursor, scan_search_keyword, count)
        print(f"key_click set value: {lst}, cursor: {cursor}")
        if cursor == 0:
            self.window.current_cursor = -1
            self.window.ui.loadMoreContentButton.setDisabled(True)
        else:
            self.window.current_cursor = cursor
        model.setHorizontalHeaderLabels(['Value'])
        index = model.rowCount()
        for item in lst:
            model.insertRow(index)
            model.setData(model.index(index, 0), item.decode('utf-8', errors='ignore'))
            index += 1

    def delete_content(self, key: str, current_index, current_data, *args, **kw):
        self.r.srem(key, current_data)

    def edit_content(self, key: str, index: QModelIndex, *args, **kw):
        # add new set
        self.r.sadd(key, index.data())
        # delete old set
        self.r.srem(key, self.window.table_content_editing_old[0])
