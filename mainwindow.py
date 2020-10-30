# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('mainwindow.ui', self) # Load the .ui file
        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.menuFile = self.findChild(QtWidgets.QMenu, 'menuFile')
        self.actionQuit = self.findChild(QtWidgets.QAction, 'actionQuit')
        self.progressBar = self.findChild(QtWidgets.QProgressBar, 'progressBar')
        self.testButton = self.findChild(QtWidgets.QPushButton, 'testButton')
        self.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Click Me!"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))

