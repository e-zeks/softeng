from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

# Add the 'functions' directory to the system path
functions_directory = os.path.join(os.path.dirname(__file__), '..', 'functions')
sys.path.append(functions_directory)

# Import functions from startup_func.py
from startup_func import handle_guest, handle_login, handle_register

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 190, 321, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.guest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.guest.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guest.sizePolicy().hasHeightForWidth())
        self.guest.setSizePolicy(sizePolicy)
        self.guest.setMinimumSize(QtCore.QSize(0, 24))
        self.guest.setMaximumSize(QtCore.QSize(16777215, 24))
        self.guest.setObjectName("guest")
        self.verticalLayout.addWidget(self.guest)
        self.login = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.register_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.register_2.setObjectName("register_2")
        self.verticalLayout.addWidget(self.register_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.guest.setText(_translate("MainWindow", "Guest"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.register_2.setText(_translate("MainWindow", "Register"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        self.guest.clicked.connect(handle_guest)
        self.login.clicked.connect(handle_login)
        self.register_2.clicked.connect(handle_register)
