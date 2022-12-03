# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowvbPLPJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 600)
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
        self.input_word = QLineEdit(self.frame)
        self.input_word.setObjectName(u"input_word")
        self.input_word.setGeometry(QRect(30, 100, 551, 51))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)
        self.input_word.setFont(font)
        self.input_word.setStyleSheet(u"QLineEdit {\n"
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
        self.precision_search = QLabel(self.frame)
        self.precision_search.setObjectName(u"precision_search")
        self.precision_search.setGeometry(QRect(0, 20, 401, 51))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(25)
        self.precision_search.setFont(font1)
        self.precision_search.setStyleSheet(u"color: rgb(66, 255, 161);")
        self.precision_search.setAlignment(Qt.AlignCenter)
        self.analyze_button = QPushButton(self.frame)
        self.analyze_button.setObjectName(u"analyze_button")
        self.analyze_button.setGeometry(QRect(590, 110, 121, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.analyze_button.setFont(font2)
        self.analyze_button.setStyleSheet(u"QPushButton {\n"
"	border: 3px solid rgb(0, 108, 154);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 176, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px; \n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.analyze_button.setAutoDefault(False)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 180, 351, 371))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.current_word = QLabel(self.frame)
        self.current_word.setObjectName(u"current_word")
        self.current_word.setGeometry(QRect(460, 200, 171, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(20)
        self.current_word.setFont(font3)
        self.current_word.setAlignment(Qt.AlignCenter)
        self.next_button = QPushButton(self.frame)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(640, 200, 71, 41))
        self.next_button.setFont(font2)
        self.next_button.setStyleSheet(u"QPushButton {\n"
"	border: 3px solid rgb(0, 108, 154);\n"
"	border-radius: 10px;\n"
"	color: rgb(66, 255, 161);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px; \n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.next_button.setAutoDefault(False)
        self.previous_button = QPushButton(self.frame)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setGeometry(QRect(380, 200, 71, 41))
        self.previous_button.setFont(font2)
        self.previous_button.setStyleSheet(u"QPushButton {\n"
"	border: 3px solid rgb(0, 108, 154);\n"
"	border-radius: 10px;\n"
"	color: rgb(66, 255, 161);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px; \n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.previous_button.setAutoDefault(False)
        self.submit_button = QPushButton(self.frame)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(490, 510, 121, 41))
        self.submit_button.setFont(font2)
        self.submit_button.setStyleSheet(u"QPushButton {\n"
"	border: 3px solid rgb(0, 108, 154);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 176, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px; \n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.submit_button.setAutoDefault(False)
        self.suggestion_1 = QRadioButton(self.frame)
        self.suggestion_1.setObjectName(u"suggestion_1")
        self.suggestion_1.setGeometry(QRect(420, 270, 251, 41))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(22)
        self.suggestion_1.setFont(font4)
        self.suggestion_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.suggestion_2 = QRadioButton(self.frame)
        self.suggestion_2.setObjectName(u"suggestion_2")
        self.suggestion_2.setGeometry(QRect(420, 330, 221, 41))
        self.suggestion_2.setFont(font4)
        self.suggestion_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.suggestion_3 = QRadioButton(self.frame)
        self.suggestion_3.setObjectName(u"suggestion_3")
        self.suggestion_3.setGeometry(QRect(420, 390, 221, 41))
        self.suggestion_3.setFont(font4)
        self.suggestion_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.suggestion_4 = QRadioButton(self.frame)
        self.suggestion_4.setObjectName(u"suggestion_4")
        self.suggestion_4.setGeometry(QRect(420, 450, 221, 41))
        self.suggestion_4.setFont(font4)
        self.suggestion_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.analyze_button.setDefault(False)
        self.submit_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input_word.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input Words Here", None))
        self.precision_search.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">PRECISION</span> | SEARCH</p></body></html>", None))
        self.analyze_button.setText(QCoreApplication.translate("MainWindow", u"ANALYZE", None))
        self.current_word.setText(QCoreApplication.translate("MainWindow", u"Current Word", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.previous_button.setText(QCoreApplication.translate("MainWindow", u"PREV", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"SUMBIT", None))
        self.suggestion_1.setText(QCoreApplication.translate("MainWindow", u"SUGGESTION 1", None))
        self.suggestion_2.setText(QCoreApplication.translate("MainWindow", u"SUGGESTION 2", None))
        self.suggestion_3.setText(QCoreApplication.translate("MainWindow", u"SUGGESTION 3", None))
        self.suggestion_4.setText(QCoreApplication.translate("MainWindow", u"SUGGESTION 4", None))
    # retranslateUi

