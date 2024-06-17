from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from screens.startup2UI import Ui_MainWindow

class startup2_win(QMainWindow, Ui_MainWindow):
    client_signal_btn = pyqtSignal()
    employee_signal_btn = pyqtSignal()
    back_button = pyqtSignal()

    # Signal with two string parameters
    def __init__(self):
        super(startup2_win, self).__init__()
        super(startup2_win, self).__init__()
        self.setupUi(self)

        self.client.clicked.connect(self.handle_client)
        self.employee.clicked.connect(self.handle_employee)
        self.back.clicked.connect(self.handle_back)

    def handle_client(self):
        self.client_signal_btn.emit()

    def handle_employee(self):
        self.employee_signal_btn.emit()

    def handle_back(self):
        self.back_button.emit()
