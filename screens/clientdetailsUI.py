from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1425, 785)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"background:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        self.label_13.setPixmap(QtGui.QPixmap("C:\\Users\\JC\\Desktop\\softeng-main\\logos\\logog.jpg"))
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
        self.back = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMinimumSize(QtCore.QSize(75, 45))
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
        self.verticalLayout_3.addWidget(self.back)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.widget_4)
        spacerItem3 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setStyleSheet("QWidget\n"
"{\n"
"background:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.lname = QtWidgets.QLineEdit(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.lname.setFont(font)
        self.lname.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.lname.setText("")
        self.lname.setObjectName("lname")
        self.verticalLayout_5.addWidget(self.lname)
        self.label_11 = QtWidgets.QLabel(self.widget_6)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.fname = QtWidgets.QLineEdit(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.fname.setFont(font)
        self.fname.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.fname.setObjectName("fname")
        self.verticalLayout_5.addWidget(self.fname)
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.address = QtWidgets.QLineEdit(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.address.setFont(font)
        self.address.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.address.setText("")
        self.address.setObjectName("address")
        self.verticalLayout_5.addWidget(self.address)
        self.label_9 = QtWidgets.QLabel(self.widget_6)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.dateEdit = QtWidgets.QDateEdit(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("QDateEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_5.addWidget(self.dateEdit)
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.contact_number = QtWidgets.QLineEdit(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.contact_number.setFont(font)
        self.contact_number.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.contact_number.setObjectName("contact_number")
        self.verticalLayout_5.addWidget(self.contact_number)
        self.horizontalLayout_4.addWidget(self.widget_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget_7)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.emailaddress = QtWidgets.QLineEdit(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.emailaddress.setFont(font)
        self.emailaddress.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.emailaddress.setObjectName("emailaddress")
        self.verticalLayout_4.addWidget(self.emailaddress)
        self.label_12 = QtWidgets.QLabel(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.username = QtWidgets.QLineEdit(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.username.setFont(font)
        self.username.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.username.setObjectName("username")
        self.verticalLayout_4.addWidget(self.username)
        self.label = QtWidgets.QLabel(self.widget_7)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.password = QtWidgets.QLineEdit(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.password.setObjectName("password")
        self.verticalLayout_4.addWidget(self.password)
        self.label_7 = QtWidgets.QLabel(self.widget_7)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.programplan = QtWidgets.QComboBox(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.programplan.setFont(font)
        self.programplan.setStyleSheet("QComboBox\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.programplan.setObjectName("programplan")
        self.programplan.addItem("")
        self.programplan.setItemText(0, "")
        self.programplan.addItem("")
        self.programplan.addItem("")
        self.programplan.addItem("")
        self.programplan.addItem("")
        self.verticalLayout_4.addWidget(self.programplan)
        self.label_8 = QtWidgets.QLabel(self.widget_7)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.medical_conditions = QtWidgets.QLineEdit(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.medical_conditions.setFont(font)
        self.medical_conditions.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.medical_conditions.setObjectName("medical_conditions")
        self.verticalLayout_4.addWidget(self.medical_conditions)
        self.horizontalLayout_4.addWidget(self.widget_7)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.widget_8 = QtWidgets.QWidget(self.widget_5)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(40)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_10 = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_10.setScaledContents(False)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.save = QtWidgets.QPushButton(self.widget_8)
        self.save.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"}\n"
"QPushButton\n"
"{\n"
"border-radius:20px;\n"
"}")
        self.save.setObjectName("register_2")
        self.verticalLayout.addWidget(self.save)
        self.horizontalLayout_4.addWidget(self.widget_8)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_3.addWidget(self.widget_5)
        spacerItem8 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back.setText(_translate("MainWindow", "Cancel"))
        self.label_2.setText(_translate("MainWindow", "Last Name:"))
        self.label_11.setText(_translate("MainWindow", "First Name:"))
        self.label_6.setText(_translate("MainWindow", "Address:"))
        self.label_9.setText(_translate("MainWindow", "Birthdate:"))
        self.label_4.setText(_translate("MainWindow", "Contact Number:"))
        self.label_5.setText(_translate("MainWindow", "Email Address:"))
        self.label_12.setText(_translate("MainWindow", "Username:"))
        self.label.setText(_translate("MainWindow", "Password:"))
        self.label_7.setText(_translate("MainWindow", "Program Plan:"))
        self.programplan.setItemText(1, _translate("MainWindow", "Weight Loss"))
        self.programplan.setItemText(2, _translate("MainWindow", "Body Building"))
        self.programplan.setItemText(3, _translate("MainWindow", "Strength Training"))
        self.programplan.setItemText(4, _translate("MainWindow", "Calisthenics"))
        self.label_8.setText(_translate("MainWindow", "Medical Conditions:"))
        self.label_3.setText(_translate("MainWindow", "Welcome!"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Please enter the details required and make sure your details are correct before you book.</span></p><p align=\"center\"><span style=\" font-size:28pt;\">Looking forward to our coaching sessions soon!</span></p></body></html>"))
        self.save.setText(_translate("MainWindow", "Save and Proceed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
