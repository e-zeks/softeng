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
        self.centralwidget.setStyleSheet("QWidget\n"
"{\n"
"background: white;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(141, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setMaximumSize(QtCore.QSize(621, 171))
        self.logo.setStyleSheet("QLabel\n"
"{\n"
"D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/Anytime_Fitness_logo.png"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/Anytime_Fitness_logo.png"))
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.widget_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.login = QtWidgets.QPushButton(self.widget_3)
        self.login.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setMinimumSize(QtCore.QSize(0, 41))
        self.login.setMaximumSize(QtCore.QSize(280, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
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
"border-radius:20px;\n"
"}")
        self.login.setObjectName("login")
        self.horizontalLayout_2.addWidget(self.login)
        spacerItem5 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.widget_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.register_2 = QtWidgets.QPushButton(self.widget_4)
        self.register_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_2.sizePolicy().hasHeightForWidth())
        self.register_2.setSizePolicy(sizePolicy)
        self.register_2.setMinimumSize(QtCore.QSize(0, 41))
        self.register_2.setMaximumSize(QtCore.QSize(280, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
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
"border-radius:20px;\n"
"}")
        self.register_2.setObjectName("register_2")
        self.horizontalLayout_3.addWidget(self.register_2)
        spacerItem8 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_2.addWidget(self.widget_4)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.register_2.setText(_translate("MainWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
