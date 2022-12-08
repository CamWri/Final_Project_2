# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading_screenKNSZoU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoadingScreen(object):
    def setupUi(self, LoadingScreen: None ) -> None:
        """
        Constructor that loads up the loading screen correctly
        :param self: the instance of the __init__ class
        :param LoadingScreen: The Loading Screen with the progress bar
        :return: None
        """
        if not LoadingScreen.objectName():
            LoadingScreen.setObjectName(u"LoadingScreen")
        LoadingScreen.resize(680, 400)
        self.centralwidget = QWidget(LoadingScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.443, x2:1, y2:0.466, stop:0 rgba(0, 68, 99, 255), stop:1 rgba(0, 29, 42, 255));\n"
"	color: rgb(230, 230, 230);\n"
"	border-radius: 12px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 50, 661, 101))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(66, 255, 161);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 140, 661, 51))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(15)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(17, 204, 221)")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 250, 561, 21))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.472, x2:1, y2:0.466, stop:0 rgba(255, 212, 101, 255), stop:1 rgba(255, 133, 11, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 270, 661, 51))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(17, 204, 221)")
        self.label_loading.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        LoadingScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadingScreen)

        QMetaObject.connectSlotsByName(LoadingScreen)
    # setupUi

    def retranslateUi(self, LoadingScreen: None) -> None:
        """
        Constructor that loads up components of the Loading Screen
        :param self: the instance of the __init__ class
        :param LoadingScreen: The Loading Screen with the text labels
        :return: None
        """
        LoadingScreen.setWindowTitle(QCoreApplication.translate("LoadingScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("LoadingScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">PRECISION</span> | SEARCH</p></body></html>", None))
        self.label_description.setText(QCoreApplication.translate("LoadingScreen", u"THE WORLD'S BEST TYPING ASSISTANT", None))
        self.label_loading.setText(QCoreApplication.translate("LoadingScreen", u"loading.....", None))
    # retranslateUi

