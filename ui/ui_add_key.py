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
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddKeyDialog(object):
    def setupUi(self, AddKeyDialog):
        if not AddKeyDialog.objectName():
            AddKeyDialog.setObjectName(u"AddKeyDialog")
        AddKeyDialog.resize(293, 131)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddKeyDialog.sizePolicy().hasHeightForWidth())
        AddKeyDialog.setSizePolicy(sizePolicy)
        AddKeyDialog.setMinimumSize(QSize(293, 131))
        AddKeyDialog.setMaximumSize(QSize(293, 131))
        self.verticalLayout_2 = QVBoxLayout(AddKeyDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(AddKeyDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.keyNameInput = QLineEdit(AddKeyDialog)
        self.keyNameInput.setObjectName(u"keyNameInput")

        self.horizontalLayout.addWidget(self.keyNameInput)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(AddKeyDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.keyTypeList = QComboBox(AddKeyDialog)
        self.keyTypeList.addItem(u"string")
        self.keyTypeList.addItem(u"hash")
        self.keyTypeList.addItem(u"list")
        self.keyTypeList.addItem(u"set")
        self.keyTypeList.addItem(u"zset")
        self.keyTypeList.addItem("")
        self.keyTypeList.setObjectName(u"keyTypeList")

        self.horizontalLayout_2.addWidget(self.keyTypeList)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(AddKeyDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(AddKeyDialog)
        self.buttonBox.accepted.connect(AddKeyDialog.accept)
        self.buttonBox.rejected.connect(AddKeyDialog.reject)

        QMetaObject.connectSlotsByName(AddKeyDialog)
    # setupUi

    def retranslateUi(self, AddKeyDialog):
        AddKeyDialog.setWindowTitle(QCoreApplication.translate("AddKeyDialog", u"Add Key", None))
        self.label.setText(QCoreApplication.translate("AddKeyDialog", u"Key Name:", None))
        self.label_2.setText(QCoreApplication.translate("AddKeyDialog", u"Key Type:", None))
        self.keyTypeList.setItemText(5, QCoreApplication.translate("AddKeyDialog", u"stream", None))

    # retranslateUi

