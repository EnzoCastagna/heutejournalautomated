import sys
from PyQt5 import QtWidgets
import mainwindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.testButton.clicked.connect(self.printTest)
        self.ui.pushButton.clicked.connect(self.advanceSlider)

    def advanceSlider(self):
        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)
    
    def printTest(self):
        print("Hello qt world!")

app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()

sys.exit(app.exec_())
