from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
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


def connect_functions(main_window, func_module):
    main_window.ui.guest.clicked.connect(func_module.handle_guest)
    main_window.ui.login.clicked.connect(func_module.handle_login)
    main_window.ui.register_2.clicked.connect(func_module.handle_register)
