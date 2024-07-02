import random
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.paymentsUI import Ui_MainWindow

class PaymentWindow(QMainWindow, Ui_MainWindow):
    #screen buttons
    back_button = QtCore.pyqtSignal()
    generatecode_button = QtCore.pyqtSignal()

    #nav bar buttons
    employeemanage_button = QtCore.pyqtSignal()
    clientmanage_button = QtCore.pyqtSignal()
    reports_button = QtCore.pyqtSignal()
    userlogs_button = QtCore.pyqtSignal()
    maintenance_button = QtCore.pyqtSignal()
    help_button = QtCore.pyqtSignal()
    logout_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(PaymentWindow, self).__init__()
        self.setupUi(self)

        #screen buttons
        self.back.clicked.connect(self.backbutton_clicked)
        self.generatecode.clicked.connect(self.generatecode_clicked)

        #nav bar button
        self.employees.clicked.connect(self.handle_employees)
        self.clients.clicked.connect(self.handle_clients)
        self.report.clicked.connect(self.handle_reports)
        self.userlogs.clicked.connect(self.handle_userlogs)
        self.maintenance.clicked.connect(self.handle_maintenance)
        self.help.clicked.connect(self.handle_help)
        self.logout.clicked.connect(self.button_clicked)

        # self.receiptno
        # self.amttotal
        # self.amtpaid
        # self.paymentdate
        # self.customerlname
        # self.customerfname
        # self.transactionhandler


    def backbutton_clicked(self):
        self.back_button.emit()

    def generatecode_clicked(self):
        # Generate a 6-digit random number
        random_code = random.randint(100000, 999999)

        # Display the generated code in QLineEdit named lineEdit
        self.lineEdit.setText(str(random_code))

    #nav bar buttons
    def handle_employees(self):
        self.employeemanage_button.emit()

    def handle_clients(self):
        self.clientmanage_button.emit()

    def handle_reports(self):
        self.reports_button.emit()

    def handle_userlogs(self):
        self.userlogs_button.emit()

    def handle_maintenance(self):
        self.maintenance_button.emit()

    def handle_help(self):
        self.help_button.emit()

    def button_clicked(self):
        print("Logging Out")
        self.logout_button.emit()