@@ -1,104 +0,0 @@
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

#This imports the UI design from the Loading Screen
from ui_loading_screen import Ui_LoadingScreen

#This imports the UI design from the Main Screen
from ui_main import Ui_MainWindow

# Counter for the Percentage
counter = 0

# Main Screen
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # This removes the title section of the screen and makes a floating window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)





# Loading Screen
class LoadingScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)

    # UI Code


        # This removes the title section of the screen and makes a floating window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        # Creates drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # This starts the QTimer for the progress bar
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(50)

        # Changes the description of the subtitle after a certain millisecond count

        # Our programs slogan
        self.ui.label_description.setText("THE WORLD'S BEST TYPING ASSISTANT")

        # Changes the description of the subtitle after a certain millisecond count
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(5000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        # This causes the main screen to load after the loading screen closes
        self.show()


    # App functions
    def progress(self):

        global counter

        # Sets the value of the counter to the initial value
        self.ui.progressBar.setValue(counter)

        # Creates a clone of the loading screen and opens up the main screen
        if counter > 100:
            # Stops the timer
            self.timer.stop()

            # Shows the main screen
            self.main = MainWindow()
            self.main.show()

            # Closes the loading screen
            self.close()

        # increments the counter by 1 until it hits 100.
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingScreen()
    sys.exit(app.exec_())