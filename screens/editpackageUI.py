from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1144, 854)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("QWidget\n"
"{\n"
"background-color:#5e3b96;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(121, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\zek\\3rd yr comsci\\summer\\CS 304\\soft eng\\github\\qt\\../logos/logog.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.employees = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employees.sizePolicy().hasHeightForWidth())
        self.employees.setSizePolicy(sizePolicy)
        self.employees.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.employees.setFont(font)
        self.employees.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.employees.setObjectName("employees")
        self.verticalLayout_2.addWidget(self.employees)
        self.clients = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clients.sizePolicy().hasHeightForWidth())
        self.clients.setSizePolicy(sizePolicy)
        self.clients.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.clients.setFont(font)
        self.clients.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.clients.setObjectName("clients")
        self.verticalLayout_2.addWidget(self.clients)
        self.payments = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.payments.sizePolicy().hasHeightForWidth())
        self.payments.setSizePolicy(sizePolicy)
        self.payments.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.payments.setFont(font)
        self.payments.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.payments.setObjectName("payments")
        self.verticalLayout_2.addWidget(self.payments)
        self.report = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.report.sizePolicy().hasHeightForWidth())
        self.report.setSizePolicy(sizePolicy)
        self.report.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.report.setFont(font)
        self.report.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.report.setObjectName("report")
        self.verticalLayout_2.addWidget(self.report)
        self.userlogs = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userlogs.sizePolicy().hasHeightForWidth())
        self.userlogs.setSizePolicy(sizePolicy)
        self.userlogs.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.userlogs.setFont(font)
        self.userlogs.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.userlogs.setObjectName("userlogs")
        self.verticalLayout_2.addWidget(self.userlogs)
        self.maintenance = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maintenance.sizePolicy().hasHeightForWidth())
        self.maintenance.setSizePolicy(sizePolicy)
        self.maintenance.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.maintenance.setFont(font)
        self.maintenance.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.maintenance.setObjectName("maintenance")
        self.verticalLayout_2.addWidget(self.maintenance)
        self.help = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        self.help.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.help.setFont(font)
        self.help.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.help.setObjectName("help")
        self.verticalLayout_2.addWidget(self.help)
        self.logout = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout.sizePolicy().hasHeightForWidth())
        self.logout.setSizePolicy(sizePolicy)
        self.logout.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.logout.setFont(font)
        self.logout.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.logout.setObjectName("logout")
        self.verticalLayout_2.addWidget(self.logout)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setStyleSheet("QWidget\n"
"{\n"
"background-color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.widget_8 = QtWidgets.QWidget(self.widget_6)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_5.addWidget(self.widget_8)
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.packagename = QtWidgets.QLineEdit(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packagename.sizePolicy().hasHeightForWidth())
        self.packagename.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.packagename.setFont(font)
        self.packagename.setStyleSheet("QLineEdit{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"}")
        self.packagename.setReadOnly(True)
        self.packagename.setObjectName("packagename")
        self.verticalLayout_5.addWidget(self.packagename)
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.packageprice = QtWidgets.QLineEdit(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.packageprice.setFont(font)
        self.packageprice.setStyleSheet("QLineEdit{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"}")
        self.packageprice.setObjectName("packageprice")
        self.verticalLayout_5.addWidget(self.packageprice)
        self.label_5 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.packagedetails = QtWidgets.QTextEdit(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packagedetails.sizePolicy().hasHeightForWidth())
        self.packagedetails.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.packagedetails.setFont(font)
        self.packagedetails.setStyleSheet("QTextEdit{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"}")
        self.packagedetails.setObjectName("packagedetails")
        self.verticalLayout_5.addWidget(self.packagedetails)
        self.horizontalLayout_2.addWidget(self.widget_6)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.widget_5.setFont(font)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cancel = QtWidgets.QPushButton(self.widget_5)
        self.cancel.setMinimumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_4.addWidget(self.cancel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.save = QtWidgets.QPushButton(self.widget_5)
        self.save.setMinimumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.save.setObjectName("save")
        self.horizontalLayout_4.addWidget(self.save)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.employees.setText(_translate("MainWindow", "Employees"))
        self.clients.setText(_translate("MainWindow", "Clients"))
        self.payments.setText(_translate("MainWindow", "Payments"))
        self.report.setText(_translate("MainWindow", "Report"))
        self.userlogs.setText(_translate("MainWindow", "User Logs"))
        self.maintenance.setText(_translate("MainWindow", "Maintenance"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.logout.setText(_translate("MainWindow", "Log Out"))
        self.label_8.setText(_translate("MainWindow", "Edit Package"))
        self.label_2.setText(_translate("MainWindow", "Package ID:"))
        self.label_3.setText(_translate("MainWindow", "Package Name:"))
        self.label_6.setText(_translate("MainWindow", "Package Price:"))
        self.label_5.setText(_translate("MainWindow", "Package Details:"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.save.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
