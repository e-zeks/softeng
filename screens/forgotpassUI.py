from PyQt5 import QtCore, QtGui, QtWidgets
from . import forgotpass_func, enterOTPUI

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, login_window=None):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 190, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(19)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 290, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.registered_email = QtWidgets.QLineEdit(self.centralwidget)
        self.registered_email.setGeometry(QtCore.QRect(370, 350, 221, 22))
        self.registered_email.setObjectName("registered_email")
        self.sendOTP = QtWidgets.QPushButton(self.centralwidget)
        self.sendOTP.setGeometry(QtCore.QRect(400, 400, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        self.sendOTP.setFont(font)
        self.sendOTP.setStyleSheet("QPushButton\n"
"{\n"
"color: #5e3b96;\n"
"}")
        self.sendOTP.setObjectName("sendOTP")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 0, 421, 121))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/logog.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.BGviolet = QtWidgets.QLabel(self.centralwidget)
        self.BGviolet.setGeometry(QtCore.QRect(0, 0, 961, 121))
        self.BGviolet.setStyleSheet("QLabel\n"
"{\n"
"background: #5e3b96;\n"
"}")
        self.BGviolet.setText("")
        self.BGviolet.setObjectName("BGviolet")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(350, 180, 261, 301))
        self.label_7.setStyleSheet("QLabel\n"
"{\n"
"background: #5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.BGviolet.raise_()
        self.back.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.registered_email.raise_()
        self.sendOTP.raise_()
        self.label_6.raise_()
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

        # OTP window
        self.enterOTP_window = QtWidgets.QMainWindow()
        self.enterOTP_ui = enterOTPUI.Ui_MainWindow()
        self.enterOTP_ui.setupUi(self.enterOTP_window, MainWindow)

        self.sendOTP.clicked.connect(lambda: self.handle_sendOTP(MainWindow)) # send OTP button connector
        self.back.clicked.connect(lambda: forgotpass_func.handle_back(MainWindow, login_window))  # Back button connector

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Forgot <br/>Password?</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Registered Email</p></body></html>"))
        self.sendOTP.setText(_translate("MainWindow", "Send OTP"))

    #send OTP function handler
    def handle_sendOTP(self, MainWindow):
        email = self.registered_email.text()
        forgotpass_func.handle_sendOTP(email, MainWindow, self.enterOTP_window, self.enterOTP_ui)