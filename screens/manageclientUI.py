from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 928)
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
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\JC\\Desktop\\asdasd\\qt\\../../softeng-main/logos/logog.jpg"))
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QtCore.QSize(89, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.back = QtWidgets.QPushButton(self.widget_4)
        self.back.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        font.setBold(False)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton\n"
                                "{\n"
                                "background-color: #5e3b96;\n"
                                "color:white;\n"
                                " border-radius:20px;\n"
                                "}")
        self.back.setObjectName("back")
        self.verticalLayout_3.addWidget(self.back)
        self.edit = QtWidgets.QPushButton(self.widget_4)
        self.edit.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        font.setBold(False)
        self.edit.setFont(font)
        self.edit.setStyleSheet("QPushButton\n"
                                "{\n"
                                "background-color: #5e3b96;\n"
                                "color:white;\n"
                                " border-radius:20px;\n"
                                "}")
        self.edit.setObjectName("edit")
        self.verticalLayout_3.addWidget(self.edit)
        self.save = QtWidgets.QPushButton(self.widget_4)
        self.save.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        font.setBold(False)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton\n"
                                "{\n"
                                "background-color: #5e3b96;\n"
                                "color:white;\n"
                                " border-radius:20px;\n"
                                "}")
        self.save.setObjectName("save")
        self.verticalLayout_3.addWidget(self.save)
        self.previous = QtWidgets.QPushButton(self.widget_4)
        self.previous.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        self.previous.setFont(font)
        self.previous.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "background-color: #5e3b96;\n"
                                    "color:white;\n"
                                    "border-radius:20px;\n"
                                    "}")
        self.previous.setObjectName("previous")
        self.verticalLayout_3.addWidget(self.previous)
        self.next = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next.sizePolicy().hasHeightForWidth())
        self.next.setSizePolicy(sizePolicy)
        self.next.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        font.setBold(False)
        self.next.setFont(font)
        self.next.setStyleSheet("QPushButton\n"
                                "{\n"
                                "background-color: #5e3b96;\n"
                                "color:white;\n"
                                " border-radius:20px;\n"
                                "}")
        self.next.setObjectName("next")
        self.verticalLayout_3.addWidget(self.next)
        spacerItem1 = QtWidgets.QSpacerItem(20, 730, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.widget_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Search bar
        self.search_bar = QtWidgets.QLineEdit(self.widget_3)
        self.search_bar.setPlaceholderText("Search...")

        self.verticalLayout_4.addWidget(self.search_bar)

        self.table = QtWidgets.QTableWidget(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.table.setFont(font)
        self.table.setStyleSheet("QTableWidget\n"
                                 "{\n"
                                 "color:#5e3b96;\n"
                                 "}")
        self.table.setObjectName("table")
        self.table.setColumnCount(8)
        self.table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        self.verticalLayout_4.addWidget(self.table)

        self.horizontalLayout.addWidget(self.widget_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem3)
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
        self.back.setText(_translate("MainWindow", "Back"))
        self.edit.setText(_translate("MainWindow", "Edit"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.previous.setText(_translate("MainWindow", "Previous"))
        self.next.setText(_translate("MainWindow", "Next"))
        item = self.table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "EmployeeID"))
