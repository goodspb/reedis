from abc import ABC

from PySide6.QtCore import QModelIndex

from redis_handler.redis_data_handler.redis_data_handler import RedisDataHandler


class ZsetHandler(RedisDataHandler, ABC):

    def update_content(self, key: str, *args, **kw):
        count = kw.get("count", 100)
        scan_search_keyword = kw.get("scan_search_keyword")
        model = self.window.ui.contentTable.model()

        self.window.ui.scanSearchLineEdit.show()
        self.window.ui.stackedContents.setCurrentIndex(2)
        print(f"current_cursor: {self.window.current_cursor}, count:{count}")
        if self.window.current_cursor == -1:
            return
        cursor, lst = self.r.zscan(key, self.window.current_cursor, scan_search_keyword, count)
        print(f"key_click zset value: {lst}, cursor: {cursor}")
        if cursor == 0:
            self.window.current_cursor = -1
            self.window.ui.loadMoreContentButton.setDisabled(True)
        else:
            self.window.current_cursor = cursor
        model.setHorizontalHeaderLabels(['Score', 'Member'])
        index = model.rowCount()
        for item in lst:
            member, score = item
            model.insertRow(index)
            model.setData(model.index(index, 0), member.decode('utf-8', errors='ignore'))
            model.setData(model.index(index, 1), score)
            index += 1

    def delete_content(self, key: str, current_index, current_data, *args, **kw):
        member_index = self.window.ui.contentTable.model().index(current_index.row(), 0)
        member = self.window.ui.contentTable.model().data(member_index)
        print(f"member: {member}")
        self.r.zrem(key, member)

    def edit_content(self, key: str, index: QModelIndex, *args, **kw):
        model = self.window.ui.contentTable.model()
        member_index = model.index(index.row(), 0)
        member = model.data(member_index)
        score_index = model.index(index.row(), 1)
        score = model.data(score_index)
        print(f"member: {member}, score: {score}")
        # change member
        if index.column() == 0:
            # add new member
            self.r.zadd(key, {member: self.window.table_content_editing_old[1]})
            # delete old member
            self.r.zrem(key, self.window.table_content_editing_old[0])
        # change score
        else:
            self.r.zadd(key, {member: score})