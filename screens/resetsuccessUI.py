# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\zek\3rd yr comsci\summer\CS 304\soft eng\github\qt\resetsuccess.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(10, 131, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #5e3b96;\n"
"color:white;\n"
" border-radius:20px;\n"
"}")
        self.back.setObjectName("back")
        self.BGviolet = QtWidgets.QLabel(self.centralwidget)
        self.BGviolet.setGeometry(QtCore.QRect(0, 0, 961, 121))
        self.BGviolet.setStyleSheet("QLabel\n"
"{\n"
"background: #5e3b96;\n"
"}")
        self.BGviolet.setText("")
        self.BGviolet.setObjectName("BGviolet")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(260, 0, 421, 121))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/logog.jpg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(348, 200, 251, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(390, 430, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.login.setFont(font)
        self.login.setStyleSheet("QPushButton\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.login.setObjectName("login")
        self.BGviolet_2 = QtWidgets.QLabel(self.centralwidget)
        self.BGviolet_2.setGeometry(QtCore.QRect(350, 170, 251, 311))
        self.BGviolet_2.setStyleSheet("QLabel\n"
"{\n"
"background: #5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.BGviolet_2.setText("")
        self.BGviolet_2.setObjectName("BGviolet_2")
        self.BGviolet_2.raise_()
        self.back.raise_()
        self.BGviolet.raise_()
        self.label_12.raise_()
        self.label.raise_()
        self.login.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Password Reset<br/>Succesful!</p></body></html>"))
        self.login.setText(_translate("MainWindow", "Back to Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())