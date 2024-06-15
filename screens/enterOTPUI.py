from PyQt5 import QtCore, QtGui, QtWidgets
from . import enterOTP_func, forgotpass_func

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, forgotpass_window=None):

        self.generated_otp = None
            
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BGviolet = QtWidgets.QLabel(self.centralwidget)
        self.BGviolet.setGeometry(QtCore.QRect(0, 0, 961, 121))
        self.BGviolet.setStyleSheet("QLabel\n"
"{\n"
"background: #5e3b96;\n"
"}")
        self.BGviolet.setText("")
        self.BGviolet.setObjectName("BGviolet")
        self.BGviolet_2 = QtWidgets.QLabel(self.centralwidget)
        self.BGviolet_2.setGeometry(QtCore.QRect(380, 150, 311, 311))
        self.BGviolet_2.setStyleSheet("QLabel\n"
"{\n"
"background: #5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.BGviolet_2.setText("")
        self.BGviolet_2.setObjectName("BGviolet_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 160, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
"font-color: rgb(255, 255, 255)\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 10, 411, 101))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/logo1.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.otp1 = QtWidgets.QLineEdit(self.centralwidget)
        self.otp1.setGeometry(QtCore.QRect(390, 260, 41, 41))
        self.otp1.setAutoFillBackground(False)
        self.otp1.setStyleSheet("QLineEdit {\n"
"border-radius: 10px;\n"
"background: white;\n"
"}")
        self.otp1.setObjectName("otp1")
        self.verifyOTP = QtWidgets.QPushButton(self.centralwidget)
        self.verifyOTP.setGeometry(QtCore.QRect(450, 340, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(False)
        self.verifyOTP.setFont(font)
        self.verifyOTP.setAutoFillBackground(False)
        self.verifyOTP.setStyleSheet("QPushButton {\n"
"border-radius: 10px;\n"
"background-color: white;\n"
"color: #5e3b96;\n"
"width: 20px;\n"
"}")
        self.verifyOTP.setIconSize(QtCore.QSize(100, 16))
        self.verifyOTP.setObjectName("verifyOTP")
        self.otp2 = QtWidgets.QLineEdit(self.centralwidget)
        self.otp2.setGeometry(QtCore.QRect(440, 260, 41, 41))
        self.otp2.setStyleSheet("QLineEdit {\n"
"border-radius: 10px;\n"
"background: white;\n"
"}")
        self.otp2.setObjectName("otp2")
        self.otp3 = QtWidgets.QLineEdit(self.centralwidget)
        self.otp3.setGeometry(QtCore.QRect(490, 260, 41, 41))
        self.otp3.setStyleSheet("QLineEdit {\n"
"border-radius: 10px;\n"
"background: white;\n"
"}")
        self.otp3.setObjectName("otp3")
        self.otp4 = QtWidgets.QLineEdit(self.centralwidget)
        self.otp4.setGeometry(QtCore.QRect(540, 260, 41, 41))
        self.otp4.setStyleSheet("QLineEdit {\n"
"border-radius: 10px;\n"
"background: white;\n"
"}")
        self.otp4.setObjectName("otp4")
        self.otp5 = QtWidgets.QLineEdit(self.centralwidget)
        self.otp5.setGeometry(QtCore.QRect(590, 260, 41, 41))
        self.otp5.setStyleSheet("QLineEdit {\n"
"border-radius: 10px;\n"
"background: white;\n"
"}")
        self.otp5.setObjectName("otp5")
        self.otp6 = QtWidgets.QLineEdit(self.centralwidget)
        self.otp6.setGeometry(QtCore.QRect(640, 260, 41, 41))
        self.otp6.setStyleSheet("QLineEdit {\n"
"border-radius: 10px;\n"
"background: white;\n"
"}")
        self.otp6.setObjectName("otp6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 380, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"color: white;\n"
"}")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.back_2 = QtWidgets.QPushButton(self.centralwidget)
        self.back_2.setGeometry(QtCore.QRect(10, 131, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.back_2.setFont(font)
        self.back_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #5e3b96;\n"
"color:white;\n"
" border-radius:20px;\n"
"}")
        self.back_2.setObjectName("back_2")
        self.BGviolet_2.raise_()
        self.BGviolet.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.otp1.raise_()
        self.verifyOTP.raise_()
        self.otp2.raise_()
        self.otp3.raise_()
        self.otp4.raise_()
        self.otp5.raise_()
        self.otp6.raise_()
        self.label_2.raise_()
        self.back_2.raise_()
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

        # Back button connector
        self.forgotpass_window = forgotpass_window
        self.back_2.clicked.connect(lambda: enterOTP_func.handle_back(MainWindow, forgotpass_window))

        self.verifyOTP.clicked.connect(lambda: enterOTP_func.handle_verifyOTP(MainWindow, self.generated_otp)) #verify otp button

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Enter One Time Password</span></p></body></html>"))
        self.verifyOTP.setText(_translate("MainWindow", "Verify OTP"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Did not receive a code? Resend now</span></p></body></html>"))
        self.back_2.setText(_translate("MainWindow", "back"))

