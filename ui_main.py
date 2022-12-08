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
from Merge_Sort_Algorithm import *

word_index = 0

spellchecked_input = []

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
        self.analyze_button.clicked.connect(self.button_analyze)
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
        self.analyzed_output = QTextBrowser(self.frame)
        self.analyzed_output.setObjectName(u"stackedWidget")
        self.analyzed_output.setGeometry(QRect(20, 250, 700, 500))
        font5 = QFont()
        font5.setPointSize(10)
        self.analyzed_output.setFont(font5)
        self.current_word = QLabel(self.frame)
        self.current_word.setObjectName(u"current_word")
        self.current_word.setGeometry(QRect(250, 200, 171, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(20)
        self.current_word.setFont(font3)
        self.current_word.setAlignment(Qt.AlignCenter)
        self.next_button = QPushButton(self.frame)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(450, 200, 71, 41))
        self.next_button.setFont(font2)
        self.next_button.clicked.connect(self.next_word)
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
        self.previous_button.setGeometry(QRect(150, 200, 71, 41))
        self.previous_button.setFont(font2)
        self.previous_button.clicked.connect(self.previous_word)
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
        self.submit_button.setGeometry(QRect(270, 510, 121, 41))
        self.submit_button.setFont(font2)
        self.submit_button.clicked.connect(self.submit)
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
        self.suggestion_1.setGeometry(QRect(230, 270, 251, 41))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(15)
        self.suggestion_1.setFont(font4)
        self.suggestion_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.suggestion_2 = QRadioButton(self.frame)
        self.suggestion_2.setObjectName(u"suggestion_2")
        self.suggestion_2.setGeometry(QRect(230, 330, 221, 41))
        self.suggestion_2.setFont(font4)
        self.suggestion_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.suggestion_3 = QRadioButton(self.frame)
        self.suggestion_3.setObjectName(u"suggestion_3")
        self.suggestion_3.setGeometry(QRect(230, 390, 221, 41))
        self.suggestion_3.setFont(font4)
        self.suggestion_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.suggestion_4 = QRadioButton(self.frame)
        self.suggestion_4.setObjectName(u"suggestion_4")
        self.suggestion_4.setGeometry(QRect(230, 450, 221, 41))
        self.suggestion_4.setFont(font4)
        self.suggestion_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.analyze_button.setDefault(False)
        self.submit_button.setDefault(False)

        self.next_button.setHidden(True)
        self.previous_button.setHidden(True)
        self.submit_button.setHidden(True)
        self.suggestion_1.setHidden(True)
        self.suggestion_2.setHidden(True)
        self.suggestion_3.setHidden(True)
        self.suggestion_4.setHidden(True)
        self.current_word.setHidden(True)
        self.analyzed_output.setHidden(False)


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
        self.analyzed_output.setText(QCoreApplication.translate("MainWindow", "\nWarning! This program only checks spelling of letters and apostrophes. "
        + "Any misspelled word dealing with any other character(i.e: ! , ?, \", \' . and so many more) will be replaced with the selected word you choose or we can not find the adequate word."
        + " Once exception is contractions. As long as you have the apostrophe, it should suggust the correct word if spelt incorrectly. To start, input your word or sentence. "
        +  "Then, click analyze. Click the circular button for the word you want, and if you want none of the requested words, just click next."
        + " You reach the final page when the submit button becomes the finalize button. Once clicked, it will give you your changes. We suggust single words or sentences.", None))
    # retranslateUi

    def button_analyze(self) -> None:
        '''
        Establishes and displays the first incorrectly spelt word and the display of four suggusted words
        :return:
        '''
        global word_index
        word_index = 0

        global spellchecked_input
        spellchecked_input = []

        input = self.input_word.text()

        suggusted_words = all_incorrect_words(input)[0]
        incorrect_word = all_incorrect_words(input)[2]

        self.suggestion_1.setHidden(False)
        self.suggestion_2.setHidden(False)
        self.suggestion_3.setHidden(False)
        self.suggestion_4.setHidden(False)
        self.submit_button.setHidden(False)
        self.previous_button.setHidden(False)
        self.current_word.setHidden(False)
        self.next_button.setHidden(False)
        self.analyzed_output.setHidden(True)

        if len(incorrect_word) > 0:
            suggustion_1 = suggusted_words[incorrect_word[0]][0]
            suggustion_2 = suggusted_words[incorrect_word[0]][1]
            suggustion_3 = suggusted_words[incorrect_word[0]][2]
            suggustion_4 = suggusted_words[incorrect_word[0]][3]

            self.current_word.setText(incorrect_word[0])
            self.suggestion_1.setText(suggustion_1)
            self.suggestion_2.setText(suggustion_2)
            self.suggestion_3.setText(suggustion_3)
            self.suggestion_4.setText(suggustion_4)
        else:
            self.current_word.setText('Finalize')
            self.suggestion_1.setHidden(True)
            self.suggestion_2.setHidden(True)
            self.suggestion_3.setHidden(True)
            self.suggestion_4.setHidden(True)
            self.next_button.setHidden(True)
            self.current_word.setHidden(True)
            self.previous_button.setHidden(True)
            self.analyzed_output.setHidden(False)
            self.analyzed_output.setText(f'Your text is perfect!\n{self.input_word.text()}')
            self.submit_button.setHidden(True)

    def next_word(self) -> None:
        '''
        Goes to the next incorrectly spelt word if possible and established the four suggusted words.
        :return: None
        '''
        input = self.input_word.text()

        suggusted_words = all_incorrect_words(input)[0]
        incorrect_word = all_incorrect_words(input)[2]

        self.suggestion_1.setHidden(False)
        self.suggestion_2.setHidden(False)
        self.suggestion_3.setHidden(False)
        self.suggestion_4.setHidden(False)
        self.submit_button.setHidden(False)

        incorrect_word.append('Finalize')
        global word_index
        if len(incorrect_word) > word_index:
            word_index += 1
            if incorrect_word[word_index] == 'Finalize':
                self.analyzed_output.setHidden(False)
                self.current_word.setText(incorrect_word[word_index])
                self.analyzed_output.setText('Get your finalized outcome if you click the Finalize button below. You will see your full changes from our spell checker.')
                self.suggestion_1.setHidden(True)
                self.suggestion_2.setHidden(True)
                self.suggestion_3.setHidden(True)
                self.suggestion_4.setHidden(True)
                self.next_button.setHidden(True)
                self.current_word.setHidden(True)
                self.submit_button.setText('Finalize')
                self.previous_button.setGeometry(QRect(300, 200, 71, 41))
            elif len(incorrect_word) - 1 > word_index:
                suggustion_1 = suggusted_words[incorrect_word[word_index]][0]
                suggustion_2 = suggusted_words[incorrect_word[word_index]][1]
                suggustion_3 = suggusted_words[incorrect_word[word_index]][2]
                suggustion_4 = suggusted_words[incorrect_word[word_index]][3]


                self.current_word.setText(incorrect_word[word_index])
                self.suggestion_1.setText(suggustion_1)
                self.suggestion_2.setText(suggustion_2)
                self.suggestion_3.setText(suggustion_3)
                self.suggestion_4.setText(suggustion_4)

    def previous_word(self) -> None:
        '''
        Goes to the previous incorrectly spelt word if possible and established what word it is looking at and the suggusted words.
        :return: None
        '''
        input = self.input_word.text()

        suggusted_words = all_incorrect_words(input)[0]
        incorrect_word = all_incorrect_words(input)[2]

        self.suggestion_1.setHidden(False)
        self.suggestion_2.setHidden(False)
        self.suggestion_3.setHidden(False)
        self.suggestion_4.setHidden(False)
        self.submit_button.setHidden(False)
        self.previous_button.setHidden(False)
        self.next_button.setHidden(False)
        self.current_word.setHidden(False)

        self.previous_button.setGeometry(QRect(150, 200, 71, 41))

        self.analyzed_output.setHidden(True)

        self.submit_button.setText('Submit')

        global word_index


        if 0 < word_index:
            word_index -= 1
            self.current_word.setText(incorrect_word[word_index])
            self.suggestion_1.setText(suggusted_words[incorrect_word[word_index]][0])
            self.suggestion_2.setText(suggusted_words[incorrect_word[word_index]][1])
            self.suggestion_3.setText(suggusted_words[incorrect_word[word_index]][2])
            self.suggestion_4.setText(suggusted_words[incorrect_word[word_index]][3])


    def submit(self) -> None:
        '''
        Checks to see if the current displayed word is incorrectly spelt words, if equals Finalize(which is manually added correctly spelt control variable), replace all
        incorrectly spelt words with their sugguested word, and set the spell checked output into the QTextBrowser, and if not the word Finalize, add a list of the suggusted
        word and the word index for the displayed word. Then it goes calls the next_word method.
        :return: None
        '''
        input = self.input_word.text()

        incorrect_index = all_incorrect_words(input)[1]
        incorrect_word = all_incorrect_words(input)[2]

        unchanged_input = input.split()

        self.suggestion_1.setHidden(True)
        self.suggestion_2.setHidden(True)
        self.suggestion_3.setHidden(True)
        self.suggestion_4.setHidden(True)
        self.submit_button.setHidden(True)

        if self.current_word.text() == 'Finalize':
            global spellchecked_input
            x = 0
            while x < len(spellchecked_input):
                correct_word = spellchecked_input[x][0]
                index_of_word = spellchecked_input[x][1]

                unchanged_input[incorrect_index[index_of_word]] = unchanged_input[incorrect_index[index_of_word]].replace(input[index_of_word],correct_word)

                unchanged_input[incorrect_index[index_of_word]] = correct_word

                x+=1

            finalized_input = ' '.join(unchanged_input)

            self.analyzed_output.setText(f'Your finalized outcome is: \n {finalized_input}')

            self.analyzed_output.setHidden(False)
            self.current_word.setHidden(True)
            self.next_button.setHidden(True)
            self.previous_button.setHidden(True)

        else:
            #TODO: do something to keep the capitalization if they have it capitalized
            if self.suggestion_1.isChecked():
                sugguested_word = self.suggestion_1.text()
            elif self.suggestion_2.isChecked():
                sugguested_word = self.suggestion_2.text()
            elif self.suggestion_3.isChecked():
                sugguested_word = self.suggestion_3.text()
            elif self.suggestion_4.isChecked():
                sugguested_word = self.suggestion_4.text()
            else:
                sugguested_word = incorrect_word[word_index]

            important_info = [sugguested_word, word_index]

            spellchecked_input.append(important_info)

            self.next_word()