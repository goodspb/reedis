import json
from abc import ABC

from PySide6.QtCore import Qt, QModelIndex

from core.redis_data_handler.redis_data_handler import RedisDataHandler


class StreamHandler(RedisDataHandler, ABC):

    def update_content(self, key: str, *args, **kw):
        model = self.window.ui.contentTable.model()

        self.window.ui.maxLabel.show()
        self.window.ui.maxLineEdit.show()
        self.window.ui.minLabel.show()
        self.window.ui.minLineEdit.show()
        self.window.ui.stackedContents.setCurrentIndex(2)
        # stream does not support pagination
        self.window.ui.loadMoreContentButton.setDisabled(True)
        lst = self.r.xrange(key, self.window.ui.minLineEdit.text(), self.window.ui.maxLineEdit.text())
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

    def delete_content(self, key: str, current_index, current_data, *args, **kw):
        stream_id_index = self.window.ui.contentTable.model().index(current_index.row(), 0)
        stream_id = self.window.ui.contentTable.model().data(stream_id_index)
        print(f"stream_id: {stream_id}")
        self.r.xdel(key, stream_id)

    def edit_content(self, key: str, index: QModelIndex, *args, **kw):
        return
