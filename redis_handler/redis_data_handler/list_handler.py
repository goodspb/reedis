from abc import ABC

from PySide6.QtCore import QModelIndex

from redis_handler.redis_data_handler.redis_data_handler import RedisDataHandler


class ListHandler(RedisDataHandler, ABC):

    def update_content(self, key: str, *args, **kw):
        count = kw.get("count", 100)
        model = self.window.ui.contentTable.model()
        self.window.ui.stackedContents.setCurrentIndex(2)
        if self.window.current_cursor == -1:
            return
        lst = self.r.lrange(key, self.window.current_cursor, self.window.current_cursor + count - 1)
        if len(lst) == count:
            self.window.current_cursor += count
        else:
            self.window.ui.loadMoreContentButton.setDisabled(True)
            self.window.current_cursor = -1
        print(f"key_click, redis_list_index: {self.window.current_cursor}, list value: {lst}")
        model.setHorizontalHeaderLabels(['Value'])
        index = model.rowCount()
        for item in lst:
            model.insertRow(index)
            model.setData(model.index(index, 0), item.decode('utf-8', errors='ignore'))
            index += 1

    def delete_content(self, key: str, current_index, current_data, *args, **kw):
        self.r.lrem(key, current_index.row(), self.r.lindex(key, current_index.row()))

    def edit_content(self, key: str, index: QModelIndex, *args, **kw):
        self.r.lset(key, index.row(), index.data())
