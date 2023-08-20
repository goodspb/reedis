# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_key.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSplitter, QWidget)

class Ui_AddKeyDialog(object):
    def setupUi(self, AddKeyDialog):
        if not AddKeyDialog.objectName():
            AddKeyDialog.setObjectName(u"AddKeyDialog")
        AddKeyDialog.resize(295, 129)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddKeyDialog.sizePolicy().hasHeightForWidth())
        AddKeyDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(AddKeyDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(AddKeyDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.keyNameInput = QLineEdit(AddKeyDialog)
        self.keyNameInput.setObjectName(u"keyNameInput")

        self.horizontalLayout.addWidget(self.keyNameInput)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.splitter = QSplitter(AddKeyDialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        self.splitter.addWidget(self.label_2)
        self.keyTypeList = QComboBox(self.splitter)
        self.keyTypeList.addItem(u"string")
        self.keyTypeList.addItem(u"hash")
        self.keyTypeList.addItem(u"list")
        self.keyTypeList.addItem(u"set")
        self.keyTypeList.addItem(u"zset")
        self.keyTypeList.addItem("")
        self.keyTypeList.setObjectName(u"keyTypeList")
        self.splitter.addWidget(self.keyTypeList)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(AddKeyDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)


        self.retranslateUi(AddKeyDialog)
        self.buttonBox.accepted.connect(AddKeyDialog.accept)
        self.buttonBox.rejected.connect(AddKeyDialog.reject)

        QMetaObject.connectSlotsByName(AddKeyDialog)
    # setupUi

    def retranslateUi(self, AddKeyDialog):
        AddKeyDialog.setWindowTitle(QCoreApplication.translate("AddKeyDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddKeyDialog", u"Key Name:", None))
        self.label_2.setText(QCoreApplication.translate("AddKeyDialog", u"Key Type:", None))
        self.keyTypeList.setItemText(5, QCoreApplication.translate("AddKeyDialog", u"stream", None))

    # retranslateUi

