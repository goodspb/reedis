# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTableView, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(846, 604)
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionAll_Connects = QAction(MainWindow)
        self.actionAll_Connects.setObjectName(u"actionAll_Connects")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.connectionList = QComboBox(self.centralwidget)
        self.connectionList.setObjectName(u"connectionList")

        self.horizontalLayout.addWidget(self.connectionList)

        self.connectButton = QPushButton(self.centralwidget)
        self.connectButton.setObjectName(u"connectButton")

        self.horizontalLayout.addWidget(self.connectButton)

        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout.addWidget(self.addButton)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")

        self.horizontalLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(True)

        self.horizontalLayout.addWidget(self.deleteButton)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dbList = QComboBox(self.centralwidget)
        self.dbList.setObjectName(u"dbList")

        self.horizontalLayout_2.addWidget(self.dbList)

        self.searchInput = QLineEdit(self.centralwidget)
        self.searchInput.setObjectName(u"searchInput")

        self.horizontalLayout_2.addWidget(self.searchInput)

        self.TypeLabel = QLabel(self.centralwidget)
        self.TypeLabel.setObjectName(u"TypeLabel")

        self.horizontalLayout_2.addWidget(self.TypeLabel, 0, Qt.AlignRight)

        self.typeShowInput = QLineEdit(self.centralwidget)
        self.typeShowInput.setObjectName(u"typeShowInput")
        self.typeShowInput.setEnabled(True)
        self.typeShowInput.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.typeShowInput)

        self.ttlLabel = QLabel(self.centralwidget)
        self.ttlLabel.setObjectName(u"ttlLabel")

        self.horizontalLayout_2.addWidget(self.ttlLabel, 0, Qt.AlignRight)

        self.ttlShowEditInput = QLineEdit(self.centralwidget)
        self.ttlShowEditInput.setObjectName(u"ttlShowEditInput")

        self.horizontalLayout_2.addWidget(self.ttlShowEditInput)

        self.saveContentButton = QPushButton(self.centralwidget)
        self.saveContentButton.setObjectName(u"saveContentButton")
        self.saveContentButton.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.saveContentButton)

        self.refreshContentButton = QPushButton(self.centralwidget)
        self.refreshContentButton.setObjectName(u"refreshContentButton")
        self.refreshContentButton.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.refreshContentButton)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 1)
        self.horizontalLayout_2.setStretch(5, 2)
        self.horizontalLayout_2.setStretch(6, 1)
        self.horizontalLayout_2.setStretch(7, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.keyList = QListView(self.centralwidget)
        self.keyList.setObjectName(u"keyList")
        self.keyList.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.verticalLayout_7.addWidget(self.keyList)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.addKeyButton = QPushButton(self.centralwidget)
        self.addKeyButton.setObjectName(u"addKeyButton")

        self.horizontalLayout_6.addWidget(self.addKeyButton)

        self.refreshKeysButton = QPushButton(self.centralwidget)
        self.refreshKeysButton.setObjectName(u"refreshKeysButton")

        self.horizontalLayout_6.addWidget(self.refreshKeysButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.stackedContents = QStackedWidget(self.centralwidget)
        self.stackedContents.setObjectName(u"stackedContents")
        self.contentStrEditPage = QWidget()
        self.contentStrEditPage.setObjectName(u"contentStrEditPage")
        self.contentStrEditPage.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.contentStrEditPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.contentTypeList = QComboBox(self.contentStrEditPage)
        self.contentTypeList.addItem(u"plain text")
        self.contentTypeList.addItem(u"Json")
        self.contentTypeList.addItem(u"Django")
        self.contentTypeList.setObjectName(u"contentTypeList")

        self.horizontalLayout_4.addWidget(self.contentTypeList)

        self.sizeLabel = QLabel(self.contentStrEditPage)
        self.sizeLabel.setObjectName(u"sizeLabel")

        self.horizontalLayout_4.addWidget(self.sizeLabel)

        self.horizontalSpacer_2 = QSpacerItem(348, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.contentStrEdit = QTextEdit(self.contentStrEditPage)
        self.contentStrEdit.setObjectName(u"contentStrEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentStrEdit.sizePolicy().hasHeightForWidth())
        self.contentStrEdit.setSizePolicy(sizePolicy)
        self.contentStrEdit.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.contentStrEdit)

        self.stackedContents.addWidget(self.contentStrEditPage)
        self.contentTablePage = QWidget()
        self.contentTablePage.setObjectName(u"contentTablePage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.contentTablePage.sizePolicy().hasHeightForWidth())
        self.contentTablePage.setSizePolicy(sizePolicy1)
        self.contentTablePage.setAutoFillBackground(False)
        self.verticalLayout_6 = QVBoxLayout(self.contentTablePage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addMemberButton = QPushButton(self.contentTablePage)
        self.addMemberButton.setObjectName(u"addMemberButton")

        self.horizontalLayout_3.addWidget(self.addMemberButton)

        self.maxLabel = QLabel(self.contentTablePage)
        self.maxLabel.setObjectName(u"maxLabel")

        self.horizontalLayout_3.addWidget(self.maxLabel)

        self.maxLineEdit = QLineEdit(self.contentTablePage)
        self.maxLineEdit.setObjectName(u"maxLineEdit")

        self.horizontalLayout_3.addWidget(self.maxLineEdit)

        self.minLabel = QLabel(self.contentTablePage)
        self.minLabel.setObjectName(u"minLabel")

        self.horizontalLayout_3.addWidget(self.minLabel)

        self.minLineEdit = QLineEdit(self.contentTablePage)
        self.minLineEdit.setObjectName(u"minLineEdit")

        self.horizontalLayout_3.addWidget(self.minLineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.contentTable = QTableView(self.contentTablePage)
        self.contentTable.setObjectName(u"contentTable")
        sizePolicy.setHeightForWidth(self.contentTable.sizePolicy().hasHeightForWidth())
        self.contentTable.setSizePolicy(sizePolicy)
        self.contentTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.contentTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.contentTable.horizontalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_6.addWidget(self.contentTable)

        self.stackedContents.addWidget(self.contentTablePage)

        self.horizontalLayout_7.addWidget(self.stackedContents)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 846, 36))
        self.menubar.setDefaultUp(True)
        self.menuConnects = QMenu(self.menubar)
        self.menuConnects.setObjectName(u"menuConnects")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuConnects.menuAction())
        self.menuConnects.addAction(self.actionAdd)
        self.menuConnects.addAction(self.actionAll_Connects)

        self.retranslateUi(MainWindow)

        self.stackedContents.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Reedis", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.actionAll_Connects.setText(QCoreApplication.translate("MainWindow", u"All Connects", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.searchInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter to Search", None))
        self.TypeLabel.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.typeShowInput.setPlaceholderText("")
        self.ttlLabel.setText(QCoreApplication.translate("MainWindow", u"TTL", None))
        self.ttlShowEditInput.setPlaceholderText("")
        self.saveContentButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.refreshContentButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.addKeyButton.setText(QCoreApplication.translate("MainWindow", u"Add Key", None))
        self.refreshKeysButton.setText(QCoreApplication.translate("MainWindow", u"Refresh Keys", None))

        self.sizeLabel.setText(QCoreApplication.translate("MainWindow", u"Size: 0", None))
        self.addMemberButton.setText(QCoreApplication.translate("MainWindow", u"Add member", None))
        self.maxLabel.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.maxLineEdit.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.minLabel.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.minLineEdit.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.menuConnects.setTitle(QCoreApplication.translate("MainWindow", u"Connects", None))
    # retranslateUi

