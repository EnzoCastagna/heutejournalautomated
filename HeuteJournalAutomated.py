import sys
from PyQt5 import QtWidgets
import mainwindow
from PyQt5.QtCore import QUrl
import datetime

monate = ["januar", "februar", "marz", "april", "mai", "juni", "juli","august","september","oktober","november","dezember"]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.browser.load(QUrl("https://solvingprocrastination.com/how-to-stop-procrastinating/"))

    def advanceSlider(self):
        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)

app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()

sys.exit(app.exec_())
