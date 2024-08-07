
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 896)
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
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\JC\\Desktop\\DYNAMIC UI\\../SOFT ENG/assets/logog.jpg"))
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
        self.widget_11 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setMaximumSize(QtCore.QSize(89, 16777215))
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.back = QtWidgets.QPushButton(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMinimumSize(QtCore.QSize(60, 50))
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
        self.verticalLayout_4.addWidget(self.back)
        spacerItem = QtWidgets.QSpacerItem(20, 730, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widget_11)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_10 = QtWidgets.QWidget(self.widget_3)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.databaselabel_3 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(50)
        font.setBold(True)
        self.databaselabel_3.setFont(font)
        self.databaselabel_3.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.databaselabel_3.setObjectName("databaselabel_3")
        self.horizontalLayout_8.addWidget(self.databaselabel_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.widget_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.databaselabel = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(True)
        self.databaselabel.setFont(font)
        self.databaselabel.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.databaselabel.setObjectName("databaselabel")
        self.horizontalLayout_3.addWidget(self.databaselabel)
        spacerItem5 = QtWidgets.QSpacerItem(487, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.backup = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backup.sizePolicy().hasHeightForWidth())
        self.backup.setSizePolicy(sizePolicy)
        self.backup.setMinimumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.backup.setFont(font)
        self.backup.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#5e3b96 ;\n"
"color:white;\n"
" border-radius:10px;\n"
"}")
        self.backup.setObjectName("backup")
        self.horizontalLayout_2.addWidget(self.backup)
        spacerItem7 = QtWidgets.QSpacerItem(500, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.restore = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restore.sizePolicy().hasHeightForWidth())
        self.restore.setSizePolicy(sizePolicy)
        self.restore.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.restore.setFont(font)
        self.restore.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#5e3b96 ;\n"
"color:white;\n"
" border-radius:10px;\n"
"}")
        self.restore.setObjectName("restore")
        self.horizontalLayout_2.addWidget(self.restore)
        spacerItem8 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_3.addWidget(self.widget_5)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.packageslabel = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(True)
        self.packageslabel.setFont(font)
        self.packageslabel.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.packageslabel.setObjectName("packageslabel")
        self.horizontalLayout_4.addWidget(self.packageslabel)
        spacerItem11 = QtWidgets.QSpacerItem(480, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem12 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.addpackage = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addpackage.sizePolicy().hasHeightForWidth())
        self.addpackage.setSizePolicy(sizePolicy)
        self.addpackage.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.addpackage.setFont(font)
        self.addpackage.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#5e3b96 ;\n"
"color:white;\n"
" border-radius:10px;\n"
"}")
        self.addpackage.setObjectName("addpackage")
        self.horizontalLayout_5.addWidget(self.addpackage)
        spacerItem13 = QtWidgets.QSpacerItem(500, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.editpackage = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editpackage.sizePolicy().hasHeightForWidth())
        self.editpackage.setSizePolicy(sizePolicy)
        self.editpackage.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.editpackage.setFont(font)
        self.editpackage.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#5e3b96 ;\n"
"color:white;\n"
" border-radius:10px;\n"
"}")
        self.editpackage.setObjectName("editpackage")
        self.horizontalLayout_5.addWidget(self.editpackage)
        spacerItem14 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.verticalLayout_3.addWidget(self.widget_7)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem15)
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem16 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_6.addItem(spacerItem16)
        self.databaselabel_2 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(True)
        self.databaselabel_2.setFont(font)
        self.databaselabel_2.setStyleSheet("QLabel\n"
"{\n"
"color:#5e3b96;\n"
"}")
        self.databaselabel_2.setObjectName("databaselabel_2")
        self.horizontalLayout_6.addWidget(self.databaselabel_2)
        spacerItem17 = QtWidgets.QSpacerItem(505, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.verticalLayout_3.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.widget_3)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem18 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem18)
        self.addcoach = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addcoach.sizePolicy().hasHeightForWidth())
        self.addcoach.setSizePolicy(sizePolicy)
        self.addcoach.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.addcoach.setFont(font)
        self.addcoach.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#5e3b96 ;\n"
"color:white;\n"
" border-radius:10px;\n"
"}")
        self.addcoach.setObjectName("addcoach")
        self.horizontalLayout_7.addWidget(self.addcoach)
        spacerItem19 = QtWidgets.QSpacerItem(500, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem19)
        self.editcoach = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editcoach.sizePolicy().hasHeightForWidth())
        self.editcoach.setSizePolicy(sizePolicy)
        self.editcoach.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        self.editcoach.setFont(font)
        self.editcoach.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#5e3b96 ;\n"
"color:white;\n"
" border-radius:10px;\n"
"}")
        self.editcoach.setObjectName("editcoach")
        self.horizontalLayout_7.addWidget(self.editcoach)
        spacerItem20 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem20)
        self.verticalLayout_3.addWidget(self.widget_9)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem21)
        self.horizontalLayout.addWidget(self.widget_3)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem22)
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
        self.userlogs.setText(_translate("MainWindow", "History"))
        self.maintenance.setText(_translate("MainWindow", "Maintenance"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.logout.setText(_translate("MainWindow", "Log Out"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.databaselabel_3.setText(_translate("MainWindow", "Maintenance"))
        self.databaselabel.setText(_translate("MainWindow", "Database"))
        self.backup.setText(_translate("MainWindow", "Backup"))
        self.restore.setText(_translate("MainWindow", "Recovery"))
        self.packageslabel.setText(_translate("MainWindow", "Packages"))
        self.addpackage.setText(_translate("MainWindow", "Add Package"))
        self.editpackage.setText(_translate("MainWindow", "Update Package"))
        self.databaselabel_2.setText(_translate("MainWindow", "Coaches"))
        self.addcoach.setText(_translate("MainWindow", "Add Coach"))
        self.editcoach.setText(_translate("MainWindow", "Update Coach Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
