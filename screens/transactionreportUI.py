

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1579, 751)
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
        self.widget_2.setMaximumSize(QtCore.QSize(139, 16777215))
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
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\JC\\Desktop\\asdasd\\qt\\../../softeng-main/logos/logog.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.coaches = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coaches.sizePolicy().hasHeightForWidth())
        self.coaches.setSizePolicy(sizePolicy)
        self.coaches.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.coaches.setFont(font)
        self.coaches.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.coaches.setObjectName("coaches")
        self.verticalLayout_4.addWidget(self.coaches)
        self.clients = QtWidgets.QPushButton(self.widget_5)
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
        self.verticalLayout_4.addWidget(self.clients)
        self.transactions = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transactions.sizePolicy().hasHeightForWidth())
        self.transactions.setSizePolicy(sizePolicy)
        self.transactions.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.transactions.setFont(font)
        self.transactions.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white ;\n"
"color:#5e3b96;\n"
" border-radius:10px;\n"
"}")
        self.transactions.setObjectName("transactions")
        self.verticalLayout_4.addWidget(self.transactions)
        self.verticalLayout_2.addWidget(self.widget_5)
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
        self.widget_4 = QtWidgets.QWidget(self.widget)
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
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #5e3b96;\n"
"color:white;\n"
" border-radius:20px;\n"
"}")
        self.back.setObjectName("back")
        self.verticalLayout_3.addWidget(self.back)
        self.help_2 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help_2.sizePolicy().hasHeightForWidth())
        self.help_2.setSizePolicy(sizePolicy)
        self.help_2.setMinimumSize(QtCore.QSize(75, 45))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        self.help_2.setFont(font)
        self.help_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #5e3b96;\n"
"color:white;\n"
" border-radius:20px;\n"
"}")
        self.help_2.setObjectName("help_2")
        self.verticalLayout_3.addWidget(self.help_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setStyleSheet("QWidget\n"
"{\n"
"background-color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.widget_6.setFont(font)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.reportname = QtWidgets.QTextEdit(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reportname.sizePolicy().hasHeightForWidth())
        self.reportname.setSizePolicy(sizePolicy)
        self.reportname.setMinimumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.reportname.setFont(font)
        self.reportname.setStyleSheet("QTextEdit\n"
"{\n"
"color:#5e3b96;\n"
"background-color:white;\n"
"}")
        self.reportname.setObjectName("reportname")
        self.horizontalLayout_2.addWidget(self.reportname)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.savetodesktop = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savetodesktop.sizePolicy().hasHeightForWidth())
        self.savetodesktop.setSizePolicy(sizePolicy)
        self.savetodesktop.setMinimumSize(QtCore.QSize(210, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.savetodesktop.setFont(font)
        self.savetodesktop.setStyleSheet("QPushButton{\n"
"background-color:white;\n"
"color:#5e3b96;\n"
"}")
        self.savetodesktop.setObjectName("savetodesktop")
        self.horizontalLayout_2.addWidget(self.savetodesktop)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.currentmonth = QtWidgets.QComboBox(self.widget_6)
        self.currentmonth.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.currentmonth.setFont(font)
        self.currentmonth.setStyleSheet("QComboBox\n"
"{\n"
"color:white;\n"
"}")
        self.currentmonth.setObjectName("currentmonth")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.currentmonth.addItem("")
        self.horizontalLayout_2.addWidget(self.currentmonth)
        self.verticalLayout_5.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_5.addWidget(self.widget_7)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem4)
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.horizontalLayout_3.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(self.widget_8)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.totalamount_2 = QtWidgets.QLineEdit(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.totalamount_2.setFont(font)
        self.totalamount_2.setStyleSheet("QLineEdit{\n"
"color:white;\n"
"}")
        self.totalamount_2.setObjectName("totalamount_2")
        self.verticalLayout_11.addWidget(self.totalamount_2)
        self.horizontalLayout_3.addWidget(self.widget_10)
        self.verticalLayout_5.addWidget(self.widget_8)
        self.horizontalLayout.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Reports"))
        self.coaches.setText(_translate("MainWindow", "Coaches"))
        self.clients.setText(_translate("MainWindow", "Clients"))
        self.transactions.setText(_translate("MainWindow", "Transactions"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.logout.setText(_translate("MainWindow", "Log Out"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.help_2.setText(_translate("MainWindow", "Help"))
        self.label_3.setText(_translate("MainWindow", "Report Name:"))
        self.savetodesktop.setText(_translate("MainWindow", "Save to Desktop"))
        self.label_4.setText(_translate("MainWindow", "Current Month:"))
        self.currentmonth.setItemText(0, _translate("MainWindow", " "))
        self.currentmonth.setItemText(1, _translate("MainWindow", "January"))
        self.currentmonth.setItemText(2, _translate("MainWindow", "February"))
        self.currentmonth.setItemText(3, _translate("MainWindow", "March"))
        self.currentmonth.setItemText(4, _translate("MainWindow", "April"))
        self.currentmonth.setItemText(5, _translate("MainWindow", "May"))
        self.currentmonth.setItemText(6, _translate("MainWindow", "June"))
        self.currentmonth.setItemText(7, _translate("MainWindow", "July"))
        self.currentmonth.setItemText(8, _translate("MainWindow", "August"))
        self.currentmonth.setItemText(9, _translate("MainWindow", "September"))
        self.currentmonth.setItemText(10, _translate("MainWindow", "October"))
        self.currentmonth.setItemText(11, _translate("MainWindow", "November"))
        self.currentmonth.setItemText(12, _translate("MainWindow", "December"))
        self.label_10.setText(_translate("MainWindow", "Total Amount:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
