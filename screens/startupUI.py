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
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"background:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget\n"
"{\n"
"background: white;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(160, 10, 621, 171))
        self.logo.setStyleSheet("QLabel\n"
"{\n"
"background-url:\"C:\\Users\\JC\\Desktop\\SOFT ENG\\assets\\Anytime_Fitness_logo.png\";\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/Anytime_Fitness_logo.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.logo.setObjectName("logo")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setEnabled(True)
        self.register_2.setGeometry(QtCore.QRect(400, 430, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_2.sizePolicy().hasHeightForWidth())
        self.register_2.setSizePolicy(sizePolicy)
        self.register_2.setMinimumSize(QtCore.QSize(0, 41))
        self.register_2.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.register_2.setFont(font)
        self.register_2.setStyleSheet("QPushButton\n"
"{\n"
"color: white;\n"
"background: #574999;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"border-radius:60px;\n"
"}")
        self.register_2.setObjectName("register_2")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setEnabled(True)
        self.login.setGeometry(QtCore.QRect(400, 350, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setMinimumSize(QtCore.QSize(0, 41))
        self.login.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.login.setFont(font)
        self.login.setStyleSheet("QPushButton\n"
"{\n"
"color: white;\n"
"background: #574999;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"border-radius:90px;\n"
"}")
        self.login.setObjectName("login")
        self.guest = QtWidgets.QPushButton(self.centralwidget)
        self.guest.setEnabled(True)
        self.guest.setGeometry(QtCore.QRect(400, 270, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guest.sizePolicy().hasHeightForWidth())
        self.guest.setSizePolicy(sizePolicy)
        self.guest.setMinimumSize(QtCore.QSize(0, 41))
        self.guest.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.guest.setFont(font)
        self.guest.setStyleSheet("QPushButton\n"
"{\n"
"color: white;\n"
"background: #574999;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"border-radius:60px;\n"
"}")
        self.guest.setObjectName("guest")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.register_2.setText(_translate("MainWindow", "Register"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.guest.setText(_translate("MainWindow", "Guest"))


#buttons handler
def connect_functions(main_window, func_module):
    main_window.ui.guest.clicked.connect(func_module.handle_guest)
    main_window.ui.login.clicked.connect(lambda: func_module.handle_login(main_window))
    main_window.ui.register_2.clicked.connect(func_module.handle_register)
