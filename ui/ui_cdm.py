# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cdmrVthrV.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 510)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/images/mgw.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(36, 36))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	color:#8590C8;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"#frame {\n"
"    background-color: #0E161F;\n"
"	border:0px;\n"
" 	margin:0px;\n"
"}\n"
"#frame_2{\n"
"    background-color: #0F111A;\n"
"}\n"
"QStackedWidget{\n"
"	background-color: #0F111A;\n"
"}\n"
"#frame{\n"
"	margin-right:0px;\n"
"	border:0px;\n"
"	padding-right:0px;\n"
"}\n"
"#frame .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 15px solid transparent;\n"
"	border-right: 0px;\n"
"	margin-right:0px;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#frame .QPushButton:hover {\n"
"	background-color:#1F2233;\n"
"	color:#DDDDDD;\n"
"}\n"
"#frame .QPushButton:pressed {	\n"
"	background-color: #1E3250;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/*\n"
"background-color: #0E161F;\n"
"*/\n"
"QPushButton {	\n"
"	border: none;\n"
"	background-color: #020817;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	backg"
                        "round-color:#003264;\n"
"	color:#DDDDDD;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #0264AF;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#stackedWidget .QPushButton {	\n"
"	border: none;\n"
"	background-color: #0E161F;\n"
"	text-align: center;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background: rgb(52, 59, 72);\n"
"	width: 7px;\n"
"	margin: 11px 0 11px 0;\n"
"	/*border-radius: 0px;*/\n"
"}\n"
"QScrollBar::handle:vertical {	\n"
"	background: rgb(22,160,255);\n"
"	min-height: 25px;\n"
"	/*border-radius: 4px*/\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);	\n"
"	height: 10px;\n"
"	/*border-bottom-left-radius: 4px;\n"
"	border-bottom-right-radius: 4px;*/\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);\n"
"	height: 10px;\n"
"	/*border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;*/\n"
"	subcontrol-position: to"
                        "p;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"QGroupBox {\n"
"	background-color: #090B10;\n"
"    border: 1px solid #0264AF;\n"
"    margin-top: 1px; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"	margin-top:0px;\n"
"    padding: 0 3px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(50, 0))
        self.frame.setMaximumSize(QSize(50, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setMaximumSize(QSize(16777215, 40))
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton.setStyleSheet(u"background-image: url(:/icons/icons/cil-menu.png);")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        self.pushButton_2.setMaximumSize(QSize(16777215, 40))
        self.pushButton_2.setFocusPolicy(Qt.NoFocus)
        self.pushButton_2.setStyleSheet(u"background-image: url(:/icons/icons/cil-data-transfer-down.png);")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setMaximumSize(QSize(16777215, 40))
        self.pushButton_3.setFocusPolicy(Qt.NoFocus)
        self.pushButton_3.setStyleSheet(u"background-image: url(:/icons/icons/cil-description.png);")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 40))
        self.pushButton_4.setMaximumSize(QSize(16777215, 40))
        self.pushButton_4.setFocusPolicy(Qt.NoFocus)
        self.pushButton_4.setStyleSheet(u"background-image: url(:/icons/icons/cil-user-female.png);")

        self.verticalLayout.addWidget(self.pushButton_4)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:#82aaff;\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label_2)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background-color: #0F111A;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.pushButton_6 = QPushButton(self.page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        self.pushButton_6.setMaximumSize(QSize(100, 16777215))
        self.pushButton_6.setFocusPolicy(Qt.NoFocus)
        self.pushButton_6.setStyleSheet(u"/*\n"
"background-color: #0E161F;\n"
"*/\n"
"QPushButton {	\n"
"	border: none;\n"
"	background-color: #020817;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:#003264;\n"
"	color:#DDDDDD;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #0264AF;\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.plainTextEdit = QPlainTextEdit(self.page)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 90))
        self.plainTextEdit.setFocusPolicy(Qt.ClickFocus)
        self.plainTextEdit.setStyleSheet(u"/*border:1px solid #0264AF;	selection-color: rgb(255, 255, 255);*/\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: #090B10;\n"
"	padding: 10px;\n"
"	border:none;\n"
"	selection-background-color: rgb(22, 160, 255);\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 1px solid #0264AF ;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 1px solid #0264AF;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.plainTextEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit.setStyleSheet(u"/*border:1px solid #0264AF;	border-radius: 5px;	padding: 10px;*/\n"
"QLineEdit {\n"
"	background-color: #090B10;\n"
"	border:none;\n"
"	selection-background-color: rgb(22, 160, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 1px solid #0264AF ;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 1px solid #0264AF ;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton_5 = QPushButton(self.page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(86, 25))
        self.pushButton_5.setFocusPolicy(Qt.NoFocus)
        self.pushButton_5.setStyleSheet(u"/*\n"
"background-color: #0E161F;\n"
"*/\n"
"QPushButton {	\n"
"	border: none;\n"
"	background-color: #020817;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:#003264;\n"
"	color:#DDDDDD;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #0264AF;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pushButton_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 50))
        self.label_10.setStyleSheet(u"color:#0264AF;\n"
"font: 700 11pt \"Segoe UI\";\n"
"")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_10)

        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"	background-color: #090B10;\n"
"	/*border:none;")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_6.setContentsMargins(9, -1, 9, 9)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, -1)

        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 9, -1, -1)

        self.horizontalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"/*	background-color: #090B10;\n"
"	/*border:none;")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(9, -1, 9, 9)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_5.setContentsMargins(-1, 9, -1, -1)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(40, 20))

        self.horizontalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_5.addWidget(self.label_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.pushButton_7 = QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 25))
        self.pushButton_7.setMaximumSize(QSize(80, 16777215))
        self.pushButton_7.setFocusPolicy(Qt.NoFocus)
        self.pushButton_7.setStyleSheet(u"/*\n"
"background-color: #0E161F;\n"
"*/\n"
"QPushButton {	\n"
"	border: none;\n"
"	background-color: #020817;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:#003264;\n"
"	color:#DDDDDD;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #0264AF;\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.progressBar = QProgressBar(self.groupBox_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #0264AF;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #16A0FF;\n"
"    width: 1px;\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_5.addWidget(self.progressBar)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_3 = QGroupBox(self.page_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 15, 2, 2)
        self.listWidget = QListWidget(self.groupBox_3)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"border:none;")

        self.verticalLayout_9.addWidget(self.listWidget)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setMargin(25)
        self.label.setOpenExternalLinks(True)

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u" QLabel { \n"
"	font-size: 11px; color: \n"
"	rgb(113, 126, 149);\n"
"	padding-left: 10px; \n"
"	padding-right: 10px; \n"
"	padding-bottom: 2px; }")

        self.verticalLayout_2.addWidget(self.label_5)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CyberDropMe-dl", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter URL(s):", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.plainTextEdit.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Save at:", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_10.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Current Threads", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"URL :", None))
        self.label_9.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Files Downloaded :", None))
        self.label_7.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"log will appear here.", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#16a0ff;\">CyberDropMe-dl</span></p><p align=\"center\"><span style=\" color:#8590c8;\">A downloader GUI for downloading files from the </span><a href=\"https://cyberdrop.me/\"><span style=\" text-decoration: underline; color:#0264af;\">Cyberdrop</span></a><span style=\" color:#8590c8;\"> file hosting service created using Python and PySide6 (support for PyQt), and with colors based on the Deep Ocean theme by </span><a href=\"https://material-theme.com/docs/reference/color-palette\"><span style=\" text-decoration: underline; color:#0264af;\">Material UI Theme</span></a><span style=\" color:#8590c8;\">.</span></p><p align=\"center\"><span style=\" color:#8590c8;\">MIT License</span></p><p align=\"center\"><span style=\" color:#16a0ff;\">Created by: </span><a href=\"https://github.com/magnusjwatson2786\"><span style=\" text-decoration: underline; color:#0264af;\">magnusjwatson2786</span></a><span style=\" color:#16a0ff;\""
                        "> @GitHub</span></p><p align=\"center\"><br/></p><p align=\"right\"><a href=\"https://github.com/magnusjwatson2786/CyberDropMe-dl\"><span style=\" text-decoration: underline; color:#0264af;\">GitHub Repository</span></a></p><p align=\"right\"><a href=\"https://github.com/magnusjwatson2786/CyberDropMe-dl/releases\"><span style=\" text-decoration: underline; color:#0264af;\">Releases</span></a></p><p align=\"right\"><a href=\"https://github.com/magnusjwatson2786/CyberDropMe-dl/issues/new\"><span style=\" text-decoration: underline; color:#0264af;\">Report an issue</span></a></p><p align=\"right\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tip: Paste the url(s) and hit Add.", None))
    # retranslateUi

