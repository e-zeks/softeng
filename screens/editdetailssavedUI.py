# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\zek\3rd yr comsci\summer\CS 304\soft eng\github\qt\editdetailssaved.ui'
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
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(0, 10, 141, 41))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/logog.jpg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.BGviolet = QtWidgets.QLabel(self.centralwidget)
        self.BGviolet.setGeometry(QtCore.QRect(0, 0, 141, 541))
        self.BGviolet.setStyleSheet("QLabel\n"
"{\n"
"background: #5e3b96;\n"
"}")
        self.BGviolet.setText("")
        self.BGviolet.setObjectName("BGviolet")
        self.schedule = QtWidgets.QPushButton(self.centralwidget)
        self.schedule.setGeometry(QtCore.QRect(10, 70, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.schedule.setFont(font)
        self.schedule.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.schedule.setObjectName("schedule")
        self.clients = QtWidgets.QPushButton(self.centralwidget)
        self.clients.setGeometry(QtCore.QRect(10, 160, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.clients.setFont(font)
        self.clients.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.clients.setObjectName("clients")
        self.SMS = QtWidgets.QPushButton(self.centralwidget)
        self.SMS.setGeometry(QtCore.QRect(10, 260, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.SMS.setFont(font)
        self.SMS.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.SMS.setObjectName("SMS")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(10, 430, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.help.setFont(font)
        self.help.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:15px;\n"
"}")
        self.help.setObjectName("help")
        self.log_out = QtWidgets.QPushButton(self.centralwidget)
        self.log_out.setGeometry(QtCore.QRect(10, 480, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.log_out.setFont(font)
        self.log_out.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:15px;\n"
"}")
        self.log_out.setObjectName("log_out")
        self.BGviolet_2 = QtWidgets.QLabel(self.centralwidget)
        self.BGviolet_2.setGeometry(QtCore.QRect(390, 130, 311, 321))
        self.BGviolet_2.setStyleSheet("QLabel\n"
"{\n"
"background: #5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.BGviolet_2.setText("")
        self.BGviolet_2.setObjectName("BGviolet_2")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(150, 10, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #5e3b96;\n"
"color:white;\n"
" border-radius:20px;\n"
"}")
        self.back.setObjectName("back")
        self.booknow1 = QtWidgets.QPushButton(self.centralwidget)
        self.booknow1.setGeometry(QtCore.QRect(460, 370, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.booknow1.setFont(font)
        self.booknow1.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"border-radius:10px;\n"
"}")
        self.booknow1.setObjectName("booknow1")
        self.numofsessions = QtWidgets.QLabel(self.centralwidget)
        self.numofsessions.setGeometry(QtCore.QRect(390, 200, 311, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.numofsessions.setFont(font)
        self.numofsessions.setLayoutDirection(QtCore.Qt.Qt::LayoutDirection::LeftToRight)
        self.numofsessions.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.numofsessions.setScaledContents(True)
        self.numofsessions.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignLeading|QtCore.Qt.Qt::AlignmentFlag::AlignLeft|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
        self.numofsessions.setObjectName("numofsessions")
        self.BGviolet.raise_()
        self.label_12.raise_()
        self.schedule.raise_()
        self.clients.raise_()
        self.SMS.raise_()
        self.help.raise_()
        self.log_out.raise_()
        self.BGviolet_2.raise_()
        self.back.raise_()
        self.booknow1.raise_()
        self.numofsessions.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.schedule.setText(_translate("MainWindow", "Schedule"))
        self.clients.setText(_translate("MainWindow", "Clients"))
        self.SMS.setText(_translate("MainWindow", "SMS"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.log_out.setText(_translate("MainWindow", "Log Out"))
        self.back.setText(_translate("MainWindow", "back"))
        self.booknow1.setText(_translate("MainWindow", "Proceed"))
        self.numofsessions.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Edited Details<br/>Saved!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
