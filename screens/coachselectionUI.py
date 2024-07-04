from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1531, 824)
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

        # Top blue widget with logo
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 171))
        self.widget_2.setStyleSheet("QWidget\n"
                                    "{\n"
                                    "background-color: #5e3b96;\n"
                                    "}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(141, 20, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setMaximumSize(QtCore.QSize(621, 171))
        self.logo.setStyleSheet("QLabel\n"
                                "{\n"
                                "background-url:\"C:\\Users\\JC\\Desktop\\SOFT ENG\\assets\\Anytime_Fitness_logo.png\";\n"
                                "}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(
                "C:\\Users\\JC\\Desktop\\softeng-main\\logos\\logog.jpg"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widget_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)

        # Help button widget
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.widget_14 = QtWidgets.QWidget(self.widget_3)
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setAlignment(QtCore.Qt.AlignTop)  # Align items to the top

        self.back = QtWidgets.QPushButton(self.widget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMinimumSize(QtCore.QSize(138, 40))  # Fixed size
        self.back.setMaximumSize(QtCore.QSize(138, 40))  # Fixed size
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton\n"
                                "{\n"
                                "background-color: #5e3b96;\n"
                                "color:white;\n"
                                " border-radius:20px;\n"
                                "}")
        self.back.setObjectName("back")
        self.verticalLayout_10.addWidget(self.back, alignment=QtCore.Qt.AlignTop)  # Align button to the top

        self.help = QtWidgets.QPushButton(self.widget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        self.help.setMinimumSize(QtCore.QSize(138, 41))  # Adjusted minimum width to half
        self.help.setMaximumSize(QtCore.QSize(138, 41))  # Adjusted maximum width to half
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        self.help.setFont(font)
        self.help.setStyleSheet("QPushButton\n"
                                "{\n"
                                "background-color: #5e3b96;\n"
                                "color:white;\n"
                                " border-radius:20px;\n"
                                "}")
        self.help.setObjectName("help")
        self.verticalLayout_10.addWidget(self.help, alignment=QtCore.Qt.AlignTop)  # Align button to the top

        self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.horizontalLayout_2.addWidget(self.widget_14)

        # Scroll area with dynamically created widgets
        self.scrollArea = QtWidgets.QScrollArea(self.widget_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1388, 575))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 8)

        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1531, 31))
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
        self.back.setText(_translate("MainWindow", "Log Out"))
        self.help.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
