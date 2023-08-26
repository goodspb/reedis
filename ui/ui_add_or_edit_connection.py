# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_or_edit_connection.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_AddOrEditConnectionDialog(object):
    def setupUi(self, AddOrEditConnectionDialog):
        if not AddOrEditConnectionDialog.objectName():
            AddOrEditConnectionDialog.setObjectName(u"AddOrEditConnectionDialog")
        AddOrEditConnectionDialog.resize(444, 658)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddOrEditConnectionDialog.sizePolicy().hasHeightForWidth())
        AddOrEditConnectionDialog.setSizePolicy(sizePolicy)
        AddOrEditConnectionDialog.setModal(False)
        self.gridLayout = QGridLayout(AddOrEditConnectionDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.commonWedget = QWidget(AddOrEditConnectionDialog)
        self.commonWedget.setObjectName(u"commonWedget")
        self.verticalLayout_4 = QVBoxLayout(self.commonWedget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.commonWedget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.hostEdit = QLineEdit(self.commonWedget)
        self.hostEdit.setObjectName(u"hostEdit")

        self.horizontalLayout_2.addWidget(self.hostEdit)

        self.label_4 = QLabel(self.commonWedget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.usernameEdit = QLineEdit(self.commonWedget)
        self.usernameEdit.setObjectName(u"usernameEdit")

        self.horizontalLayout_2.addWidget(self.usernameEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.commonWedget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.portEdit = QLineEdit(self.commonWedget)
        self.portEdit.setObjectName(u"portEdit")
        self.portEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.portEdit)

        self.label_3 = QLabel(self.commonWedget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.passwordEdit = QLineEdit(self.commonWedget)
        self.passwordEdit.setObjectName(u"passwordEdit")

        self.horizontalLayout.addWidget(self.passwordEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sshCheckBox = QCheckBox(self.commonWedget)
        self.sshCheckBox.setObjectName(u"sshCheckBox")

        self.horizontalLayout_3.addWidget(self.sshCheckBox)

        self.sslCheckBox = QCheckBox(self.commonWedget)
        self.sslCheckBox.setObjectName(u"sslCheckBox")

        self.horizontalLayout_3.addWidget(self.sslCheckBox)

        self.sentinelCheckBox = QCheckBox(self.commonWedget)
        self.sentinelCheckBox.setObjectName(u"sentinelCheckBox")

        self.horizontalLayout_3.addWidget(self.sentinelCheckBox)

        self.clusterCheckBox = QCheckBox(self.commonWedget)
        self.clusterCheckBox.setObjectName(u"clusterCheckBox")

        self.horizontalLayout_3.addWidget(self.clusterCheckBox)

        self.readonlyCheckBox = QCheckBox(self.commonWedget)
        self.readonlyCheckBox.setObjectName(u"readonlyCheckBox")
        self.readonlyCheckBox.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.readonlyCheckBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.commonWedget, 0, 0, 1, 1)

        self.line = QFrame(AddOrEditConnectionDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.sshWidget = QWidget(AddOrEditConnectionDialog)
        self.sshWidget.setObjectName(u"sshWidget")
        self.verticalLayout_2 = QVBoxLayout(self.sshWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.sshWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(288, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.sshWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.sshHostEdit = QLineEdit(self.sshWidget)
        self.sshHostEdit.setObjectName(u"sshHostEdit")

        self.horizontalLayout_5.addWidget(self.sshHostEdit)

        self.label_7 = QLabel(self.sshWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.sshUsernameEdit = QLineEdit(self.sshWidget)
        self.sshUsernameEdit.setObjectName(u"sshUsernameEdit")

        self.horizontalLayout_5.addWidget(self.sshUsernameEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.sshWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.sshPortEdit = QLineEdit(self.sshWidget)
        self.sshPortEdit.setObjectName(u"sshPortEdit")
        self.sshPortEdit.setClearButtonEnabled(False)

        self.horizontalLayout_6.addWidget(self.sshPortEdit)

        self.label_9 = QLabel(self.sshWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.sshPasswordEdit = QLineEdit(self.sshWidget)
        self.sshPasswordEdit.setObjectName(u"sshPasswordEdit")

        self.horizontalLayout_6.addWidget(self.sshPasswordEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.sshWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.sshPrivateKeyLineEdit = QLineEdit(self.sshWidget)
        self.sshPrivateKeyLineEdit.setObjectName(u"sshPrivateKeyLineEdit")

        self.horizontalLayout_7.addWidget(self.sshPrivateKeyLineEdit)

        self.sshPrivateKeyToolButton = QToolButton(self.sshWidget)
        self.sshPrivateKeyToolButton.setObjectName(u"sshPrivateKeyToolButton")

        self.horizontalLayout_7.addWidget(self.sshPrivateKeyToolButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.sshWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)

        self.sshPassphraseEdit = QLineEdit(self.sshWidget)
        self.sshPassphraseEdit.setObjectName(u"sshPassphraseEdit")
        self.sshPassphraseEdit.setClearButtonEnabled(False)

        self.horizontalLayout_8.addWidget(self.sshPassphraseEdit)

        self.label_12 = QLabel(self.sshWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.sshTimeoutEdit = QLineEdit(self.sshWidget)
        self.sshTimeoutEdit.setObjectName(u"sshTimeoutEdit")

        self.horizontalLayout_8.addWidget(self.sshTimeoutEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.gridLayout.addWidget(self.sshWidget, 2, 0, 1, 1)

        self.sslWidget = QWidget(AddOrEditConnectionDialog)
        self.sslWidget.setObjectName(u"sslWidget")
        self.verticalLayout = QVBoxLayout(self.sslWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.sslWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_9.addWidget(self.label_13)

        self.horizontalSpacer_2 = QSpacerItem(288, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.sslWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_10.addWidget(self.label_14)

        self.sslPrivateKeylineEdit = QLineEdit(self.sslWidget)
        self.sslPrivateKeylineEdit.setObjectName(u"sslPrivateKeylineEdit")

        self.horizontalLayout_10.addWidget(self.sslPrivateKeylineEdit)

        self.sslPrivateKeyToolButton = QToolButton(self.sslWidget)
        self.sslPrivateKeyToolButton.setObjectName(u"sslPrivateKeyToolButton")

        self.horizontalLayout_10.addWidget(self.sslPrivateKeyToolButton)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_15 = QLabel(self.sslWidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.sslPublicKeylLineEdit = QLineEdit(self.sslWidget)
        self.sslPublicKeylLineEdit.setObjectName(u"sslPublicKeylLineEdit")

        self.horizontalLayout_11.addWidget(self.sslPublicKeylLineEdit)

        self.sslPublicKeylToolButton = QToolButton(self.sslWidget)
        self.sslPublicKeylToolButton.setObjectName(u"sslPublicKeylToolButton")

        self.horizontalLayout_11.addWidget(self.sslPublicKeylToolButton)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.sslWidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_12.addWidget(self.label_16)

        self.sslAuthorityLineEdit = QLineEdit(self.sslWidget)
        self.sslAuthorityLineEdit.setObjectName(u"sslAuthorityLineEdit")

        self.horizontalLayout_12.addWidget(self.sslAuthorityLineEdit)

        self.sslAuthorityToolButton = QToolButton(self.sslWidget)
        self.sslAuthorityToolButton.setObjectName(u"sslAuthorityToolButton")

        self.horizontalLayout_12.addWidget(self.sslAuthorityToolButton)


        self.verticalLayout.addLayout(self.horizontalLayout_12)


        self.gridLayout.addWidget(self.sslWidget, 3, 0, 1, 1)

        self.sentinelWidget = QWidget(AddOrEditConnectionDialog)
        self.sentinelWidget.setObjectName(u"sentinelWidget")
        self.verticalLayout_3 = QVBoxLayout(self.sentinelWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_17 = QLabel(self.sentinelWidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.horizontalSpacer_3 = QSpacerItem(288, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_18 = QLabel(self.sentinelWidget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_14.addWidget(self.label_18)

        self.sentinelMasterGroupNameEdit = QLineEdit(self.sentinelWidget)
        self.sentinelMasterGroupNameEdit.setObjectName(u"sentinelMasterGroupNameEdit")

        self.horizontalLayout_14.addWidget(self.sentinelMasterGroupNameEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_19 = QLabel(self.sentinelWidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_15.addWidget(self.label_19)

        self.sentinelRedisNodePasswordEdit = QLineEdit(self.sentinelWidget)
        self.sentinelRedisNodePasswordEdit.setObjectName(u"sentinelRedisNodePasswordEdit")

        self.horizontalLayout_15.addWidget(self.sentinelRedisNodePasswordEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)


        self.gridLayout.addWidget(self.sentinelWidget, 4, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(AddOrEditConnectionDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)


        self.retranslateUi(AddOrEditConnectionDialog)
        self.buttonBox.rejected.connect(AddOrEditConnectionDialog.reject)

        QMetaObject.connectSlotsByName(AddOrEditConnectionDialog)
    # setupUi

    def retranslateUi(self, AddOrEditConnectionDialog):
        AddOrEditConnectionDialog.setWindowTitle(QCoreApplication.translate("AddOrEditConnectionDialog", u"Add/Edit Connection", None))
        self.label.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"*Host", None))
        self.hostEdit.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"127.0.0.1", None))
        self.label_4.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"*Port", None))
        self.portEdit.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"6379", None))
        self.label_3.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Password", None))
        self.sshCheckBox.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"SSH", None))
        self.sslCheckBox.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"SSL", None))
        self.sentinelCheckBox.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Sentinel", None))
        self.clusterCheckBox.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Cluster", None))
        self.readonlyCheckBox.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Readonly", None))
        self.label_5.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"SSH Config", None))
        self.label_6.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"*Host", None))
        self.sshHostEdit.setText("")
        self.label_7.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Username", None))
        self.label_8.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"*Port", None))
        self.sshPortEdit.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"22", None))
        self.label_9.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Password", None))
        self.label_10.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Private Key", None))
        self.sshPrivateKeyToolButton.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"...", None))
        self.label_11.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Passphrase", None))
        self.sshPassphraseEdit.setText("")
        self.label_12.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Timeout", None))
        self.sshTimeoutEdit.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"30", None))
        self.label_13.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"SSL Config", None))
        self.label_14.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Private Key", None))
        self.sslPrivateKeyToolButton.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"...", None))
        self.label_15.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Public Key", None))
        self.sslPublicKeylToolButton.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"...", None))
        self.label_16.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Authority", None))
        self.sslAuthorityToolButton.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"...", None))
        self.label_17.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Sentinel Config", None))
        self.label_18.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"*Master Group Name", None))
        self.sentinelMasterGroupNameEdit.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"mymaster", None))
        self.label_19.setText(QCoreApplication.translate("AddOrEditConnectionDialog", u"Redis Node Password", None))
    # retranslateUi

