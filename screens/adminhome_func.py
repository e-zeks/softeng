from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.adminhomeUI import Ui_MainWindow

class AdminHomeWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()
    employeemanage_button = QtCore.pyqtSignal()
    clientmanage_button = QtCore.pyqtSignal()
    def __init__(self):
        super(AdminHomeWindow, self).__init__()
        self.setupUi(self)
        self.logout.clicked.connect(self.button_clicked)
        self.employees.clicked.connect(self.handle_employees)
        self.clients.clicked.connect(self.handle_clients)

    def button_clicked(self):
        print("Logging Out")
        self.logout_button.emit()

    def handle_employees(self):
        self.employeemanage_button.emit()

    def handle_clients(self):
        self.clientmanage_button.emit()
