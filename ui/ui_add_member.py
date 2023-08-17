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
        AddMemberDialog.resize(407, 299)
        self.gridLayout = QGridLayout(AddMemberDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.FieldLayout = QHBoxLayout()
        self.FieldLayout.setObjectName(u"FieldLayout")
        self.label = QLabel(AddMemberDialog)
        self.label.setObjectName(u"label")

        self.FieldLayout.addWidget(self.label)

        self.FieldInput = QLineEdit(AddMemberDialog)
        self.FieldInput.setObjectName(u"FieldInput")

        self.FieldLayout.addWidget(self.FieldInput)


        self.gridLayout.addLayout(self.FieldLayout, 0, 0, 1, 1)

        self.ScoreLayout = QHBoxLayout()
        self.ScoreLayout.setObjectName(u"ScoreLayout")
        self.label_2 = QLabel(AddMemberDialog)
        self.label_2.setObjectName(u"label_2")

        self.ScoreLayout.addWidget(self.label_2)

        self.ScoreInput = QLineEdit(AddMemberDialog)
        self.ScoreInput.setObjectName(u"ScoreInput")

        self.ScoreLayout.addWidget(self.ScoreInput)


        self.gridLayout.addLayout(self.ScoreLayout, 1, 0, 1, 1)

        self.ValueLayout = QHBoxLayout()
        self.ValueLayout.setObjectName(u"ValueLayout")
        self.label_3 = QLabel(AddMemberDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.ValueLayout.addWidget(self.label_3)

        self.ValueTextEdit = QTextEdit(AddMemberDialog)
        self.ValueTextEdit.setObjectName(u"ValueTextEdit")

        self.ValueLayout.addWidget(self.ValueTextEdit)


        self.gridLayout.addLayout(self.ValueLayout, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(AddMemberDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)


        self.retranslateUi(AddMemberDialog)
        self.buttonBox.accepted.connect(AddMemberDialog.accept)
        self.buttonBox.rejected.connect(AddMemberDialog.reject)

        QMetaObject.connectSlotsByName(AddMemberDialog)
    # setupUi

    def retranslateUi(self, AddMemberDialog):
        AddMemberDialog.setWindowTitle(QCoreApplication.translate("AddMemberDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddMemberDialog", u"Field: ", None))
        self.label_2.setText(QCoreApplication.translate("AddMemberDialog", u"Score: ", None))
        self.label_3.setText(QCoreApplication.translate("AddMemberDialog", u"Value:", None))
    # retranslateUi

