# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contact.ui'
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
    QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ContactDialog(object):
    def setupUi(self, ContactDialog):
        if not ContactDialog.objectName():
            ContactDialog.setObjectName(u"ContactDialog")
        ContactDialog.resize(362, 139)
        self.verticalLayout = QVBoxLayout(ContactDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(ContactDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(ContactDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(ContactDialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(ContactDialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(ContactDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ContactDialog)
        self.buttonBox.accepted.connect(ContactDialog.accept)
        self.buttonBox.rejected.connect(ContactDialog.reject)

        QMetaObject.connectSlotsByName(ContactDialog)
    # setupUi

    def retranslateUi(self, ContactDialog):
        ContactDialog.setWindowTitle(QCoreApplication.translate("ContactDialog", u"Contact", None))
        self.label_2.setText(QCoreApplication.translate("ContactDialog", u"Project Address", None))
        self.label.setText(QCoreApplication.translate("ContactDialog", u"<a href='https://github.com/goodspb/reedis'>https://github.com/goodspb/reedis</a>", None))
        self.label_3.setText(QCoreApplication.translate("ContactDialog", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("ContactDialog", u"<html><head/><body><p><a href=\"mailto:goodspb.luo@gmail.com\"><span style=\" text-decoration: underline; color:#094fd1;\">goodspb.luo@gmail.com</span></a></p></body></html>", None))
    # retranslateUi

