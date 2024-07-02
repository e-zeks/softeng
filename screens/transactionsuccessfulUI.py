
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1754, 835)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"background:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 121))
        self.widget_2.setStyleSheet("QWidget\n"
"{\n"
"background: #5e3b96;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(435, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setMaximumSize(QtCore.QSize(421, 121))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/logog.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        spacerItem1 = QtWidgets.QSpacerItem(435, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.help = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        self.help.setMinimumSize(QtCore.QSize(75, 45))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        self.help.setFont(font)
        self.help.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #5e3b96;\n"
"color:white;\n"
" border-radius:20px;\n"
"}")
        self.help.setObjectName("help")
        self.verticalLayout_3.addWidget(self.help)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 62))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget_6.setFont(font)
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(372, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(371, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_9 = QtWidgets.QWidget(self.widget_7)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.coachline = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.coachline.setFont(font)
        self.coachline.setReadOnly(True)
        self.coachline.setObjectName("coachline")
        self.verticalLayout_5.addWidget(self.coachline)
        self.label_5 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.programplanline = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.programplanline.setFont(font)
        self.programplanline.setReadOnly(True)
        self.programplanline.setObjectName("programplanline")
        self.verticalLayout_5.addWidget(self.programplanline)
        self.label_6 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.packageline = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.packageline.setFont(font)
        self.packageline.setReadOnly(True)
        self.packageline.setObjectName("packageline")
        self.verticalLayout_5.addWidget(self.packageline)
        self.label_7 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.numberofsessionsline = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.numberofsessionsline.setFont(font)
        self.numberofsessionsline.setReadOnly(True)
        self.numberofsessionsline.setObjectName("numberofsessionsline")
        self.verticalLayout_5.addWidget(self.numberofsessionsline)
        self.label_8 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.totalamtline = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.totalamtline.setFont(font)
        self.totalamtline.setReadOnly(True)
        self.totalamtline.setObjectName("totalamtline")
        self.verticalLayout_5.addWidget(self.totalamtline)
        self.horizontalLayout_5.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(self.widget_7)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_11 = QtWidgets.QWidget(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(328, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.widget_11)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(327, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_4.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_10)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_12)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_6.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_12)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_6.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_12)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_6.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_12)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_6.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_12)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_6.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_12)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_6.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_12)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("QLineEdit\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_6.addWidget(self.lineEdit_7)
        self.verticalLayout_4.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.widget_10)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.verticalLayout_4.addWidget(self.widget_13)
        self.horizontalLayout_5.addWidget(self.widget_10)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 47))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(550, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.confirm = QtWidgets.QPushButton(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(21)
        self.confirm.setFont(font)
        self.confirm.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#5e3b96;\n"
"color:white;\n"
"border-radius:20px;\n"
"}")
        self.confirm.setObjectName("confirm")
        self.horizontalLayout_4.addWidget(self.confirm)
        spacerItem8 = QtWidgets.QSpacerItem(550, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout.addWidget(self.widget_8)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.label.setText(_translate("MainWindow", "Transaction Successful!"))
        self.label_4.setText(_translate("MainWindow", "Coach:"))
        self.label_5.setText(_translate("MainWindow", "Program Plan:"))
        self.label_6.setText(_translate("MainWindow", "Package:"))
        self.label_7.setText(_translate("MainWindow", "Number of Sessions:"))
        self.label_8.setText(_translate("MainWindow", "Total Amount:"))
        self.label_2.setText(_translate("MainWindow", "Selected Schedule"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Note: Please keep note of these details or take a picture of it as it will not be sent to you.</span></p></body></html>"))
        self.confirm.setText(_translate("MainWindow", "Confirm and Log Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
