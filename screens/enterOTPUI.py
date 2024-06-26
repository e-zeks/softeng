from PyQt5 import QtCore, QtGui, QtWidgets

class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("text-decoration: underline; color: blue;")

    def mousePressEvent(self, event):
        self.clicked.emit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1665, 739)
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
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 171))
        self.widget_2.setStyleSheet("QWidget\n"
"{\n"
"background-color: #5e3b96;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(141, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setMaximumSize(QtCore.QSize(621, 171))
        self.logo.setStyleSheet("QLabel\n"
"{\n"
"D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/Anytime_Fitness_logo.png\";\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/logog.jpg"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widget_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.back = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMinimumSize(QtCore.QSize(71, 41))
        self.back.setMaximumSize(QtCore.QSize(550, 350))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        font.setBold(True)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #5e3b96;\n"
"color:white;\n"
" border-radius:20px;\n"
"}")
        self.back.setObjectName("back")
        self.verticalLayout_6.addWidget(self.back)
        spacerItem3 = QtWidgets.QSpacerItem(20, 249, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_2.addWidget(self.widget_4)
        spacerItem4 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_5.setStyleSheet("QWidget\n"
"{\n"
"background-color: #5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        spacerItem7 = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.otp1 = QtWidgets.QLineEdit(self.widget_7)
        self.otp1.setMaximumSize(QtCore.QSize(16777215, 43))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        self.otp1.setFont(font)
        self.otp1.setAutoFillBackground(False)
        self.otp1.setStyleSheet("QLineEdit\n"
"{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"}")
        self.otp1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.otp1.setObjectName("otp1")
        self.horizontalLayout_4.addWidget(self.otp1)
        self.otp2 = QtWidgets.QLineEdit(self.widget_7)
        self.otp2.setMaximumSize(QtCore.QSize(16777215, 43))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        self.otp2.setFont(font)
        self.otp2.setAutoFillBackground(False)
        self.otp2.setStyleSheet("QLineEdit\n"
"{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"}")
        self.otp2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.otp2.setObjectName("otp2")
        self.horizontalLayout_4.addWidget(self.otp2)
        self.otp3 = QtWidgets.QLineEdit(self.widget_7)
        self.otp3.setMaximumSize(QtCore.QSize(16777215, 43))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        self.otp3.setFont(font)
        self.otp3.setAutoFillBackground(False)
        self.otp3.setStyleSheet("QLineEdit\n"
"{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"}")
        self.otp3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.otp3.setObjectName("otp3")
        self.horizontalLayout_4.addWidget(self.otp3)
        self.otp4 = QtWidgets.QLineEdit(self.widget_7)
        self.otp4.setMaximumSize(QtCore.QSize(16777215, 43))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        self.otp4.setFont(font)
        self.otp4.setAutoFillBackground(False)
        self.otp4.setStyleSheet("QLineEdit\n"
"{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"}")
        self.otp4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.otp4.setObjectName("otp4")
        self.horizontalLayout_4.addWidget(self.otp4)
        self.otp5 = QtWidgets.QLineEdit(self.widget_7)
        self.otp5.setMaximumSize(QtCore.QSize(16777215, 43))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        self.otp5.setFont(font)
        self.otp5.setAutoFillBackground(False)
        self.otp5.setStyleSheet("QLineEdit\n"
"{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"}")
        self.otp5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.otp5.setObjectName("otp5")
        self.horizontalLayout_4.addWidget(self.otp5)
        self.otp6 = QtWidgets.QLineEdit(self.widget_7)
        self.otp6.setMaximumSize(QtCore.QSize(16777215, 43))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        self.otp6.setFont(font)
        self.otp6.setAutoFillBackground(False)
        self.otp6.setStyleSheet("QLineEdit\n"
"{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"}")
        self.otp6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.otp6.setObjectName("otp6")
        self.horizontalLayout_4.addWidget(self.otp6)
        self.verticalLayout_3.addWidget(self.widget_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem8)
        self.verifyOTP = QtWidgets.QPushButton(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        self.verifyOTP.setFont(font)
        self.verifyOTP.setStyleSheet("QPushButton\n"
"{\n"
"color: #5e3b96;\n"
"background-color:white;\n"
"border-radius:20px;\n"
"}")
        self.verifyOTP.setObjectName("VerifyOTP")
        self.verticalLayout_3.addWidget(self.verifyOTP)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem9)
        self.resendOTP = ClickableLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.resendOTP.setFont(font)
        self.resendOTP.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.resendOTP.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resendOTP.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.resendOTP.setObjectName("forgot")
        self.verticalLayout_3.addWidget(self.resendOTP)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.horizontalLayout_3.addWidget(self.widget_6)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.horizontalLayout_2.addWidget(self.widget_5)
        spacerItem12 = QtWidgets.QSpacerItem(450, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Enter One Time</p><p align=\"center\">Password</p></body></html>"))
        self.verifyOTP.setText(_translate("MainWindow", "Verify OTP"))
        self.resendOTP.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Did not receive a code? </span></p><p align=\"center\"><span style=\" text-decoration: underline;\">Resend now</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
