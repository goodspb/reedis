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
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_AddMemberDialog(object):
    def setupUi(self, AddMemberDialog):
        if not AddMemberDialog.objectName():
            AddMemberDialog.setObjectName(u"AddMemberDialog")
        AddMemberDialog.resize(413, 352)
        self.verticalLayout = QVBoxLayout(AddMemberDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.FieldLayout = QHBoxLayout()
        self.FieldLayout.setObjectName(u"FieldLayout")
        self.label = QLabel(AddMemberDialog)
        self.label.setObjectName(u"label")

        self.FieldLayout.addWidget(self.label)

        self.FieldInput = QLineEdit(AddMemberDialog)
        self.FieldInput.setObjectName(u"FieldInput")

        self.FieldLayout.addWidget(self.FieldInput)


        self.verticalLayout.addLayout(self.FieldLayout)

        self.ScoreLayout = QHBoxLayout()
        self.ScoreLayout.setObjectName(u"ScoreLayout")
        self.label_2 = QLabel(AddMemberDialog)
        self.label_2.setObjectName(u"label_2")

        self.ScoreLayout.addWidget(self.label_2)

        self.ScoreInput = QLineEdit(AddMemberDialog)
        self.ScoreInput.setObjectName(u"ScoreInput")

        self.ScoreLayout.addWidget(self.ScoreInput)


        self.verticalLayout.addLayout(self.ScoreLayout)

        self.IdLayout = QHBoxLayout()
        self.IdLayout.setObjectName(u"IdLayout")
        self.label_4 = QLabel(AddMemberDialog)
        self.label_4.setObjectName(u"label_4")

        self.IdLayout.addWidget(self.label_4)

        self.IdInput = QLineEdit(AddMemberDialog)
        self.IdInput.setObjectName(u"IdInput")

        self.IdLayout.addWidget(self.IdInput)


        self.verticalLayout.addLayout(self.IdLayout)

        self.ValueLayout = QHBoxLayout()
        self.ValueLayout.setObjectName(u"ValueLayout")
        self.label_3 = QLabel(AddMemberDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.ValueLayout.addWidget(self.label_3)

        self.ValueTextEdit = QTextEdit(AddMemberDialog)
        self.ValueTextEdit.setObjectName(u"ValueTextEdit")

        self.ValueLayout.addWidget(self.ValueTextEdit)


        self.verticalLayout.addLayout(self.ValueLayout)

        self.buttonBox = QDialogButtonBox(AddMemberDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddMemberDialog)
        self.buttonBox.accepted.connect(AddMemberDialog.accept)
        self.buttonBox.rejected.connect(AddMemberDialog.reject)

        QMetaObject.connectSlotsByName(AddMemberDialog)
    # setupUi

    def retranslateUi(self, AddMemberDialog):
        AddMemberDialog.setWindowTitle(QCoreApplication.translate("AddMemberDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddMemberDialog", u"Field: ", None))
        self.label_2.setText(QCoreApplication.translate("AddMemberDialog", u"Score: ", None))
        self.label_4.setText(QCoreApplication.translate("AddMemberDialog", u"ID:", None))
        self.IdInput.setText(QCoreApplication.translate("AddMemberDialog", u"*", None))
        self.label_3.setText(QCoreApplication.translate("AddMemberDialog", u"Value:", None))
    # retranslateUi

