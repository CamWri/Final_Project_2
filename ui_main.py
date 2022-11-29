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
from Merge_Sort_Algorithm import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        self.Input = QLineEdit(self.frame)
        self.Input.setObjectName(u"lineEdit")
        self.Input.setGeometry(QRect(60, 120, 500, 51))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)
        self.Input.setFont(font)
        self.Input.setStyleSheet(u"QLineEdit {\n"
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
        self.Title = QLabel(self.frame)
        self.Title.setObjectName(u"label_title")
        self.Title.setGeometry(QRect(0, 30, 391, 51))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(25)
        self.Title.setFont(font1)
        self.Title.setStyleSheet(u"color: rgb(66, 255, 161);")
        self.Title.setAlignment(Qt.AlignCenter)
        self.Analyze_Button = QPushButton(self.frame)
        self.Analyze_Button.setObjectName(u"pushButton")
        self.Analyze_Button.setGeometry(QRect(590, 120, 121, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.Analyze_Button.setFont(font2)
        self.Analyze_Button.clicked.connect(self.analyze) #------------------------------------------------------------------------------
        self.Analyze_Button.setStyleSheet(u"QPushButton {\n"
"	border: 3px solid rgb(0, 108, 154);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 176, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px; \n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.Analyze_Button.setAutoDefault(False)
        self.Suggested_List = QLabel(self.frame)
        self.Suggested_List.setObjectName(u"label_title_2")
        self.Suggested_List.setGeometry(QRect(110, 290, 551, 51))
        self.Suggested_List.setFont(font)
        self.Suggested_List.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.443, x2:1, y2:0.466, stop:0 rgba(0, 68, 99, 255), stop:1 rgba(0, 29, 42, 255));\n"
"color: rgb(17, 204, 221);")
        self.Suggested_List.setAlignment(Qt.AlignCenter)
        self.Current_Word = QLabel(self.frame)
        self.Current_Word.setObjectName(u"label")
        self.Current_Word.setGeometry(QRect(280, 210, 231, 51))
        self.Current_Word.setFont(font1)
        self.Current_Word.setAlignment(Qt.AlignCenter)
        self.Next_Button = QPushButton(self.frame)
        self.Next_Button.setObjectName(u"pushButton_2")
        self.Next_Button.setGeometry(QRect(540, 220, 151, 41))
        self.Next_Button.setFont(font2)
        self.Next_Button.setStyleSheet(u"QPushButton {\n"
"	border: 3px solid rgb(0, 108, 154);\n"
"	border-radius: 10px;\n"
"	color: rgb(66, 255, 161);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px; \n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.Next_Button.setAutoDefault(False)
        self.Previous_Button = QPushButton(self.frame)
        self.Previous_Button.setObjectName(u"pushButton_3")
        self.Previous_Button.setGeometry(QRect(70, 220, 181, 41))
        self.Previous_Button.setFont(font2)
        self.Previous_Button.setStyleSheet(u"QPushButton {\n"
"	border: 3px solid rgb(0, 108, 154);\n"
"	border-radius: 10px;\n"
"	color: rgb(66, 255, 161);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px; \n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.Previous_Button.setAutoDefault(False)
        self.Analyzed_Input = QTextBrowser(self.frame)
        self.Analyzed_Input.setObjectName(u"display_TextBrowser")
        self.Analyzed_Input.setGeometry(QRect(90, 360, 601, 181))

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input Words Here", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">PRECISION</span> | SEARCH</p></body></html>", None))
        self.Analyze_Button.setText(QCoreApplication.translate("MainWindow", u"ANALYZE", None))
        self.Suggested_List.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>List Of Suggestions &amp; Possible Replacements</p></body></html>", None))
        self.Current_Word.setText(QCoreApplication.translate("MainWindow", u"Current Word", None))
        self.Next_Button.setText(QCoreApplication.translate("MainWindow", u"NEXT WORD", None))
        self.Previous_Button.setText(QCoreApplication.translate("MainWindow", u"PREVIOUS WORD", None))
        self.Analyzed_Input.setText("")
    # retranslateUi



    def analyze(self):
        pass

    def submit(self):
        pass