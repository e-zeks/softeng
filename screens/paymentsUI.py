from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1335, 740)
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
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(100, 60))
        self.widget_4.setMaximumSize(QtCore.QSize(90, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.back = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMaximumSize(QtCore.QSize(90, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton\n"
"{\n"
"background-color: #5e3b96;\n"
"color:white;\n"
" border-radius:20px;\n"
"}")
        self.back.setObjectName("back")
        self.verticalLayout_3.addWidget(self.back)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"color: #5e3b96;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.widget_7)
        self.verticalLayout_4.addWidget(self.widget_6)
        self.widget_3 = QtWidgets.QWidget(self.widget_5)
        self.widget_3.setStyleSheet("QWidget\n"
"{\n"
"background-color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget_9)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.receiptno = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.receiptno.setFont(font)
        self.receiptno.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.receiptno.setText("")
        self.receiptno.setObjectName("receiptno")
        self.verticalLayout_5.addWidget(self.receiptno)
        self.label_11 = QtWidgets.QLabel(self.widget_9)
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
        self.amttotal = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.amttotal.setFont(font)
        self.amttotal.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.amttotal.setObjectName("amttotal")
        self.verticalLayout_5.addWidget(self.amttotal)
        self.label_9 = QtWidgets.QLabel(self.widget_9)
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
        self.amtpaid = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.amtpaid.setFont(font)
        self.amtpaid.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.amtpaid.setObjectName("amtpaid")
        self.verticalLayout_5.addWidget(self.amtpaid)
        self.label_4 = QtWidgets.QLabel(self.widget_9)
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
        self.paymentdate = QtWidgets.QDateEdit(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.paymentdate.setFont(font)
        self.paymentdate.setStyleSheet("QDateEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.paymentdate.setObjectName("paymentdate")
        self.verticalLayout_5.addWidget(self.paymentdate)
        self.horizontalLayout_5.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(self.widget_8)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget_10)
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
        self.verticalLayout_6.addWidget(self.label_5)
        self.customerlname = QtWidgets.QLineEdit(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.customerlname.setFont(font)
        self.customerlname.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.customerlname.setObjectName("customerlname")
        self.verticalLayout_6.addWidget(self.customerlname)
        self.label_6 = QtWidgets.QLabel(self.widget_10)
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
        self.verticalLayout_6.addWidget(self.label_6)
        self.customerfname = QtWidgets.QLineEdit(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.customerfname.setFont(font)
        self.customerfname.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.customerfname.setText("")
        self.customerfname.setObjectName("customerfname")
        self.verticalLayout_6.addWidget(self.customerfname)
        self.label_8 = QtWidgets.QLabel(self.widget_10)
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
        self.verticalLayout_6.addWidget(self.label_8)
        self.transactionhandler = QtWidgets.QLineEdit(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.transactionhandler.setFont(font)
        self.transactionhandler.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.transactionhandler.setObjectName("transactionhandler")
        self.verticalLayout_6.addWidget(self.transactionhandler)
        self.label_7 = QtWidgets.QLabel(self.widget_10)
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
        self.verticalLayout_6.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)  # Make QLineEdit not editable
        self.verticalLayout_6.addWidget(self.lineEdit)
        self.horizontalLayout_5.addWidget(self.widget_10)
        spacerItem2 = QtWidgets.QSpacerItem(60, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.widget_11 = QtWidgets.QWidget(self.widget_8)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(20, 666, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_7.addItem(spacerItem3)
        self.generatecode = QtWidgets.QPushButton(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generatecode.sizePolicy().hasHeightForWidth())
        self.generatecode.setSizePolicy(sizePolicy)
        self.generatecode.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.generatecode.setFont(font)
        self.generatecode.setStyleSheet("QPushButton\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.generatecode.setObjectName("generatecode")
        self.verticalLayout_7.addWidget(self.generatecode)
        self.save = QtWidgets.QPushButton(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        self.save.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton\n"
"{\n"
"background:white;\n"
"color:#5e3b96;\n"
"border-radius:20px;\n"
"}")
        self.save.setObjectName("save")
        self.verticalLayout_7.addWidget(self.save)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_5.addWidget(self.widget_11)
        self.horizontalLayout_2.addWidget(self.widget_8)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem5)
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
        self.label_2.setText(_translate("MainWindow", "Add a Payment"))
        self.label_3.setText(_translate("MainWindow", "Receipt Number:"))
        self.label_11.setText(_translate("MainWindow", "Amount Total:"))
        self.label_9.setText(_translate("MainWindow", "Amount Paid:"))
        self.label_4.setText(_translate("MainWindow", "Payment Date:"))
        self.label_5.setText(_translate("MainWindow", "Customer Last Name:"))
        self.label_6.setText(_translate("MainWindow", "Customer First Name:"))
        self.label_8.setText(_translate("MainWindow", "Transaction Handler:"))
        self.label_7.setText(_translate("MainWindow", "Code:"))
        self.generatecode.setText(_translate("MainWindow", "Generate Code"))
        self.save.setText(_translate("MainWindow", "Save Transaction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
