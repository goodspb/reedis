import json
import pickle
from abc import ABC

from PySide6.QtCore import QModelIndex

from redis_handler.redis_data_handler.redis_data_handler import RedisDataHandler


class StringHandler(RedisDataHandler, ABC):

    def update_content(self, key: str, *args, **kw):
        self.window.ui.stackedContents.setCurrentIndex(1)
        content = self.r.get(key)
        content_str = content.decode('utf-8', errors='ignore')
        print(f"key_click string value {content_str}, size: {len(content_str)}")
        self.window.ui.sizeLabel.setText(f"Size: {len(content_str)}")
        content_type = self.window.ui.contentTypeList.currentText()
        print(f"content type: {content_type}")
        try:
            if content_type == 'Json':
                content_str = json.dumps(json.loads(content_str), indent=4)
            elif content_type == 'Django':
                content_str = pickle.loads(content)
        except Exception as err:
            print("content type convert error", err)
        self.window.ui.contentStrEdit.setText(content_str)

    def delete_content(self, key: str, *args, **kw):
        return

    def edit_content(self, key: str, index: QModelIndex, *args, **kw):
        return
