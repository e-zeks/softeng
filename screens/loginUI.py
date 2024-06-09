from PyQt5 import QtCore, QtGui, QtWidgets
from . import login_func
from . import forgotpassUI
from main import connect_to_db

# Class for creating clickable label
class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("text-decoration: underline; color: blue;")

    def mousePressEvent(self, event):
        self.clicked.emit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, startup_window=None):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"background:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(10, 130, 61, 41))
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
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 0, 421, 121))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/logog.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(360, 380, 231, 23))
        self.login.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.login.setFont(font)
        self.login.setStyleSheet("QPushButton\n"
"{\n"
"color:#574999;\n"
"background:white;\n"
"border-radius:40px;\n"
"}")
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(360, 350, 231, 20))
        self.password.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"}")
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 320, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(360, 280, 231, 20))
        self.username.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"}")
        self.username.setObjectName("username")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 250, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 170, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(17)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.forgot = ClickableLabel(self.centralwidget) #clickable text
        self.forgot.setGeometry(QtCore.QRect(360, 420, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.forgot.setFont(font)
        self.forgot.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.forgot.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.forgot.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.forgot.setObjectName("forgot")
        self.BGviolet_2 = QtWidgets.QLabel(self.centralwidget)
        self.BGviolet_2.setGeometry(QtCore.QRect(350, 160, 251, 311))
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
        self.label_6.raise_()
        self.login.raise_()
        self.password.raise_()
        self.label_3.raise_()
        self.username.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.forgot.raise_()
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

        # Connect the login button click event to the handle_login method
        self.login.clicked.connect(lambda: self.handle_login(MainWindow))#login button
        self.back.clicked.connect(lambda: login_func.handle_back(MainWindow, startup_window))  # Back button connector
        self.forgot.clicked.connect(lambda: login_func.handle_forgot(MainWindow))  # forgot password connector

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label.setText(_translate("MainWindow", "Log In"))
        self.forgot.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Forgot Password?</span></p></body></html>"))

# login function handler
    def handle_login(self, MainWindow):
        username = self.username.text()
        password = self.password.text()
        conn = connect_to_db()
        if conn:
            login_func.handle_login(conn, username, password)
            conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())