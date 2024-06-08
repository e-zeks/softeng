from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"background:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(10, 131, 61, 41))
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
        self.BGviolet = QtWidgets.QLabel(self.centralwidget)
        self.BGviolet.setGeometry(QtCore.QRect(0, 0, 961, 121))
        self.BGviolet.setStyleSheet("QLabel\n"
"{\n"
"background: #5e3b96;\n"
"}")
        self.BGviolet.setText("")
        self.BGviolet.setObjectName("BGviolet")
        self.BGviolet_2 = QtWidgets.QLabel(self.centralwidget)
        self.BGviolet_2.setGeometry(QtCore.QRect(80, 140, 821, 361))
        self.BGviolet_2.setStyleSheet("QLabel\n"
"{\n"
"background: #5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.BGviolet_2.setText("")
        self.BGviolet_2.setObjectName("BGviolet_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 160, 141, 29))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label.setObjectName("label")
        self.lname = QtWidgets.QLineEdit(self.centralwidget)
        self.lname.setGeometry(QtCore.QRect(110, 190, 220, 22))
        self.lname.setText("")
        self.lname.setObjectName("lname")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 230, 151, 29))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.fname = QtWidgets.QLineEdit(self.centralwidget)
        self.fname.setGeometry(QtCore.QRect(110, 270, 220, 22))
        self.fname.setObjectName("fname")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 300, 211, 29))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.contactnum = QtWidgets.QLineEdit(self.centralwidget)
        self.contactnum.setGeometry(QtCore.QRect(110, 340, 220, 22))
        self.contactnum.setObjectName("contactnum")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 380, 191, 29))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(110, 410, 220, 22))
        self.email.setObjectName("email")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 160, 141, 29))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(370, 190, 220, 22))
        self.username.setObjectName("username")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 230, 171, 29))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(370, 270, 220, 22))
        self.password.setText("")
        self.password.setObjectName("password")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 300, 211, 29))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.confirm_password = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_password.setGeometry(QtCore.QRect(370, 340, 220, 22))
        self.confirm_password.setObjectName("confirm_password")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 370, 241, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(650, 120, 191, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel\n"
"{\n"
"font-size:15;\n"
"color:white;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(640, 210, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(640, 280, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(640, 380, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.register_2.setFont(font)
        self.register_2.setStyleSheet("QPushButton\n"
"{\n"
"color:#5e3b96;\n"
"}\n"
"QPushButton\n"
"{\n"
"border-radius-15px;\n"
"}")
        self.register_2.setObjectName("register_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(260, 0, 421, 121))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../assets/logog.jpg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.BGviolet_2.raise_()
        self.back.raise_()
        self.BGviolet.raise_()
        self.label.raise_()
        self.lname.raise_()
        self.label_2.raise_()
        self.fname.raise_()
        self.label_3.raise_()
        self.contactnum.raise_()
        self.label_4.raise_()
        self.email.raise_()
        self.label_5.raise_()
        self.username.raise_()
        self.label_6.raise_()
        self.password.raise_()
        self.label_7.raise_()
        self.confirm_password.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.register_2.raise_()
        self.label_12.raise_()
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
        self.back.setText(_translate("MainWindow", "back"))
        self.label.setText(_translate("MainWindow", "Last Name:"))
        self.label_2.setText(_translate("MainWindow", "First Name:"))
        self.label_3.setText(_translate("MainWindow", "Contact Number:"))
        self.label_4.setText(_translate("MainWindow", "Email Address:"))
        self.label_5.setText(_translate("MainWindow", "Username:"))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.label_7.setText(_translate("MainWindow", "Confirm Password:"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#ffffff;\">Password must meet the following <br/>requirements:<br/><br/>At least 8 characters long<br/>One uppercase character <br/>One lowercase character<br/>One number<br/>No special characters</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:400;\">Welcome!</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt;\">Ensure that your details <br/>are final before clicking <br/>the ‘Register’ button.</span></p><p align=\"justify\"><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Please update the <br/>admin after successfully<br/>registering an account.</span></p></body></html>"))
        self.register_2.setText(_translate("MainWindow", "Register"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
