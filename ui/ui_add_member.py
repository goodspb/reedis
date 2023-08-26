# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_member.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QTextEdit, QWidget)

class Ui_AddMemberDialog(object):
    def setupUi(self, AddMemberDialog):
        if not AddMemberDialog.objectName():
            AddMemberDialog.setObjectName(u"AddMemberDialog")
        AddMemberDialog.resize(423, 400)
        self.gridLayout = QGridLayout(AddMemberDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fieldLayout = QHBoxLayout()
        self.fieldLayout.setObjectName(u"fieldLayout")
        self.label = QLabel(AddMemberDialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.fieldLayout.addWidget(self.label)

        self.FieldInput = QLineEdit(AddMemberDialog)
        self.FieldInput.setObjectName(u"FieldInput")

        self.fieldLayout.addWidget(self.FieldInput)

        self.fieldLayout.setStretch(0, 1)
        self.fieldLayout.setStretch(1, 5)

        self.gridLayout.addLayout(self.fieldLayout, 0, 0, 1, 1)

        self.scoreLayout = QHBoxLayout()
        self.scoreLayout.setObjectName(u"scoreLayout")
        self.label_2 = QLabel(AddMemberDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.scoreLayout.addWidget(self.label_2)

        self.ScoreInput = QLineEdit(AddMemberDialog)
        self.ScoreInput.setObjectName(u"ScoreInput")

        self.scoreLayout.addWidget(self.ScoreInput)

        self.scoreLayout.setStretch(0, 1)
        self.scoreLayout.setStretch(1, 5)

        self.gridLayout.addLayout(self.scoreLayout, 1, 0, 1, 1)

        self.idLayout = QHBoxLayout()
        self.idLayout.setObjectName(u"idLayout")
        self.label_4 = QLabel(AddMemberDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4.setWordWrap(False)

        self.idLayout.addWidget(self.label_4)

        self.IdInput = QLineEdit(AddMemberDialog)
        self.IdInput.setObjectName(u"IdInput")

        self.idLayout.addWidget(self.IdInput)

        self.idLayout.setStretch(0, 1)
        self.idLayout.setStretch(1, 5)

        self.gridLayout.addLayout(self.idLayout, 2, 0, 1, 1)

        self.valueLayout = QHBoxLayout()
        self.valueLayout.setObjectName(u"valueLayout")
        self.label_3 = QLabel(AddMemberDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.valueLayout.addWidget(self.label_3)

        self.ValueTextEdit = QTextEdit(AddMemberDialog)
        self.ValueTextEdit.setObjectName(u"ValueTextEdit")

        self.valueLayout.addWidget(self.ValueTextEdit)

        self.valueLayout.setStretch(0, 1)
        self.valueLayout.setStretch(1, 5)

        self.gridLayout.addLayout(self.valueLayout, 3, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(AddMemberDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)


        self.retranslateUi(AddMemberDialog)
        self.buttonBox.accepted.connect(AddMemberDialog.accept)
        self.buttonBox.rejected.connect(AddMemberDialog.reject)

        QMetaObject.connectSlotsByName(AddMemberDialog)
    # setupUi

    def retranslateUi(self, AddMemberDialog):
        AddMemberDialog.setWindowTitle(QCoreApplication.translate("AddMemberDialog", u"Add Member", None))
        self.label.setText(QCoreApplication.translate("AddMemberDialog", u"Field: ", None))
        self.label_2.setText(QCoreApplication.translate("AddMemberDialog", u"Score: ", None))
        self.label_4.setText(QCoreApplication.translate("AddMemberDialog", u"ID:", None))
        self.IdInput.setText(QCoreApplication.translate("AddMemberDialog", u"*", None))
        self.label_3.setText(QCoreApplication.translate("AddMemberDialog", u"Value:", None))
    # retranslateUi

