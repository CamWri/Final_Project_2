# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainxjLbBv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: None) -> None:
        """
            Constructor that loads up the Main Screen correctly
            :param self: the instance of the __init__ class
            :param MainWindow: The Main Screen in its default stage
            :return: None
        """
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 583)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.443, x2:1, y2:0.466, stop:0 rgba(0, 68, 99, 255), stop:1 rgba(0, 29, 42, 255));\n"
"	color: rgb(230, 230, 230);\n"
"	border-radius: 12px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 120, 500, 51))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 3px solid rgb(0, 108, 154);\n"
"	border-radius: 12px;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px; \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(0, 165, 230);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(198, 198, 198);\n"
"}")
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 30, 391, 51))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(25)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(66, 255, 161);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(590, 120, 121, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 3px solid rgb(0, 108, 154);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 176, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px; \n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.pushButton.setAutoDefault(False)
        self.label_title_2 = QLabel(self.frame)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setGeometry(QRect(110, 290, 551, 51))
        self.label_title_2.setFont(font)
        self.label_title_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.443, x2:1, y2:0.466, stop:0 rgba(0, 68, 99, 255), stop:1 rgba(0, 29, 42, 255));\n"
"color: rgb(17, 204, 221);")
        self.label_title_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 210, 231, 51))
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(540, 220, 151, 41))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: 3px solid rgb(0, 108, 154);\n"
"	border-radius: 10px;\n"
"	color: rgb(66, 255, 161);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px; \n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 220, 181, 41))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border: 3px solid rgb(0, 108, 154);\n"
"	border-radius: 10px;\n"
"	color: rgb(66, 255, 161);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px; \n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.pushButton_3.setAutoDefault(False)
        self.display_label = QLabel(self.frame)
        self.display_label.setObjectName(u"display_label")
        self.display_label.setGeometry(QRect(90, 360, 601, 181))

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow: None) -> None:
        """
        Constructor that loads up the Main Screen correctly
        :param self: the instance of the __init__ class
        :param MainWindow : The Main Screen to it default stage
        :return: None
        """
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input Words Here", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">PRECISION</span> | SEARCH</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"ANALYZE", None))
        self.label_title_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>List Of Suggestions &amp; Possible Replacements</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current Word", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"NEXT WORD", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PREVIOUS WORD", None))
        self.display_label.setText("")
    # retranslateUi

