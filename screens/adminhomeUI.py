# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\zek\3rd yr comsci\summer\CS 304\soft eng\github\qt\adminhome.ui'
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
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.employees = QtWidgets.QPushButton(self.centralwidget)
        self.employees.setGeometry(QtCore.QRect(10, 60, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        self.employees.setFont(font)
        self.employees.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:15px;\n"
"}")
        self.employees.setObjectName("employees")
        self.clients = QtWidgets.QPushButton(self.centralwidget)
        self.clients.setGeometry(QtCore.QRect(10, 120, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        self.clients.setFont(font)
        self.clients.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:15px;\n"
"}")
        self.clients.setObjectName("clients")
        self.payments = QtWidgets.QPushButton(self.centralwidget)
        self.payments.setGeometry(QtCore.QRect(8, 180, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        self.payments.setFont(font)
        self.payments.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:15px;\n"
"}")
        self.payments.setObjectName("payments")
        self.report = QtWidgets.QPushButton(self.centralwidget)
        self.report.setGeometry(QtCore.QRect(8, 240, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        self.report.setFont(font)
        self.report.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:15px;\n"
"}")
        self.report.setObjectName("report")
        self.user_logs = QtWidgets.QPushButton(self.centralwidget)
        self.user_logs.setGeometry(QtCore.QRect(8, 300, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        self.user_logs.setFont(font)
        self.user_logs.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:15px;\n"
"}")
        self.user_logs.setObjectName("user_logs")
        self.SMS = QtWidgets.QPushButton(self.centralwidget)
        self.SMS.setGeometry(QtCore.QRect(8, 360, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        self.SMS.setFont(font)
        self.SMS.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:15px;\n"
"}")
        self.SMS.setObjectName("SMS")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(8, 430, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        self.help.setFont(font)
        self.help.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:20px;\n"
"}")
        self.help.setObjectName("help")
        self.log_out = QtWidgets.QPushButton(self.centralwidget)
        self.log_out.setGeometry(QtCore.QRect(10, 480, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        self.log_out.setFont(font)
        self.log_out.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:20px;\n"
"}")
        self.log_out.setObjectName("log_out")
        self.BGviolet = QtWidgets.QLabel(self.centralwidget)
        self.BGviolet.setGeometry(QtCore.QRect(0, 0, 141, 541))
        self.BGviolet.setStyleSheet("QLabel\n"
"{\n"
"background: #5e3b96;\n"
"}")
        self.BGviolet.setText("")
        self.BGviolet.setObjectName("BGviolet")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 141, 41))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/logog.jpg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(240, 150, 621, 171))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.logo.setFont(font)
        self.logo.setStyleSheet("QLabel\n"
"{\n"
"background-url:\"C:\\Users\\JC\\Desktop\\SOFT ENG\\assets\\Anytime_Fitness_logo.png\";\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/Anytime_Fitness_logo.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.BGviolet.raise_()
        self.employees.raise_()
        self.clients.raise_()
        self.payments.raise_()
        self.report.raise_()
        self.user_logs.raise_()
        self.SMS.raise_()
        self.help.raise_()
        self.log_out.raise_()
        self.label_12.raise_()
        self.logo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.employees.setText(_translate("MainWindow", "Employees"))
        self.clients.setText(_translate("MainWindow", "Clients"))
        self.payments.setText(_translate("MainWindow", "Payments"))
        self.report.setText(_translate("MainWindow", "Report"))
        self.user_logs.setText(_translate("MainWindow", "User Logs"))
        self.SMS.setText(_translate("MainWindow", "SMS"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.log_out.setText(_translate("MainWindow", "Log Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
