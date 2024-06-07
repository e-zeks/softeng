from PyQt5 import QtCore, QtGui, QtWidgets
from . import login_func
from main import connect_to_db

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(10, 130, 61, 41))
        self.back.setObjectName("back")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(390, 210, 135, 170))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.login = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.forgot = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.forgot.setAlignment(QtCore.Qt.AlignCenter)
        self.forgot.setObjectName("forgot")
        self.verticalLayout.addWidget(self.forgot)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 961, 121))
        self.label_4.setObjectName("label_4")
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

        self.login.clicked.connect(lambda: self.handle_login(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back.setText(_translate("MainWindow", "back"))
        self.label.setText(_translate("MainWindow", "Log In"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.forgot.setText(_translate("MainWindow", "Forgot Password?"))

    #login function handler
    def handle_login(self, MainWindow):
        username = self.username.text()
        password = self.password.text()
        conn = connect_to_db()
        if conn:
            login_successful = login_func.handle_login(conn, username, password)
            #if login_successful:
             #   print("Login successful - Proceed with next steps")
            #else:
              #  print("Login failed - Inform the user")
            conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
